import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
from datetime import datetime

def get_meta_data(pubs):
    """
    Scrapes publication meta data from the ERS website

    Args:
        pubs (int,string,or list): can be a single 6 digit publication id, a url string, or list 
        of multiple ids/urls that represent the publications to pull meta data for
 
    Returns:
        Pandas data frame: a data frame with each row representing a different publication and
         each column corresponding to a piece of meta data 
    
    Examples:
        #>>> get_meta_data(110765)
        #>>> get_meta_data("https://www.ers.usda.gov/publications/pub-details?pubid=110765")
        #>>> get_meta_data([110765,110767])
    """
    # if the pubs argument was entered as a single character string, 
    # or numeric value for publication id, convert it to a list with a single element.
    if isinstance(pubs, str) or isinstance(pubs, int):
        pubs = [pubs]

    # initialize a dictionary to store meta data for each pubs
    meta_data = {}

    # loop over each pubs and get the meta data
    for i in pubs:
    
        # if the pubs is a integer representing a publication id, 
        # add the base pubs to it
        if isinstance(i, int):
            i = "https://www.ers.usda.gov/publications/pub-details?pubid=" + str(i)

        # get the pubs
        response = requests.get(i)

        # get report number, which isn't listed with the other meta data
        report_no = BeautifulSoup(response.content, 'html.parser').find("li", class_="usa-collection__meta-item usa-tag").contents[0]

        # locate the json string with all the publication meta data
        json_data = BeautifulSoup(response.content, 'html.parser').find("script", type="application/json").contents[0]

        # convert the json string to a dictionary
        dict = json.loads(json_data)

        # select the data layer
        dataLayer = dict['dataLayer']['page']

        # get the publication id to label the dictionary entry
        pub_id = dataLayer["pubId"]

        # for dictionary entries that have multiple elements, 
        # make sure they are lists so that they are contained 
        # in a single data frame cell later
        dataLayer['authors'] = [dataLayer['authors']]
        dataLayer['breadcrumbs'] = [dataLayer['breadcrumbs']]

        # add the report number to the dataLayer
        dataLayer['report_no'] = report_no

        # add data layers to the meta data dictionary
        meta_data[pub_id] = pd.DataFrame(dataLayer)

    # concat the meta data dictionary into a data frame
    meta_data = pd.concat(meta_data)

    # return a data frame with publication meta data for each pubs
    return(meta_data)

def gen_cite_key(authors, date):
  
    # convert date string to a datetime object
    date = datetime.strptime(date, "%Y-%m-%d")

    # isolate the year
    year = date.year

    # extract the first author from the list of authors
    first_author = authors[0].split(" ")

    # create a citation key using the last name of the first authro
    # and year of publication
    key = first_author[len(first_author)-1] + "_" + str(year)

    return(key)

def cite_ers(pubs):

    meta_data = get_meta_data(pubs)

    for i in range(0,len(meta_data)):
        pub_meta_data = meta_data.iloc[i]

        # isolate each piece of meta data and get it into the 
        # approirate form for entering into a bibtex entry
        authors = " AND ".join(pub_meta_data['authors'])
        title = pub_meta_data['title']
        date = datetime.strptime(pub_meta_data['date'], "%Y-%m-%d")
        pub_type_short = pub_meta_data['series']
        pub_type_long = pub_meta_data['siteSectionSecondLevel'].replace("Publications:", "").strip()
        cite_key = gen_cite_key(pub_meta_data['authors'], pub_meta_data['date'])
        pub_url = "https://www.ers.usda.gov/publications/pub-details?pubid=" + str(pub_meta_data['pubId'])
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


