"""A module that... """
import requests
from bs4 import BeautifulSoup
import re

def hypothetical_function(x):
    print(x)

def ers2bib(url):
    """
    Convert URL of a publication from USDA, Economic Research Service into a BibTeX entry.

    Args:
        url (str): A character string of the URL for the publication.

    Returns:
        str: A character vector of a BibTeX entry that can be pasted into a .bib file.

    Examples:
        ers2bib("https://www.ers.usda.gov/publications/pub-details/?pubid=104776")
    """

    #page = scrape_page(url)
    #authors = extract_authors(page)
    #title = extract_title(page)
    #pub = extract_pubmeta(page)
    #date = extract_date(page)
    #key = gen_cite_key(authors, date['year'])
    
    #bib = f"@misc{{{key}, 
    #author = {{{' and '.join(authors)}}}, 
    #title = {{{' '.join(title)}}}, 
    #address = {{U.S. Department of Agriculture, Economic Research Service}}, 
    #howpublished = {{{pub}}}, year = {{{date['year']}}}, 
    #url = {{{url}}} }}"
    bib = "a bibtex entry"

    return bib


def scrape_page(url):
    """
    Extract the page text from a given URL.

    Args:
        url (str): The URL of the webpage to scrape.

    Returns:
        BeautifulSoup: Parsed HTML content of the page.
    """
    response = requests.get(url)
    page = BeautifulSoup(response.content, 'html.parser')
    
    return page

def extract_authors(page):
    """
    Extract and clean the list of authors from the webpage.

    Args:
        page (BeautifulSoup): Parsed HTML content of the page.

    Returns:
        list: A list of cleaned author names.
    """
    authors = page.select("p.byline")
    authors = [author.get_text() for author in authors]

    if authors and authors[0].startswith("by"):
        authors[0] = authors[0][2:]

    authors = [author.replace(", ", " and ") for author in authors]
    authors = [author.replace(" and and ", " and ") for author in authors]

    return authors

def extract_title(page):
    """
    Extract the title from the webpage.

    Args:
        page (BeautifulSoup): Parsed HTML content of the page.

    Returns:
        list: A list containing the title of the page.
    """
    title = page.select("h1")
    title = [t.get_text().strip() for t in title]
    
    return title

def extract_pubmeta(page):
    """
    Extract publication metadata from the webpage.

    Args:
        page (BeautifulSoup): Parsed HTML content of the page.

    Returns:
        str: The publication metadata.
    """
    pub = page.select_one('#meta')
    if pub:
        pub = pub.get_text().strip()
        pub = re.split(r'\(|\)', pub)[1].strip()
    
    return pub

def extract_date(page):
    """
    Extract the publication date from the webpage.

    Args:
        page (BeautifulSoup): Parsed HTML content of the page.

    Returns:
        dict: A dictionary containing the month and year of publication.
    """
    date = page.select("div.date")
    date = [d.get_text().strip() for d in date]
    
    if date:
        date_parts = date[0].split()
        month = date_parts[0]
        year = date_parts[1]
        date = {'month': month, 'year': year}
    
    return date

def gen_cite_key(authors, year):
    """
    Generate a citation key based on the first author's name and the publication year.

    Args:
        authors (list): A list of author names.
        year (str): The publication year.

    Returns:
        str: The generated citation key.
    """
    first_author = re.split(r'and', authors[0])[0].strip().split()
    first_name = first_author[0]
    last_name = first_author[1]
    
    key = f"{last_name}_{year}"
    
    return key
    
