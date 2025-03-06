import streamlit as st
import subprocess
import locale
import os

def review_code(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            code = file.read()

        # Prompt İngilizce bırakıldı
        prompt = f"Analyze the following code for potential bugs, improvements, and best practices:\n\n{code}"

        result = subprocess.run(
            ["ollama", "run", "llama3.2", prompt],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )

        encoding = locale.getpreferredencoding()
        review_output = result.stdout.decode(encoding, errors="ignore").strip()

        with open("review_output.txt", "w", encoding="utf-8") as output_file:
            output_file.write(review_output)

        return review_output

    except Exception as e:
        return f"Hata oluştu: {e}"

# Streamlit Arayüzü
st.set_page_config(page_title="Kod İnceleyici", page_icon="🧑‍💻", layout="wide")

st.title("🧑‍💻 AI Destekli Kod İnceleyici")
st.write("Python dosyanızı yükleyin ve yapay zeka destekli kod inceleme alın!")

uploaded_file = st.file_uploader("Python dosyanızı yükleyin", type=["py"])

if uploaded_file is not None:
    file_path = f"temp_{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success(f"✅ Dosya '{uploaded_file.name}' başarıyla yüklendi!")

    if st.button("Kod İncele 🚀"):
        with st.spinner("Kod analiz ediliyor..."):
            review_output = review_code(file_path)

        st.subheader("📄 AI Kod İnceleme Sonucu")
        st.text_area("İnceleme Sonucu", review_output, height=300)

        with open("review_output.txt", "rb") as file:
            st.download_button(label="📥 İnceleme Sonucunu İndir", data=file, file_name="review_output.txt",
                               mime="text/plain")

        os.remove(file_path)  # Geçici dosyayı kaldır
