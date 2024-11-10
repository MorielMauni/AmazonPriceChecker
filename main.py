# ================================== IMPORTS ================================== #
import requests
from bs4 import BeautifulSoup
import smtplib

# ================================== REQUESTS ================================== #

URL = <Any Amazon Link>
header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-GB,de;q=0.8,fr;q=0.6,en;q=0.4,ja;q=0.2",
    "Dnt": "1",
    "Priority": "u=1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Gpc": "1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0",
}

response = requests.get(url=URL, headers=header)
response.raise_for_status()
webpage = response.text
# ================================== SCRAPING ================================== #

soup = BeautifulSoup(webpage, "html.parser")
# Find the HTML element that contains the price
price = soup.find(class_="a-offscreen").get_text()

# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)

# ================================== MAIL ================================== #
mail = <YOUR MAIL>
passwd = <YOUR PASSWORD> # it's the 'app password' from password given by gmail

if price_as_float < 100:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls() # Encrypte on fly
        connection.login(user=mail, password=passwd) # Log in intothe mail
        connection.sendmail(from_addr=mail,
                            to_addrs=mail,
                            msg=f"Subject:Price is Down!\n\nThe price in ${price_as_float}")
