import requests
from bs4 import BeautifulSoup
from indeed import get_jobs as indeed_get_jobs

# https://www.indeed.com/q-python-jobs.html
# https://www.indeed.com/jobs?as_and=python&limit=50
# https://stackoverflow.com/jobs?q=python

indeed_jobs = indeed_get_jobs()
