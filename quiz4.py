import requests
from bs4 import BeautifulSoup 

file = open('books.csv', 'w', encoding='utf-8_sig')
headings = 'წიგნის ავტორი,წიგნის სახელი\n'
file.write(headings)

#გამოვიყენე წიგნების საიტი, sulakauri.ge
url = 'https://www.sulakauri.ge/wignebi/?swoof=1&fbclid=IwAR2ZxeUjKXhDpmp-PZknFVRgQ_moic7d749fkKCVGGoKv4kkFafm5ImdGU8&paged=1'
for i in range(1,6):
	r = requests.get(url + str(i))
	#აღწერს გვერდის ნომერს
	print("Page - ",str(i))

	data = r.text
	soup = BeautifulSoup(data,"html.parser")

	main_table = soup.find('div',{"class":"mkdf-pl-main-holder"})
	for item in main_table:
	    book_info = main_table.find_all('div',{"class":"mkdf-pl-text-wrapper"})
	    for i in book_info:
	        author = i.find("div",{"class":"mkdf-pl-author-holder"}).text
	        book_name = i.find("h5",{"class":"mkdf-product-list-title"}).find("a").text
	        
	        print(author + " - " + book_name  )

file.write(book_info+','+author+','+book_name+','+main_table+'\n')


