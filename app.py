from flask import Flask, render_template, request
import torch
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

def load_model_and_tokenizer(model_dir):
    """
    Load the saved model and tokenizer.
    """
    logging.info("Loading the saved model and tokenizer...")
    tokenizer = MBart50TokenizerFast.from_pretrained(model_dir)
    model = MBartForConditionalGeneration.from_pretrained(model_dir).to(device)
    return model, tokenizer

model_dir = r"E:\New folder\data-pipeline-project\saved_model"  # Path to the saved model directory
model, tokenizer = load_model_and_tokenizer(model_dir)

# Set language codes for Japanese to English translation
tokenizer.src_lang = "ja_XX"
tokenizer.tgt_lang = "en_XX"

def translate_text(input_text, model, tokenizer):
    """
    Translate Japanese text into English using the model.
    """
    try:
        # Tokenize input text
        inputs = tokenizer(
            input_text,
            return_tensors="pt",
            truncation=True,
            max_length=128,
            padding="max_length"
        ).to(device)

        # Generate translation
        outputs = model.generate(
            input_ids=inputs['input_ids'],
            attention_mask=inputs['attention_mask'],
            max_length=128,
            num_beams=4
        )

        # Decode the output
        translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return translation
    except Exception as e:
        logging.error(f"Error during translation: {e}")
        raise

@app.route('/', methods=['GET', 'POST'])
def index():
    translation = ""
    if request.method == 'POST':
        input_text = request.form['input_text']
        translation = translate_text(input_text, model, tokenizer)
    return render_template('index.html', translation=translation)

if __name__ == "__main__":
    app.run(debug=True)
