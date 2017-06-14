from bs4 import BeautifulSoup
import urllib, collections, codecs

f = codecs.open('aisi.txt','w','utf-8')
for i in range(1,6000):
    print i
    url = "http://www.aisiakshare.com/node/"+str(i)
    html = urllib.urlopen(url).read()
    h1 = html.find('Submitted by')
    if h1 != -1:
        h2 = html.find('fb-root')
        if h2 != -1:
            html = html[h1:h2]
            soup = BeautifulSoup(html)
            text = soup.get_text()
            f.write(text)
        else:
            pass
        
        #print text

f.close()
