# step 0 : installation some requirements
# pip install requests
# pip install bs4 means beautifulsoup4
# pip install html5lib
# pip install urllib3



import requests
from bs4 import BeautifulSoup

# step1 : get the html
url = "https://www.cam.ac.uk/"



# request will get all the html of this url
r = requests.get(url)
htmlContent = r.content
# print(htmlContent)


# step2 : parse the html in beautifulsoup
from urllib.parse import urlparse

soup = BeautifulSoup(htmlContent, 'html.parser')
links = soup.find_all('a')

# for link in links:
#     url = link['href']
#     parsed_url = urlparse(url)
#     domain_name = parsed_url.netloc
#     print(domain_name)






# # Find all `img` tags in the document
# img_tags = soup.find_all('img')
# # print(img_tags)
# # Iterate over the `img` tags and look for the logo
# for img in img_tags:
#     # Check if the `src` attribute of the `img` tag contains the URL of the logo
#     if 'cambridge_university2.svg' in img['src']:
#         # Print the `src` attribute of the `img` tag to get the URL of the logo
#         print(img['src'])
#
#
#


vision_element = soup.find('div', {'class': 'vision'})
# print(vision_element)
# Extract the text of the vision element
# vision_text = vision_element.text
#
# # Print the text of the vision statement
# print(vision_text)

# str = soup.get_text()
# print(str[0:str.find("vision")+12])
# print(str.find("vision"))
# if "vision" in str:
#     print("yes ")



a_tags = soup.find_all('a')

# Iterate over the `a` tags and look for the "About Us" link
for a in a_tags:
    # Check if the `a` tag has a `href` attribute that contains the URL of the "About Us" page
    if 'about-us' in a['href']:
        # Print the `href` attribute of the `a` tag to get the URL of the "About Us" page
        print(a['href'])



soup = BeautifulSoup(htmlContent,"html.parser")
# print(soup.prettify)
# step3 : Html Tree Traversal

# now we can scrap all the things in this website with this soup


title = soup.title

# some objects which we need to learn :
# 1. Tag
# print(type(title))  #<class 'bs4.element.Tag'>


# 2. NavigableString
# print(type(title.string)) #<class 'bs4.element.NavigableString'>

# 3. BeautifulSoup
# print(type(soup)) #<class 'bs4.BeautifulSoup'>


# for all acnhor tags
anchor = soup.find_all("p")
# print(anchor)
# for i in anchor:
#     str =  i.string
#     if str == "about us":
#         print(str)

paragraph_tag = soup.find_all("p")
# print(paragraph_tag)


# to get first element of the html page and .string se we can take the string inside anchor tag
first_anchor = soup.find("a").string
first_anchor_class = soup.find("a")['class'] #all class will show of this anchor tag
# print(first_anchor)
# print(first_anchor_class)


first_para = soup.find("p")
# print(first_para)



# find all the element with a specific class and id

all_field = soup.find_all('div',class_='field-items')


# so we find all the img tags with this class and link of all images and src also
# for i in all_field:
#     imgtag = i.find_all("img")
#     for imgdata in imgtag:
#         print(imgdata['alt'],imgdata['src'])
#


alldiv = soup.find_all("div")
# print(alldiv)

# for divs in alldiv:
    # all_text = divs.get_text()
    # if "about" in all_text:
    #     print(all_text)

# all text of this site
# print(soup.get_text())


# now we use the id of element and get content and children of that particular elements

# elements = soup.find(id = "graduate")
#
# somelem = elements.next_element.next_element
# print(somelem.contents)







# print(elements.contents)
# for element in elements.contents:
#     ab = element.find('a')







    # if element.get_text() == "Courses":
    #     print(element)





