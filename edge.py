import re
import os
import sys
from selenium.webdriver.common.by import By
from selenium.webdriver import Edge,EdgeOptions



import time
start = time.time()

options = EdgeOptions()

# close edge if it's running
os.system("taskkill /f /im msedge.exe")

# use edge profile
options.add_argument('--user-data-dir=C:\\Users\\Batmanly\\AppData\\Local\\Microsoft\\Edge\\User Data')
options.add_argument('--profile-directory=Default')

#Make faster chrome
#options.add_argument("start-maximized")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_experimental_option('useAutomationExtension', False)
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument('disable-cache')
options.add_argument('-ignore-certificate-errors')
options.add_argument('-ignore -ssl-errors')
# options.add_argument('--headless')

driver = Edge(options=options)

links = set()
cc_list = set()

if len(sys.argv) < 2:
    back = 1
else:
    back = int(sys.argv[1])


# open and login , if not loged in
def open_and_login(driver):
    driver.get('https://craxpro.io/threads/live-cc-working.623085/')
    page_content = driver.page_source

    if 'To view the content, you need to ' in page_content:
        driver.get('https://craxpro.io/login/')
        username = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/form/div[1]/div/dl[1]/dd/input')
        password = driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/form/div[1]/div/dl[2]/dd/div/div/input')
        username.send_keys('****')
        password.send_keys('*****')
        driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[2]/div[3]/div[2]/div/div/form/div[1]/dl/dd/div/div[2]/button/span').click()


# collect links from pages.
def scrape_links(back):
    for i in range(back):
        driver.get(
            f'https://craxpro.io/forums/freebie.73/page-{i + 1}'
        )
        elements = driver.find_elements(By.TAG_NAME, 'a')
        
        # print all links
        # for element in elements:
        #     print(element.get_attribute('href'))

        # don't add this links
        dont_add = [
            'https://crax.shop/',
        ]

        # check if link is valid
        for element in elements:
            href = element.get_attribute('href')
            if 'https://craxpro.io/threads/' not in str(href):
                continue
            elif str(href) in dont_add:
                continue
            elif '/lates' in str(href):
                continue
            elif '/unread' in str(href):
                continue
            elif '/show' in str(href):
                continue
            else:
                links.add(element.get_attribute('href'))
        # print all links
        # for i in links:
        #     print(i)

def open_web_page(url):
    try:
        driver.get(url)
        
        # before close page get cc
        get_source = driver.page_source
        # get credit card from source

        #matches = re.findall(r'(\d{16})\|(\d{2})\|(\d{4})\|(\d{3})', get_source)
        regex1 = re.findall(r'(\d{16})\|(\d{2})\|(\d{4})\|(\d{3})', get_source) # [('4201996000195279', '01', '2026', '667')]
        regex2 = re.findall(r'\d{4}\d{4}\d{4}\d{4}', get_source) # ['4201996000195279']
        # if regex2 is already in regex1, delete regex2, because regex1 is more accurate
        try:
            for i in range(len(regex2)):
                if regex2[i] in regex1[i]:
                    regex2.remove(regex2[i])
        except:
            pass

        try:
            for match in regex1:
                cc_info = '|'.join(match)
                #add cc list
                cc_list.add(cc_info)
                print(f"Credit Card Info: {cc_info} from {url}")

            for match in regex2:
                cc_info = match
                #add cc list
                cc_list.add(cc_info)
                print(f"Credit Card Info: {cc_info} from {url}")
        except:
            pass
    except:
        pass


        

open_and_login(driver)
scrape_links(back)
link_list = list(links)
# print(link_list)

for i in link_list:
   open_web_page(i)

driver.quit()

# write all cc to file
cc_list = list(cc_list)
with open('cc.txt', 'w') as f:
    for i in cc_list:
        f.write(i + '\n')

print(str(len(links)) + ' links found')
print(str(len(cc_list)) + ' credit cards found')
end = time.time()
print("The time of execution of above program is :", end-start)