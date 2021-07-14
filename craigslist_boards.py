

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

# print(containers[0])

# print(container)

# print(container.a)

# print(container.h3.a.text)


# board_title = container.div.h3.a.text #the html line within the .div.h3.a line contains straight text for the price. '.text' is how you ref that

# print(board_title.strip())


#Board range capture. to ensure the surfboard range stays in the RI area:

result_range_container = page_soup.find("div", {"class":"search-legend"})

print(result_range_container)

result_range_line = result_range_container.find("span", {"class":"totalcount"})

result_range = result_range_line.text

print(result_range)


# print(board_location)
# grabbing each product
filename = "Surfboards.csv"

f = open(filename, "w")

headers = "board_title, board_price, board_location, board_URL\n"

f.write(headers)


for contianer in containers[0:int(result_range)]:
    
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
    if x<=int(result_range):
        container = containers[x]
    elif x>int(result_range):
        print("End Loop")

f.close()


#IMAGE SCRAPPING:
#tryin to see if i can grab the images for the listsings:

# board_image_url = 'https://images.craigslist.org/{board_img_data_ids}_300x300.jpg'

# # soup_img = soup(r.content, 'lxml')

# board_img_data_ids = container.a["data-ids"]

# board_img = container.a.img['src'] # saying that his is a Nonetype

# print(board_img)

# print(board_img_data_ids) #the dataids are the only thing that changes for the image url.

















