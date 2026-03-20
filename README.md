# 🛂 AI ID Authenticity Verification System

An AI-powered system to detect potential fraud in identity documents using OCR, image analysis, and intelligent reasoning.

---

## 🚀 Features

* 🖼️ Upload ID images for analysis
* 🔍 OCR-based text extraction
* 🧠 AI-powered fraud detection
* ⚠️ Tampering detection (image inconsistencies)
* 📊 Structured fraud analysis report
* 📚 RAG-based validation using knowledge base

---

## 🛠️ Tech Stack

* **Frontend**: Streamlit
* **Backend**: Python
* **AI Models**: OpenAI / Google Gemini
* **OCR**: Tesseract / Image Processing
* **Vector DB**: FAISS
* **Libraries**: Pandas, OpenCV, dotenv

---

## 📂 Project Structure

```
id_authenticity/
│
├── app.py
├── frontend.py
├── build_index.py
├── rag_engine.py
├── ocr.py
├── tamper_check.py
│
├── knowledge.txt
├── requirements.txt
│
├── uploads/          # (ignored in git)
├── vector_db/        # (ignored in git)
│
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/id_authenticity.git
cd id_authenticity
```

---

### 2. Create virtual environment

```
python -m venv .venv
.venv\Scripts\activate
```

---

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

### 4. Setup environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

---

### 5. Run the application

```
streamlit run app.py
```

---

## 💡 How It Works

1. User uploads an ID image
2. OCR extracts text from the document
3. Image is analyzed for tampering
4. Extracted data is validated using RAG
5. AI generates a fraud analysis report

---

## 📊 Example Output

* Detected name, DOB, ID number
* Tampering indicators (blur, mismatch, edits)
* Risk assessment
* AI-generated explanation

---

## ⚠️ Important

* Do NOT commit `.env` (contains API keys)
* Ensure Tesseract OCR is installed (if required)
* This is a prototype — not production-grade fraud detection

---

## 🔮 Future Improvements

* Real-time government database validation
* Deepfake / face matching detection
* Multi-document support (passport, license, Aadhaar)
* Confidence scoring system
* API deployment

---

## 👤 Author

**Abjith**

---

## ⭐ Support

If you find this useful, give it a ⭐ on GitHub!
