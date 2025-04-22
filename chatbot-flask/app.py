from flask import Flask, request, jsonify, render_template
from transformers import pipeline, MarianMTModel, MarianTokenizer
from langdetect import detect

app = Flask(__name__)

# Load chatbot model
chatbot_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-small")

# Translation utility functions
def get_model_and_tokenizer(src, tgt):
    model_name = f"Helsinki-NLP/opus-mt-{src}-{tgt}"
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    model = MarianMTModel.from_pretrained(model_name)
    return model, tokenizer

def translate(text, model, tokenizer):
    tokens = tokenizer([text], return_tensors="pt", padding=True)
    translated = model.generate(**tokens)
    return tokenizer.decode(translated[0], skip_special_tokens=True)

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

# Chatbot logic
def basic_chatbot_response(user_input):
    response = chatbot_pipeline(user_input, max_length=50, pad_token_id=50256)
    return response[0]['generated_text']

# Route for UI
@app.route('/')
def index():
    return render_template('index.html')

# Chat endpoint
@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Step 1: Detect language
    user_lang = detect_language(user_input)

    # Step 2: Translate to English if needed
    if user_lang != "en":
        try:
            model_en, tokenizer_en = get_model_and_tokenizer(user_lang, "en")
            user_input = translate(user_input, model_en, tokenizer_en)
        except Exception as e:
            return jsonify({"error": f"Translation to English failed: {str(e)}"}), 500

    # Step 3: Get chatbot response
    response = basic_chatbot_response(user_input)

    # Step 4: Translate back to user's language if needed
    if user_lang != "en":
        try:
            model_back, tokenizer_back = get_model_and_tokenizer("en", user_lang)
            response = translate(response, model_back, tokenizer_back)
        except Exception as e:
            return jsonify({"error": f"Translation back failed: {str(e)}"}), 500

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)