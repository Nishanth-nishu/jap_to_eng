import torch
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration
from nltk.translate.bleu_score import sentence_bleu, SmoothingFunction
import logging
import os

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

def calculate_bleu(references, hypothesis):
    smoothie = SmoothingFunction().method1
    return sentence_bleu(references, hypothesis, smoothing_function=smoothie)

def evaluate_model(model_path, model_name, test_data_path):
    model = load_model(model_path, model_name)
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)

    with open(test_data_path, 'r', encoding='utf-8') as f:
        test_data = [line.strip().split('\t') for line in f]

    bleu_scores = []
    for ja_sentence, en_sentence in test_data:
        try:
            translation = translate_text(ja_sentence, model, tokenizer)
            references = [en_sentence.split()]
            hypothesis = translation.split()
            bleu = calculate_bleu(references, hypothesis)
            bleu_scores.append(bleu)
        except Exception as e:
            logging.error(f"Error during translation or
