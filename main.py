import requests
from bs4 import BeautifulSoup
from indeed import extract_indeed_pages_new, extract_indeed_jobs

max_indeed_pages_new = extract_indeed_pages_new()

indeed_jobs = extract_indeed_jobs(max_indeed_pages_new)
