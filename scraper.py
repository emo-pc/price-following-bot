from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import time


def get_data(url):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    driver=webdriver.Chrome(options=options)

    try:
        if "?" in url:
            url = url.split("?")[0]

        driver.get(url)
        time.sleep(3)
        soup=BeautifulSoup(driver.page_source,"html.parser")
        title_el=soup.find(id="productTitle")
        title=title_el.text.strip() if title_el else "no title"

        price_el=soup.find("span",class_="a-price-whole")
        fraction_el=soup.find("span",class_="a-price*fraction")

        if price_el:
            price=price_el.text.strip().replace(".","").replace(",","")

            if fraction_el:
                price+="."+fraction_el.text.strip()

            return {"title":title,"price":float(price)}
        else:
            return {"title":title,"price":None,"error":"couldn't find the price"}
    except Exception as e:
        return {"error":f"something went wrong:{str(e)}"}
    finally:
        driver.quit()

#######
##test_url="https://amzn.eu/d/04QlQjuP"
##print("processing")
##result=get_data(test_url)
##print("###############")
##print(result)