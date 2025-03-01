#%%
import requests
from bs4 import BeautifulSoup
import pandas as pd
import json
from datetime import datetime

class Publication:
    """
    A class to represent a publication and generate citations for it.
    Attributes
    ----------
    pubs : list
        A list of publication URLs or IDs.
    meta_data : dict
        A dictionary to store metadata of publications.

    Methods
    -------
    fetch_meta_data():
        Fetches metadata for each publication and stores it in a DataFrame.
    gen_cite_key(authors, date):
        Generates a citation key based on the first author's last name and the publication year.
    generate_citation():
        Generates and prints BibTeX citations for the publications.
    """
        
    def __init__(self, pubs):
        """
        Initializes the instance with a list of publications.
        Args:
            pubs (str, int, or list): A single publication (as a string or integer) 
                                      or a list of publications.
        Attributes:
            pubs (list): A list of publications.
            meta_data (dict): A dictionary to store metadata related to the publications.
        """

        if isinstance(pubs, str) or isinstance(pubs, int):
            self.pubs = [pubs]
        else:
            self.pubs = pubs
        self.meta_data = {}

        for i in self.pubs:
            if isinstance(i, int):
                i = f"https://www.ers.usda.gov/publications/pub-details?pubid={i}"

            response = requests.get(i)
            report_no = BeautifulSoup(response.content, 'html.parser').find("li", class_="usa-collection__meta-item usa-tag").contents[0]
            json_data = BeautifulSoup(response.content, 'html.parser').find("script", type="application/json").contents[0]
            data_dict = json.loads(json_data)
            data_layer = data_dict['dataLayer']['page']
            pub_id = data_layer["pubId"]
            data_layer['authors'] = [data_layer['authors']]
            data_layer['breadcrumbs'] = [data_layer['breadcrumbs']]
            data_layer['report_no'] = report_no
            self.meta_data[pub_id] = pd.DataFrame(data_layer)

        self.meta_data = pd.concat(self.meta_data)

    @staticmethod
    def gen_cite_key(authors, date):
        """
        Generates a citation key based on the first author's last name and the year of publication.
        Args:
            authors (list of str): A list of author names, where each name is a string.
            date (str): The publication date in the format 'YYYY-MM-DD'.
        Returns:
            str: A citation key in the format 'LastName_Year'.
        """

        date = datetime.strptime(date, "%Y-%m-%d")
        year = date.year
        first_author = authors[0].split(" ")
        key = first_author[-1] + "_" + str(year)
        return key

    def generate_citation(self):
        """
        Generates BibTeX citations for each publication in the metadata.
        This method fetches metadata for publications, processes each publication's
        metadata to create a BibTeX citation, and prints the citation.

        """
        
        for i in range(len(self.meta_data)):
            pub_meta_data = self.meta_data.iloc[i]
            authors = " AND ".join(pub_meta_data['authors'])
            title = pub_meta_data['title']
            date = datetime.strptime(pub_meta_data['date'], "%Y-%m-%d")
            pub_type_long = pub_meta_data['siteSectionSecondLevel'].replace("Publications:", "").strip()
            cite_key = self.gen_cite_key(pub_meta_data['authors'], pub_meta_data['date'])
            pub_url = f"https://www.ers.usda.gov/publications/pub-details?pubid={pub_meta_data['pubId']}"
            report_no = pub_meta_data["report_no"]

            bibtex = (
                f"@misc{{{cite_key},\n"
                f"author = {{{authors}}},\n"
                f"title = {{{title}}},\n"
                f"publisher = {{U.S. Department of Agriculture, Economic Research Service}},\n"
                f"howpublished = {{{pub_type_long}}},\n"
                f"year = {{{date.year}}},\n"
                f"month = {{{date.month}}},\n"
                f"number = {{{report_no}}},\n"
                f"url = {{{pub_url}}}\n"
                f"}}"
            )

            print(bibtex.strip('"\''))



