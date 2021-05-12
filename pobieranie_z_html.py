'''
BeautifulSoup4 Module
do parsowania html'a

'''
'''
url = 'https://www.amazon.com/Automate-Boring-Stuff-Python-Programming/dp/1593275994/'
headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
res = requests.get(url, headers=headers)
print(res.raise_for_status())

soup = bs4.BeautifulSoup(res.text, 'html.parser') # html.parser aby nie było warrninga

niestety amazon trochę pomieszał i nie działa ani xpath, ani css

#elems = soup.xpath('//*[@id="a-autoid-7-announce"]/span[2]/span')
elems2 = soup.select('#priceblock_dealprice')[0].text
print(elems2[0].text.strip)
'''

import bs4, requests

def getAmazonPrice(productUrl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}

    res = requests.get(productUrl, headers=headers)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    #elem = soup.select('#priceblock_dealprice') #cssselector
    elem = soup.xpath(r'//*[@id="mediaTab_heading_1"]/a/span/div[2]/span') #xpath
    #elem = soup.xpath(r'/ html / body / div[2] / div[2] / div[3] / div[9] / div / div[2] / div[2] / div / div / div[1] / div / ul / li[
        2] / a / span / div[2] / span') #full xpath
    return elem[0].text.strip()

getAmazonPrice('https://www.amazon.com/Automate-Boring-Stuff-Python-Programming-dp-1593275994/dp/1593275994/ref=mt_other?_encoding=UTF8&me=&qid=')

