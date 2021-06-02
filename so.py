import requests
from bs4 import BeautifulSoup
from requests.api import request

SO_URL = "https://stackoverflow.com/jobs?q=python"


# returns int
def extract_last_page():
    result = requests.get(SO_URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    pagination = soup.find("div", {"class": "s-pagination"})
    pages = pagination.find_all("a")
    pages = pages[-2]
    last_page = pages.get_text().strip()
    return int(last_page)


def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        result = requests.get(f"{SO_URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class":"-job"}) 
        for result in results:
            print(result["data-jobid"])

        

    return jobs



def get_all_jobs():
    last_page = extract_last_page()
    jobs = extract_jobs(last_page)
    return jobs