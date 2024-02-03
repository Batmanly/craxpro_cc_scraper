# Craxpro.io - CC Scraper   
# This is a simple web scraper that scrapes the craxpro.io website for the latest credit card dumps.

# How To Use:

1. First choose browser that you want to run(Chrome or Edge, I prefer Edge because i can't use the browser while it's scraping)

2. In code you may need to change default profile which you want to run while scraping, if you want auto login you also need to add your credentials (if you are already logged auto login will be skipped). 
    ```python
    options.add_argument("user-data-dir=C:\\Users\\***YOUR_USERNAME***\\AppData\\Local\\Google\\Chrome\\User Data")
    options.add_argument('profile-directory=Profile 4')
    ```

    ```python
        username.send_keys('***') # change *** with your username
        password.send_keys('****') # change *** with your password
    ```

3. Open Edge before run , and pass the cloudflare protection , no need to login or anything just pass the protection.

4. Run the script and wait for the results. (python3 edge.py $page_number)
    
        Example: 
        ```python
        python3 edge.py 1```
        (This will scrape the one page in area where cc sharing of the website and save the results in the cc.txt file.)

5. The results will be in the cc.txt file.



# Requirements:
- Python 3
- Selenium (pip install selenium)
- Edge or Chrome browser
- Edge or Chrome webdriver


# Note:
- if you get error while running , check if edge is running in background or not, if it's running close it and run the script again.