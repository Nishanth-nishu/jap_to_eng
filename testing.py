import torch
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration
import logging
from concurrent.futures import ThreadPoolExecutor

# Set up logging
logging.basicConfig(level=logging.INFO)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_model(model_path, model_name):
    model = MBartForConditionalGeneration.from_pretrained(model_name).to(device)
    model.load_state_dict(torch.load(model_path))
    model.eval()
    return model

def translate_text(input_text, model, tokenizer):
    inputs = tokenizer(
        input_text, return_tensors="pt", truncation=True, max_length=128, padding="max_length"
    ).to(device)
    outputs = model.generate(
        input_ids=inputs['input_ids'], attention_mask=inputs['attention_mask'], max_length=128, num_beams=4
    )
    translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return translation

def main():
    model_name = 'facebook/mbart-large-50-many-to-many-mmt'
    model_path = "japanese_english_translator.pt"
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)
    model = load_model(model_path, model_name)

    test_texts = ["こんにちは", "お元気ですか"]
    with ThreadPoolExecutor() as executor:
        translations = list(executor.map(lambda text: translate_text(text, model, tokenizer), test_texts))
    for text, translation in zip(test_texts, translations):
        logging.info(f"Original: {text} | Translation: {translation}")

if __name__ == "__main__":
    main()
