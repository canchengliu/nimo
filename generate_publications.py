import pandas as pd
# import csv

def format_authors(authors_str):
    authors = [author.strip() for author in authors_str.split(';')]
    if not authors:
        return ""
    elif len(authors) == 1:
        return authors[0]
    else:
        # Bold your name (assuming "Wode Ni" based on your example)
        formatted_authors = []
        for author in authors:
            if author.strip().lower() in ["liu cancheng", "liu-cancheng"]:
                formatted_authors.append(f"**{author.strip()}**")
            else:
                formatted_authors.append(author.strip())
        return ", ".join(formatted_authors[:-1]) + ", and " + formatted_authors[-1]

def generate_markdown(publication):
    title = publication['Title']
    pdf_url = publication['PDF_url']
    authors = format_authors(publication['Authors'])
    publication_name = publication['Publication']
    year = publication['Year']
    publisher = publication['Publisher']
    volume = publication['Volume']
    number = publication['Number']
    pages = publication['Pages']
    
    markdown = f"""### [**{title}**]({pdf_url})

{authors}.  
*{publication_name}*, **{volume}**({number}), {pages}, {year}.  
[[PDF]({pdf_url})]
"""
    return markdown

def csv_to_markdown(csv_filepath, markdown_filepath):
    # with open(csv_filepath, 'r', encoding='utf-8') as csvfile, open(markdown_filepath, 'w', encoding='utf-8') as mdfile:
    with open(markdown_filepath, 'w', encoding='utf-8') as mdfile:
        df = pd.read_excel(csv_filepath)
        # reader = csv.DictReader(csvfile)
        for i, row in df.iterrows():
            md_entry = generate_markdown(row)
            mdfile.write(md_entry + "\n")

if __name__ == "__main__":
    input_csv = '/Users/liucancheng/Downloads/citations.xlsx'      # Path to your CSV file
    output_md = '/Users/liucancheng/Downloads/citations.md'       # Desired output Markdown file
    csv_to_markdown(input_csv, output_md)
    print(f"Markdown file '{output_md}' has been generated successfully.")

