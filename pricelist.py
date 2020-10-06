from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

item_no = 1
#input search items like "football","shirts","badminton" etc.
searchItem = input('Enter the Product name you want to search(e.g. "football", "shirts" etc.): ') 
print("The product list along with prices is here...\n\n")
for i in range(1, 100):
    actualLink = "https://www.flipkart.com/search?page=" + str(i) + "&q=" + searchItem
    try:
        page = urlopen(actualLink)
        soup = bs(page, "lxml")
        # soup.prettify()
        allPrice = soup.find_all(class_="_1vC4OE")
        allModelName = soup.find_all(class_="_2cLu-l")
        no_of_items = min(len(allModelName), len(allPrice))   
        if(no_of_items == 0):
            print("No more results found...")
            break
        print(len(allModelName), len(allPrice))
        for j in range(no_of_items):
            print(f"{item_no} . {allModelName[j].get_text()} :: {allPrice[j].get_text()}")
            item_no += 1
    except:
        print("No more results found...")
        break

