from bs4 import BeautifulSoup
import urllib, collections

cons = ['\u091' + str(i) for i in range(5,10)] + ['\u091' + chr(i) for i in range(ord('a'), ord('g'))]  
cons.extend(['\u092' + str(i) for i in range(10)] + ['\u092' + chr(i) for i in range(ord('a'), ord('g'))])
cons.extend(['\u093' + str(i) for i in range(10)])
cons_u = [unicode(i, 'unicode-escape') for i in cons]

count = collections.Counter({})
for i in range(1,6000):
    print i
    url = "http://www.aisiakshare.com/node/"+str(i)
    html = urllib.urlopen(url).read()
    h1 = html.find('Submitted by')
    if h1 != -1:
        h2 = html.find('field_vote')
        html = html[h1:h2]
        soup = BeautifulSoup(html)
        text = soup.get_text()
        
        #print text
        ct = collections.Counter(list(text))     #Dictionary of counts of every character in the file
        
        #Creating a list of unicode characters of all Devanagari consonants 
        
        final_ct = collections.Counter({i: ct[i] for i in cons_u})   #Creating dictionary of counts of only Devanagari consonants
        count = count + final_ct

count_sorted_keys = sorted(count, key=count.get, reverse=True)     #Arranging with counts
for r in count_sorted_keys[:10]:
    print r, count[r]

