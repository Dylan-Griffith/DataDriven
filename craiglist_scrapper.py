from bs4 import BeautifulSoup
import urllib.request


class CraiglistScraper:
    def __init__(self, location, postal, radius, make, model, year):
        self.location = location
        self.postal = postal
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
        self.make_model = self.make + ' ' + self.model

    def find_all_posts(self):
        # gets link for every post and populates url_lst
        html_page = urllib.request.urlopen(self.url)
        soup = BeautifulSoup(html_page, "html.parser")

        for post in soup.findAll("a", {"class": "result-title hdrlnk"}):
            if self.make_model in post.text:
                self.url_lst.append(post['href'])
                # print('URL ADDED')
                # print(post.text)

    def car_details(self, url):
        html_page = urllib.request.urlopen(url)
        soup = BeautifulSoup(html_page, "html.parser")

        for link in soup.findAll("p", {"class": "attrgroup"}):
            title = link.b.text
            print('TITLE: ', title)
            break

        for link in soup.findAll("section", {"id": "postingbody"}):
            des = link.text
            des = des[28:]
            print('DESCRIPTION: ', des)

        car_attr = []
        for link in soup.findAll("p", {"class": "attrgroup"}):
            attr = link.text
            car_attr.append(attr)
            # print('ATTRS: ', attr)
        print('ATTR: ', car_attr[1])
        attr = car_attr[1]

        return title, des, attr

location = 'sfbay'
distance = '5'
postal = '94201'
radius = '5'
model = 'Accord'
make = 'Honda'
year = '2010'

details = {}
scapper = CraiglistScraper(location, postal, radius, make, model, year)
scapper.find_all_posts()
for link in scapper.url_lst[:2]:
    print(link)
    title, des, attr = scapper.car_details(link)
    print('______________________________')
    details[link] = {'title': title,
                     'des': des,
                     'attr': attr}
print(details)

