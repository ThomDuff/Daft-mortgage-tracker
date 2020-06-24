import bs4 as bs
import urllib.request

sauce = urllib.request.urlopen('https://www.daft.ie/kildare/property-for-sale/maynooth/?s%5Bmxp%5D=275000').read()
soup = bs.BeautifulSoup(sauce,'lxml')

for strongs in soup.find_all('strong', class_='PropertyInformationCommonStyles__costAmountCopy'):
    print(strongs.text)
