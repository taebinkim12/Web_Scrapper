import requests
from bs4 import BeautifulSoup

LIMIT = 50
INDEED_URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"

# returns: int (last page)      
# --> This does not work anymore as indeed's webpage structure(pagination) is slightly adjusted
def indeed_extract_page_by_nico():
    result = requests.get(INDEED_URL)
    # print(indeed_testing.text)                                                --> getting the HTML information

    # soup      --> Data Extracter

    soup = BeautifulSoup(result.text, "html.parser")                            # A soup to extract HTML from a link to website
    pagination = soup.find("div", {"class": "pagination"})                      # Another soup that finds "div, class 'pagination'"
    links = pagination.find_all('a')                                            # Another soup to find the "hyperlink" in that div

    pages = []

    for link in links[:-1]:
        pages.append(int(link.find("span").string))                             # Soup and use it to find a "span" inside a link (inside <a>)   (span is like another header inside HTML file)

    max_page = pages[-1]                                                        # Last page!!
    return max_page


# Returning int (the number of pages)
def extract_pages_new():
    start = 0
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, 'html.parser')                            # A soup to extract HTML from website

    next_button = soup.find("a", {"aria-label":"Next"})                 

    while next_button:
        indeed_url_updated = f"https://www.indeed.com/jobs?q=python&limit=50&start={str(start*50)}"
        result_updated = requests.get(indeed_url_updated)
        soup_updated = BeautifulSoup(result_updated.text, 'html.parser')
        next_button = soup_updated.find("a", {"aria-label":"Next"})
        if next_button == None:
            break
        start = int(start) + 1
    
    return int(start) + 1


# takes html(soup named 'job_card')
# Retruns a dictionary (with title, company name, location, and Job_id on indeed)
def extract_job(job_card):
    title = job_card.find("h2",{"class":"title"}).find("a")["title"]
    
    company = job_card.find("span", {"class": "company"})
    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else :
            company = str(company.string)
            company = company.strip()
    else :
        company = None
    
    location = job_card.find("div", {"class": "recJobLoc"})["data-rc-loc"]

    job_id = job_card["data-jk"]                                                # [] for finding an attribute in "div" in html

    return {'title': title, 
            'company': company, 
            'location': location, 
            'apply_link': f"https://www.indeed.com/viewjob?&jk={job_id}&from=web&vjs=3"}
            

# Takes int
# Returns array (of all jobs)
def extract_jobs(max_page):
    jobs = []
    for page in range (max_page):
        print(f"id: Scrapping page {page + 1}")
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        job_cards = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})        # list of soups
        for job_card in job_cards:
            job = extract_job(job_card)
            jobs.append(job)
    return jobs


# Wrapper Function
def get_all_jobs():
    max_page = extract_pages_new()
    indeed_jobs = extract_jobs(max_page)
    return indeed_jobs
