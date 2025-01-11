import torch
from transformers import MBart50TokenizerFast, MBartForConditionalGeneration, MBartConfig
import logging
from datasets import load_dataset
from torch.utils.data import DataLoader, Dataset
from tqdm import tqdm
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

class JapaneseEnglishDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)

def train():
    model_name = "facebook/mbart-large-50-many-to-many-mmt"
    dataset = load_dataset("opus_mt", "ja-en")
    tokenizer = MBart50TokenizerFast.from_pretrained(model_name)

    def tokenize_function(examples):
        return tokenizer(examples["translation"]["ja"], examples["translation"]["en"], truncation=True)

    tokenized_datasets = dataset.map(tokenize_function, batched=True)
    train_dataset = JapaneseEnglishDataset(tokenized_datasets["train"]["input_ids"], tokenized_datasets["train"]["labels"])
    train_dataloader = DataLoader(train_dataset, batch_size=4, shuffle=True)

    config = MBartConfig.from_pretrained(model_name)
    model = MBartForConditionalGeneration.from_pretrained(model_name, config=config).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)

    epochs = 3
    for epoch in range(epochs):
        model.train()
        for batch in tqdm(train_dataloader):
            optimizer.zero_grad()
            input_ids = batch['input_ids'].to(device)
            attention_mask = batch['attention_mask'].to(device)
            labels = batch['labels'].
