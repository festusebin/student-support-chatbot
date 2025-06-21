# 🎓 AI-Powered Student Support Chatbot

This is a simple Natural Language Processing (NLP) chatbot designed to answer frequently asked questions (FAQs) from university students. It uses TF-IDF vectorization and cosine similarity to match student queries with predefined answers from a dataset.

---

## 📚 Features

- Responds to student questions using a preloaded FAQ dataset
- Uses TF-IDF + cosine similarity for semantic matching
- Built with modular Python files for reusability and clarity
- Easy to upgrade to deep learning models like BERT in the future

---

## 🧪 Sample Questions

- What are the admission requirements?
- When is the application deadline?
- How do I apply for scholarships?
- What’s the tuition fee?

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/festusebin/student-support-chatbot.git
cd student-support-chatbot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the chatbot

```bash
python chatbot/main.py
```

Project Structure

```bash
student-support-chatbot/
├── chatbot/
│   ├── __init__.py
│   ├── main.py           # CLI chatbot runner
│   └── nlp_engine.py     # NLP matching logic
├── data/
│   └── faq_dataset.csv   # Dataset with Q&A pairs
├── requirements.txt
└── README.md
```

### 4. Dependencies

#### Add the following to your requirements.txt file

```bash
pandas
scikit-learn
```

### 5 👨‍💻 Built By
Festus Ebin
Aspiring MSc student in AI and Software Engineering
GitHub: @festusebin

📜 License
This project is licensed under the MIT License.
