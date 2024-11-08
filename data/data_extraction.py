import os
from rich import print

# Path to the directory containing article files
directory_path = "./articles"

def read_article_file(file_path):
    with open(file_path, "r") as file:
        content = file.read()
    
    # Split content by markers
    try:
        article_content = content.split("Article:")[1].split("Article Summary:")[0].strip()
        article_summary = content.split("Article Summary:")[1].strip()
        return article_content, article_summary
    except IndexError:
        print(f"[bold red]Error in file format:[/bold red] {file_path}")
        return None, None

# Process each file in the directory
for filename in os.listdir(directory_path):
    if filename.endswith(".txt"):
        file_path = os.path.join(directory_path, filename)
        article_content, article_summary = read_article_file(file_path)
        
        if article_content and article_summary:
            print(f"\n[bold cyan]File:[/bold cyan] {filename}")
            print(f"[bold yellow]Article:[/bold yellow] {article_content}")
            print(f"[bold green]Summary:[/bold green] {article_summary}")
        else:
            print(f"[bold red]Skipping file due to format error:[/bold red] {filename}")
