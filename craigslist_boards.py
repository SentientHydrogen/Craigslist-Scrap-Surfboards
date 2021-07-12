

from os import error
import bs4

from urllib.request import urlopen as uReq

from bs4 import BeautifulSoup as soup

my_url= 'https://providence.craigslist.org/d/for-sale/search/sss?query=surfboard&sort=rel'

print(my_url)

uClient = uReq(my_url)

page_html = uClient.read()

uClient.close()

page_soup = soup(page_html, "html.parser")

print(page_soup.h1)

#this is grabbing each result for the search
containers = page_soup.findAll("li", {"class":"result-row"})

# print(len(containers))

# print(containers[0])

print(len(containers))

x =0
container = containers[x] #issue here for some reason

print(containers[0])

# print(container)

# print(container.a)

# print(container.h3.a.text)

# #post title
# board_title = container.div.h3.a.text #the html line within the .div.h3.a line contains straight text for the price. '.text' is how you ref that

# print(board_title.strip())

# #post date

# board_post_date = container.div.time["datetime"]
# print(board_post_date)

# #board price
# board_price = container.a.text

# print(board_price.strip())

# #boardLocations
# board_location_line = container.find('span', class_= 'result-hood')
# board_location = board_location_line.text
# print(board_location)

# #boardURL
# board_URLLine = container.find('h3', class_='result-heading')

# board_URL = board_URLLine.a["href"]

# print(board_URL)


# print(board_location)
#grabbing each product
filename = "Surfboards.csv"

f = open(filename, "w")

headers = "board_title, board_price, board_location, board_URL\n"

f.write(headers)


for contianer in containers:
    
    if container.div.h3.a.text is not None:
        preboard_title = container.div.h3.a.text
        board_title = preboard_title.strip()
    
    if container.div.time["datetime"] is not None:
        board_post_date = container.div.time["datetime"]
    
    if container.a.text is not None:
        preboard_price = container.a.text
        board_price = preboard_price.strip()
    

    if container.find('span', class_= 'result-hood') is not None:
        board_location_line = container.find('span', class_= 'result-hood')
        if board_location_line.text is not None:
            preboard_location = board_location_line.text
            board_location = preboard_location.strip()
    
    board_URLLine = container.find('h3', class_='result-heading')
    if board_URLLine.a["href"] is not None:
        preboard_URL = board_URLLine.a["href"]
        board_URL = preboard_URL.strip()
    
    print("NAME: " + board_title)
    print("PRICE: " + board_price)
    print("LOCATION: " +board_location)
    print("URL Link: " + board_URL)
    
    f.write(board_title.replace(",", "|") + "," + board_price.replace(",", "|") + "," + board_location.replace(",", "|") + "," + board_URL.replace(",", "|") +"\n")
    x = x+1
    if x<len(containers):
        container = containers[x]
    elif x>=len(containers):
        print("End Loop")

f.close()



# edit for the git tutorial test

# editing this again
#more changes and deleted the import language at the end











