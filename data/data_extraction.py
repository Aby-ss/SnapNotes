from rich import print
from rich.traceback import install
install(show_locals=True)

import newspaper
from transformers import pipeline, BartForConditionalGeneration, BartTokenizer

# Summarization Pipeline with Hugging Face BART
def setup_summarizer():
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    return summarizer

# Extract and Summarize the Article
def summarize_article(url):
    # Set up the summarizer
    summarizer = setup_summarizer()
    
    # Fetch the article
    article = newspaper.Article(url)
    article.download()
    article.parse()

    # Display the full article text
    print("[bold cyan]Full Article Text:[/bold cyan]")
    print(article.text)
    
    # Summarize the article
    summary = summarizer(article.text, max_length=130, min_length=30, do_sample=False)
    print("\n[bold green]Summary:[/bold green]")
    print(summary[0]['summary_text'])

# Example Usage
url = "https://www.bbc.com/news/world-europe-60603432"  # Replace with your desired news article URL
summarize_article(url)
