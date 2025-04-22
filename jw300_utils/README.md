
# Hausa Language Chatbot using MarianMT and Flask

This project implements a Hausa-language chatbot using a Transformer-based model (MarianMT), built with Python and Flask. It focuses on natural language understanding and translation to facilitate real-time responses for customer inquiries in Hausa.

## 🔧 Technologies Used

- **Python**
- **NLTK** – for preprocessing
- **Hugging Face Transformers** – for fine-tuning MarianMT
- **Flask** – for building and deploying the chatbot interface

---

## 📦 Setup Instructions

1. **Install Dependencies**

   ```bash
   pip install nltk transformers flask
   ```

2. **Preprocess the Corpus**

   - Tokenization of text data
   - Padding sequences for model compatibility

   Preprocessing prepares parallel corpora into a training-ready format.

3. **Model Configuration**

   - Loaded and fine-tuned the **MarianMT** model using Hausa ↔ English parallel corpora.
   - Saved trained weights for deployment.

4. **Chatbot Deployment with Flask**

   - Integrated basic chatbot logic into a Flask web app.
   - Handled user inputs and returned translated/generated responses.

---

## 🤖 Chatbot Architecture

1. **Training Phase**
   - Loaded Hausa-English parallel corpora.
   - Fine-tuned MarianMT translation model using Hugging Face's `Trainer` API.

2. **Inference Pipeline**
   - User Input → Tokenization
   - Hausa-to-English Translation
   - Response Generation (or retrieval)
   - Translation back to Hausa

3. **Simulation & Evaluation**
   - Simulated user sessions with sample queries.
   - Measured:
     - **BLEU Scores** for translation quality
     - **Latency** for response time
     - **Fluency** for user satisfaction

---

## 📊 Evaluation Metrics

| Metric         | Description                          |
|----------------|--------------------------------------|
| **BLEU Score** | Evaluated accuracy of translations   |
| **Latency**    | Time taken to generate responses     |
| **Fluency**    | Human-like naturalness of responses  |


## ✅ Status

- [x] Model fine-tuned on Hausa-English corpus  
- [x] Basic chatbot logic deployed with Flask  
- [x] Evaluation completed (BLEU, latency, fluency)  


## 📁 Project Structure

/project-root
│
├── app.py                 # Flask application
├── model/                 # Saved MarianMT model
├── data/                  # Parallel corpora and processed data
├── preprocess.py          # Tokenization and padding script
├── train.py               # Fine-tuning script
└── README.md              # Project documentation
