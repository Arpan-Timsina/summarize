# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")
model = AutoModelForSeq2SeqLM.from_pretrained("sshleifer/distilbart-cnn-12-6")