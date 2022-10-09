from bs4 import BeautifulSoup


# TRYING OUT BEAUTIFUL SOUP
# with open("./day45_web_scraping/website.html", encoding="utf8") as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, "html.parser")
# #print(soup.title.string)

# # this will give you only the first para - use FIND_ALL!!
# #print(soup.p)

# # find all tags
# all_anchor_tags = soup.find_all("a")

# #retrieve tag info
# for tag in all_anchor_tags:
#     pass
#     #print(tag.getText())
#     #print(tag.get("href"))

# # soup has read in the entire webpage, you can print it (and indent it properly with prettify)
# #print(soup.prettify())

# # find specific ID or class
# #heading = soup.find(name="h1", id="name")
# #print(heading)

# #use css selectors to find elements
# #find the first a inside a the first p 
# company_url = soup.select_one(selector="p a")
# print(company_url)
