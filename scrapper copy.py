import requests
from bs4 import BeautifulSoup
import smtplib

url = 'https://www.amazon.in/Fortune-Sunlite-Refined-Sunflower-Oil/dp/B00NYZTGEO/ref=sr_1_10_mod_primary_alm?almBrandId=ctnow&dchild=1&fpw=alm&keywords=fortune&qid=1606218074&sbo=m6DjfpMzMLDmL8pSMKX8hw%3D%3D&sr=8-10'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36'}


def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    print(title.strip())
    print(price)


    converted_price = float(price[2:8])

    

    if(converted_price > 120.00):
        send_mail()



def send_mail():
     server = smtplib.SMTP('smtp.gmail.com', 587)
     server.ehlo()
     server.starttls()
     server.ehlo()

     server.login('tanx793@gmail.com', 'wtfnyccokxnfwjfk')

     subject = 'Price fell down!'
     body = 'buy it https://www.amazon.in/Fortune-Sunlite-Refined-Sunflower-Oil/dp/B00NYZTGEO/ref=sr_1_10_mod_primary_alm?almBrandId=ctnow&dchild=1&fpw=alm&keywords=fortune&qid=1606218074&sbo=m6DjfpMzMLDmL8pSMKX8hw%3D%3D&sr=8-10'



     msg = f"Subject: {subject}\n\n\n{body}"

     server.sendmail(
         'tanx739@gmail.com',
         'tdmorakhia26@gmail.com',
         msg
     )

     print('EMAIL SEND!')

     server.quit()

check_price()














    