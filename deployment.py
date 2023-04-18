from ray import serve
from model_wrapper import EmailClassifier

serve.run(EmailClassifier().bind())