import bs4 as bs
import urllib.request

#county = input("Enter a county: ")
#city = input("Enter a city: ")
#option = input("Do you want a house for sale, rent or to share? ")

#if(option == "sale"):
#    pageNumber = 0
#    for page in range(3):
#        print("\nPage number " + str(page+1))
    
url = 'https://www.daft.ie/westmeath/property-for-sale/mullingar/?ad_type=sale&advanced=1&s%5Badvanced%5D=1&searchSource=sale'
source = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(source,'lxml')

#ul = soup.ul

span = soup.find_all('span', attrs={'class':'paging clear'})
for spans in span:
    print(span.href)
        


#url = 'https://www.daft.ie/' + county + '/property-for-sale/' + city + '/?offset=' + str(pageNumber)
