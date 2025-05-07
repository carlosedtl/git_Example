Sentiment Analysis for Amazon Product Reviews
This project performs sentiment analysis on Amazon product reviews using a pre-trained DistilBERT model. The code processes a dataset of Amazon reviews, breaks the text into sentences, and analyzes the sentiment of each sentence.
Features

Loads Amazon product reviews dataset from Kaggle
Processes text using spaCy for sentence segmentation
Performs sentiment analysis using Hugging Face's transformers library
Visualizes sentiment distribution in the reviews

Installation

Clone this repository:
bashgit clone https://github.com/yourusername/amazon-reviews-sentiment-analysis.git
cd amazon-reviews-sentiment-analysis

Install the required dependencies:
bashpip install kagglehub pandas transformers matplotlib spacy

Download the English language model for spaCy:
bashpython -m spacy download en_core_web_sm


Usage

Make sure you have a Kaggle account and API token configured for kagglehub to access the dataset.
Run the main script:
bashpython sentiment_analysis.py

The script will:

Download the Amazon product reviews dataset
Process the first 50 reviews
Split the text into sentences
Analyze sentiment for each sentence
Display results and statistics



Dependencies

kagglehub - For downloading the dataset
pandas - For data manipulation
transformers - For sentiment analysis model
matplotlib - For visualization
spacy - For natural language processing and sentence segmentation

Dataset
This project uses the "Amazon Product Reviews" dataset by arhamrumi on Kaggle.
Model
Sentiment analysis is performed using the "distilbert-base-uncased-finetuned-sst-2-english" model from Hugging Face, which classifies text as either POSITIVE or NEGATIVE.
Example Output
The script outputs:

The combined text of all reviews
A list of extracted sentences
Sentiment analysis results for each sentence
A count of positive vs negative sentences

License
[Specify your license here]
Contributors
[Your name or GitHub username]RetryClaude does not have the ability to run the code it generates yet.Claude can make mistakes. Please double-check responses.