import tiktoken

from rich.traceback import install
install(show_locals=True)

def tokenize_text(text):
    """
    Tokenizes the given text using the 'cl100k_base' encoding.

    Args:
        text (str): The input text to tokenize.

    Returns:
        list: List of token IDs.
    """
    # Use cl100k_base, which is compatible with GPT-3.5 and GPT-4 models
    encoding = tiktoken.get_encoding("cl100k_base")

    tokens = encoding.encode(text)
    print(f"Tokenized Text: {tokens}")
    print(f"Number of Tokens: {len(tokens)}")

    return tokens

def split_into_chunks(text, max_tokens=1000):
    """
    Splits text into smaller chunks based on the token limit.

    Args:
        text (str): The input text to split.
        max_tokens (int): Maximum number of tokens per chunk.

    Yields:
        list: A chunk of token IDs within the specified limit.
    """
    encoding = tiktoken.get_encoding("cl100k_base")
    tokens = encoding.encode(text)

    for i in range(0, len(tokens), max_tokens):
        yield tokens[i:i + max_tokens]

# Example paragraph to test the functions
paragraph = """
Artificial intelligence is transforming industries across the world. From healthcare to finance,
AI-driven solutions are becoming more integral to everyday life. Technologies like chatbots,
recommendation systems, and autonomous vehicles are reshaping our future.
"""

# Test the tokenize_text function
print("Tokenization Test:")
tokens = tokenize_text(paragraph)

# Test the split_into_chunks function
print("\nChunking Test:")
for chunk in split_into_chunks(paragraph, max_tokens=10):
    print(chunk)
