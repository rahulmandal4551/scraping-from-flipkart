from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
k=1
searchItem=input("Enter the Product name you want to search(e.g. "football", "shirts" etc.): ")    #input search items like "football","shirts","badminton" etc.
print("The product list along with prices is here...\n\n")
for i in range(1,58):
	actualLink = ("https://www.flipkart.com/search?page="+str(i)+"&q="+searchItem)
	try:
		page=urlopen(actualLink)
	except:
		print("Internet Connection Error...")
	soup=bs(page,"lxml")
  #print(soup.prettify())
	soup.prettify()
	allPrice=soup.find_all(class_="_1vC4OE")
	allModelName=soup.find_all(class_="_2cLu-l")
	for j in range(40):
		print((k),". ",allModelName[j].get_text(),"::",allPrice[j].get_text())
		k+=1
