# All credits to Data Science Dojo from Youtube (https://www.youtube.com/watch?v=XQgXKtPSzUI&t=13s&ab_channel=DataScienceDojo)

# This is a web scraper for NewEgg Graphics card and is done as a practice for fun

# Done on: 16/08/2021


from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as  uReq

# URL that we are scraping
my_Url = 'https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38'

# Connecting to the URL
u_Client= uReq(my_Url)

# Download the webpage
page_html = u_Client.read()

# Once download, close the connection
u_Client.close()

# parsing the HTML
page_soup = soup(page_html, "html.parser")

# grabs each product, in this case is the graphics card in newegg
containers = page_soup.findAll("div",{"class":"item-container"})

for container in containers:
  # Extracting the name of Graphic Card
  name_of_Gcard = container.findAll("a",{"class":"item-title"})
  product_name = name_of_Gcard[0].text

  # Extracting the Out Of Stock information
  is_it_OOS = container.findAll("p",{"class":"item-promo"})
  OOS= is_it_OOS[0].text

  # Extacting the price. As some of the price contains an a tag which indicate an example like "2 Offers", we need to trim it and check if price is empty as well
  a_tag = container.findAll("a",{"class":"price-current-num"},href=True)
  if a_tag:
    for a in container.findAll("a",{"class":"price-current-num"},href=True):
      a.extract()
  else:
    price = container.findAll("li",{"class":"price-current"})
    price_checker = price[0].text
    if not price_checker:
      gcP = "Price field is empty"
    else: 
      gcP = price_checker.strip()[:-2]
    
    # Extract shipping fee
    ship = container.findAll("li",{"class":"price-ship"})
    ship_checker = ship[0].text
    if not ship_checker:
      ship_checker = "Shipping field is empty"
    shipping = ship_checker



  print("Product Name: " + product_name)
  print("OFS: " + OOS)
  print("GCP: " + gcP)
  print("Shipping: " + shipping)
