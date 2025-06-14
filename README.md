# 🧠 RAGMed: LangChain Medical Chatbot

**RAGMed** is a Flask-based medical chatbot that uses **Retrieval-Augmented Generation (RAG)** to answer health-related queries. Built on top of **LangChain**, **Groq-hosted LLaMA models**, and **Pinecone vector storage**, it processes and retrieves answers from a structured medical PDF — **The Gale Encyclopedia of Medicine (2nd Edition)**.

---

## 🚀 Features

- 🧾 Accepts medical queries via an interactive web interface
- 📄 Retrieves answers from a vectorized PDF medical encyclopedia
- 🧠 Powered by **LangChain** and **Groq-hosted LLaMA/Gemma models**
- 🔍 Uses **Pinecone** to store and search vector embeddings
- ⚙️ Built with **Flask** and includes evaluation support

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS (in `/templates`, `/static`)
- **Backend:** Python, Flask
- **LLM Interface:** LangChain with Groq API
- **Vector DB:** Pinecone (via `langchain-pinecone`)
- **Embeddings:** Hugging Face Sentence Transformers
- **Docs Source:** *The Gale Encyclopedia of Medicine (2nd Ed)*

---

## 📂 Project Structure

```bash
ragmed-langchain-medical-chatbot/
├── app.py # Main Flask app
├── src/
│ ├── helper.py # PDF loading, embeddings
│ ├── prompt.py # Custom system prompt
├── templates/
│ └── chat.html # Frontend UI
├── static/
│ └── style.css # Chat styling
├── test_data.json # For evaluation
├── requirements.txt # Python dependencies
├── .env # API keys (Groq, Pinecone)
├── .gitignore
└── README.md
```

## 🔐 API Keys Setup
This project requires two API keys to function:

1. **Groq API Key**
Used to access Groq-hosted LLaMA or Gemma models via LangChain

🔗 Get your key here: https://console.groq.com/keys

2. **Pinecone API Key**
Used to connect with Pinecone vector database for document retrieval

🔗 Sign up at: https://www.pinecone.io/

### ⚠ Important: Never upload your actual API key to GitHub. Use a .env file or environment variables for security.

---

## ⚙️ Setup Instructions

1. **Clone the Repository**
```bash
git clone https://github.com/YOUR_USERNAME/ragmed-langchain-medical-chatbot.git
cd ragmed-langchain-medical-chatbot
```

2. **Set Up Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Set Your API Keys**

Create a .env file in the root directory and add:
```bash
GROQ_API_KEY=your_groq_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

5. **Run the App**
```bash
python app.py
```

Visit in browser:
http://127.0.0.1:8080

---

## 📚 Knowledge Source
All answers are retrieved from:

The Gale Encyclopedia of Medicine, 2nd Edition (Volumes A–B)
A trusted reference used to embed and vectorize responses.

---

## 👤 Author

Developed by Kushal S

---

## 📄 License

This project is created for educational and demonstration purposes only.
It is not intended for real clinical use.

---

## 📬 Feedback

Feel free to open issues or submit pull requests.  
We welcome suggestions to improve functionality and UI/UX!
