import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import database as db
from scraper import get_data
import time
import schedule

#write the email address of the bot
e_mail=""
#write the app key of that e mail
password=""

def send_mail(product_name,url,target_price,current_price):
    title="DISCOUNT"
    message=f"""
    Hi mate,
    
    Lately the price of a product in your track list has fallen.
    
    Name: {product_name}
    Target: {target_price}
    Current: {current_price}

    Click to buy:
    {url}

    Take care!!
    AmazBot
    """

    msg = MIMEMultipart()
    msg['From']=e_mail
    #write the e mail of receiver
    msg['To']=""
    msg['Subject']=title
    msg.attach(MIMEText(message, 'plain','utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(e_mail , password)
        server.send_message(msg)
        server.quit()
        print("SUCCESS")
    except Exception as e:
        print(f"Error: {e}")

def check_prices():
    print("Checking")
    df=db.get_all_products()

    if df.empty:
        print("no product to track")
        return

    for index,row in df.iterrows():
        product_name=row['product_name']
        url=row['url']
        target_price=row['target_price']

        print(f"Checking {product_name[:30]}")

        result=get_data(url)
        if "error" not in result and result["price"] is not None:
            current_price=result["price"]
            print(f" Current: {current_price} | Target: {target_price}")

            if current_price<=target_price:
                print("HIT")
                send_mail(product_name,url,target_price,current_price)
            else:
                print("another time")
        else:
            print("error")

        time.sleep(5)
        print("-"*40)
    print("\n completed")
if __name__=="__main__":
    print("bot is set")
    check_prices()
    schedule.every().day.at("10.00").do(check_prices())
    schedule.every().day.at("20.00").do(check_prices())

    while True:
        schedule.run_pending()
        time.sleep(60)