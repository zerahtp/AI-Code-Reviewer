# 🧑‍💻 AI Code Reviewer

AI Code Reviewer, Python dosyalarınızı yapay zeka (LLM) ile analiz ederek **hataları tespit eder**, **iyileştirme önerileri sunar** ve **en iyi uygulamaları değerlendirir**. Bu uygulama, [Ollama](https://ollama.com/) üzerinden çalışan LLaMA 3.2 modelini kullanır ve sade bir **Streamlit** arayüzü ile kullanıcı dostu bir deneyim sağlar.


---

## 🚀 Özellikler

- ✅ Python dosyalarını yükleyerek analiz etme
- 🤖 LLaMA 3.2 LLM ile kod gözden geçirme
- 💡 Hatalar, kod kokuları, iyileştirme önerileri
- 📥 İnceleme çıktısını `.txt` dosyası olarak indirme
- 🌐 Streamlit tabanlı web arayüzü

---

## 📦 Kullanılan Teknolojiler

| Teknoloji | Açıklama |
|----------|----------|
| [Streamlit](https://streamlit.io/) | Web uygulaması arayüzü |
| [Ollama](https://ollama.com/) | Yerel LLM sunucusu |
| `llama3.2` | Kod incelemesi için kullanılan büyük dil modeli |
| `subprocess` | Python üzerinden terminal komutlarını çalıştırma |
| `locale` | Kodlama türünü sistemden almak için |

---

## 🛠️ Kurulum

### 1. Gerekli Ortamı Kur
```bash
git clone https://github.com/zerahtp/AI-Code-Reviewer.git
cd AI-Code-Reviewer

