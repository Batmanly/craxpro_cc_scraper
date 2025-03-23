# Craxpro.io - CC Scraper   
# This is a simple web scraper that scrapes the craxpro.io website for the latest credit card dumps.

# How To Use:

1. Export [Cookie Editor extension](https://chromewebstore.google.com/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm?hl=en-US&utm_source=ext_sidebar) as "Header String" than save it in a file called .env

2. Run the script and wait for the results. 
    
        Example: 
        ```python
        python3 main.py 1```
        (This will scrape the one page in area where cc sharing of the website and save the results in the cc.txt file.)

3. The results will be in the cc.txt file.

# Requirements:
- Python 3
- pip3 install -r requirements.txt