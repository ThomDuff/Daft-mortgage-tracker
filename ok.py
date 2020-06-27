import bs4 as bs
import urllib.request

county = input("Enter a county: ")
city = input("Enter a city: ")
option = input("Do you want a house for sale, rent or to share? ")

if(option == "sale"):
    pageNumber = 0
    for page in range(3):
        print("\nPage number " + str(page+1))
    
        url = 'https://www.daft.ie/' + county + '/property-for-sale/' + city + '/?offset=' + str(pageNumber)
        source = urllib.request.urlopen(url).read()
        soup = bs.BeautifulSoup(source,'lxml')

        for strongs in soup.find_all('strong', class_='PropertyInformationCommonStyles__costAmountCopy'):
            print(strongs.text)
        
        pageNumber += 20

if(option == "rent"):
#    print("\nPage number " + str(page+1))
    
    url = 'https://www.daft.ie/' + county + '/rooms-to-share/' + city
    source = urllib.request.urlopen(url).read()
    soup = bs.BeautifulSoup(source,'lxml')

    for strongs in soup.find_all('strong', class_='price'):
        print(strongs.text)
                        
#    pageNumber += 20

    


#https://www.daft.ie/' + county + '/rooms-to-share/' + city + '/?offset=' + str(pageNumber)
#    pageNumber = 0
#    for page in range(3):


#MUST ADD DYNAMIC PAGE NUMBER
