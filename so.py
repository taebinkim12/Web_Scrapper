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


def extract_job(result):
    title = result.find("h2", {"class":"mb4"}).find("a")["title"]

    company, location = result.find("h3", {"class":"fc-black-700"}).find_all("span", recursive = 0)
    company = company.get_text().strip()
    location = location.get_text().strip()

    job_id = result["data-jobid"]
    apply_link = f"https://stackoverflow.com/jobs/{job_id}"
    # print(apply_link)
    
    return {'title': title, 
            'company': company, 
            'location': location,
            'apply_link': apply_link}
    


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"SO: Scrapping page {page + 1}")
        result = requests.get(f"{SO_URL}&pg={page + 1}")
        soup = BeautifulSoup(result.text, 'html.parser')
        results = soup.find_all("div", {"class":"-job"}) 
        for result in results:
            job = extract_job(result)
            jobs.append(job)

    return jobs



def get_all_jobs():
    last_page = extract_last_page()
    jobs = extract_jobs(last_page)
    return jobs