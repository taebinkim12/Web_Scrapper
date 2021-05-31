# from Web_Scrapper.indeed import indeed_extract_page_by_nico, indeed_extract_page_new
import requests
from bs4 import BeautifulSoup
from indeed import extract_indeed_pages_new, extract_indeed_jobs

# max_indeed_pages = indeed_extract_page_by_nico()

# extract_indeed_jobs(max_indeed_pages)

max_indeed_pages_new = extract_indeed_pages_new()

extract_indeed_jobs(max_indeed_pages_new)
