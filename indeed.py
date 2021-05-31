import requests
from bs4 import BeautifulSoup

# https://www.indeed.com/q-python-jobs.html
# https://www.indeed.com/jobs?as_and=python&limit=50
# https://stackoverflow.com/jobs?q=python

LIMIT = 50
INDEED_URL = f"https://www.indeed.com/jobs?as_and=python&limit={LIMIT}"

# returns: int (last page)
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


# Returning ints
def extract_indeed_pages_new():
    start = 0
    # start_int_list = [0]
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, 'html.parser')

    next_button = soup.find("a", {"aria-label":"Next"})

    while next_button:
        indeed_url_updated = f"https://www.indeed.com/jobs?q=python&limit=50&start={str(start*50)}"
        result_updated = requests.get(indeed_url_updated)
        soup_updated = BeautifulSoup(result_updated.text, 'html.parser')
        next_button = soup_updated.find("a", {"aria-label":"Next"})
        if next_button == None:
            break
        start = int(start) + 1
        # start_int_list.append(start)
        # print(f"start_int_list:{start_int_list}")
    
    return int(start) + 1


# Takes int
# Returning...?
def extract_indeed_jobs(max_page):
    # print(max_page)
    jobs = []
    for page in range (max_page):
        result = requests.get(f"{INDEED_URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, 'html.parser')
        job_cards = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})        # list of soups
        for job in job_cards:
            #title = job.find("div", {"class":"title"})
            #anchor = title.find("a")["title"]
            title = job.find("h2",{"class":"title"}).find("a")["title"]
            print(title)
    return jobs