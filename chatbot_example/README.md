We will use chatterbot to create a basic chatbot.

# Requirements
Python 3.7
install requirements.txt

Install spacy models: `python -m spacy download en_core_web_sm` and `python -m spacy download fr_core_news_sm`

If you have the following error : `Can't find model 'en'`, then open the `C:\Users\USER\AppData\Local\Programs\Python\Python37\lib\site-packages\chatterbot\tagging.py` equivalent file to replace `self.nlp = spacy.load(self.language.ISO_639_1.lower())` with 
```
if self.language.ISO_639_1.lower() == 'en':
    self.nlp = spacy.load('en_core_web_sm')
else:
    self.nlp = spacy.load(self.language.ISO_639_1.lower())
```