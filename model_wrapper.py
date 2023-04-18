from ray import serve
from transformers import pipeline

@serve.deployment("/")
class EmailClassifier:
    def __init__(self):
        self.model = pipeline("zero-shot-classification", model="MoritzLaurer/mDeBERTa-v3-base-mnli-xnli")
    def __call__(self):

        # candidate_labels = ["Учетная запись", "РПД", "Учебные планы", "Личный кабинет"]
        # output = classifier(text, candidate_labels, multi_label=False, use_fast=False)
        # return output["labels"][0], output["scores"][0]
        pass