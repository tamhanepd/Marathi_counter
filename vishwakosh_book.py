"""This file downloads a particular volume of Marathi Vishwakosh (https://marathivishwakosh.maharashtra.gov.in/) and saves the pages spread across twenty files using a modulo of 20 to the number of Vishkosh page entry.

Run using 'python vishwkosh_book.py volume' from terminal where volume is the Volume of Vishwakosh you want to download, which ranges from 1-20. """
from bs4 import BeautifulSoup
import urllib, collections, codecs, ssl
import numpy as np
import re
import sys
from urlparse import urljoin

vol = str(sys.argv[1])
context = ssl._create_unverified_context()
base_url = 'https://marathivishwakosh.maharashtra.gov.in/khandas/khand'+vol+'/index.php'
for i in range(20):
    locals()['f'+str(i)] = codecs.open('vishwakosh_books_'+str(i)+'.txt','a','utf-8')
#f = codecs.open('vishwakosh_books.txt','w','utf-8')
links = []
url1 = 'https://marathivishwakosh.maharashtra.gov.in/khandas/khand'+vol+'/'
html1 = urllib.urlopen(url1,context=context).read()
soup1 = BeautifulSoup(html1)

for link in soup1.findAll('a',href=re.compile('index.php')):
    links.append(link['href'])
count = 0
for i in range(len(links)):
    print i
    print links[i]
    #url = "https://marathivishwakosh.maharashtra.gov.in/khandas/khand1/index.php/component/content/article?id="+str(i)
    #url = base_url + links[i]
    url = urljoin(base_url, links[i])
    html = urllib.urlopen(url,context=context).read()
    #if html == blank:
    #    continue
    page = str(html)
    number = page.find('\xe0\xa4\xaa\xe0\xa5\x82\xe0\xa4\xb0\xe0\xa5\x8d\xe0\xa4\xa3 \xe0\xa4\xa8\xe0\xa5\x8b\xe0\xa4\x82\xe0\xa4\xa6 \xe0\xa4\xaa\xe0\xa4\xb9\xe0\xa4\xbe')
    if number != -1:
        print 'Using whole page'
        page2 = page[number-200:number]
        linklist = [i for i in page2.split() if i.startswith('href')][0]
        link = [i for i in linklist.split('"') if i.startswith('/khandas')][0]
        #url = base_url + link
        url = urljoin(base_url, link)
        html = urllib.urlopen(url,context=context).read()
    h1 = html.find('article-info-term')
    if h1 != -1:
        h2 = html.find('MVishwakosh')
        if h2 != -1:
            html = html[h1:h2]
            soup = BeautifulSoup(html)
            text = soup.get_text()
            count += 1
            print 'count', count
            locals()['f'+str(np.mod(count,20))].write(text)
            
#        else:
#            pass
#    else:
#        pass
        #print text

#f.close()
for i in range(20):
    locals()['f'+str(i)].close()
