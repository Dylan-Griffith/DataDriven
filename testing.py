from bs4 import BeautifulSoup
import urllib.request

location = ''
distance = ''
model = ''
postal = ''


class CraiglistScraper:
    def __init__(self, location, postal, max_price, radius, make, model, year):
        self.location = location
        self.postal = postal
        self.max_price = max_price
        self.radius = radius
        self.make = make
        self.model = model
        self.year = year

        self.test_url = 'https://sfbay.craigslist.org/search/cta?search_distance=5&postal=94201&auto_make_model=honda+accord'
        self.url = '''https://{location}.craigslist.org/search/cta?query={make}+{model}+{year}&search_distance={radius}
        &postal={postal}&auto_make_model={make}+{model}'''.format(location=self.location,
                                                                  make=self.make,
                                                                  model=self.model,
                                                                  postal=self.postal,
                                                                  radius=self.radius,
                                                                  year=self.year)
        self.url_lst = []
        self.car_details = {}

    def find_all_posts(self):
        # gets link for every post and populates url_lst
        html_page = urllib.request.urlopen(self.test_url)
        soup = BeautifulSoup(html_page, "html.parser")

        for post in soup.findAll("a", {"class": "result-title hdrlnk"}):
            if 'Honda Accord EX' in post.text:
                self.url_lst.append(post['href'])
                print('URL ADDED')
                print(post.text)

    def car_details(self, url):
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")

        for link in soup.findAll("p", {"class": "attrgroup"}):
            title = link.b
            print('TITLE: ', title.text)
            break

        for link in soup.findAll("section", {"id": "postingbody"}):
            des = link.text
            print(link.text)

        for link in soup.findAll("p", {"class": "attrgroup"}):
            attr = link.text
            print(attr)

        return title, des, attr


url = 'https://sfbay.craigslist.org/search/cta?search_distance=5&postal=94201&auto_make_model=honda+accord'

url_list = []
good_url = []
html_page = urllib.request.urlopen(url)
soup = BeautifulSoup(html_page, "html.parser")

# gets link for every post
# for link in soup.findAll("a", {"class": "result-title hdrlnk"}):
#     print(link["href"])
#     url_list.append(link["href"])

# Gets name of every post and adds url if name matches search params
# for post in soup.findAll("a", {"class": "result-title hdrlnk"}):
#     if 'Honda Accord EX' in post.text:
#         good_url.append(post['href'])
#         print('URL ADDED')
#         print(post.text)


car_url = 'https://sfbay.craigslist.org/sby/ctd/d/san-jose-2010-honda-accord-ex-1-owner/6899677463.html'
html_page = urllib.request.urlopen(car_url)
soup = BeautifulSoup(html_page, "html.parser")

# gets posting description
# for link in soup.findAll("section", {"id": "postingbody"}):
#     des = link.text.split('\n\n')
#     print(link.text)

# gets all attr for posting
t = []
for link in soup.findAll("p", {"class": "attrgroup"}):
    attr = link.text
    t.append(attr)
    print(attr)

# get car title
# for link in soup.findAll("p", {"class": "attrgroup"}):
#     title = link.b
#     print('TITLE: ', title.text)
#     break
print(t[1])


