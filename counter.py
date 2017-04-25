"""run as 'python counter.py filename' from terminal where filename is the name/path to a text file."""
import codecs, collections, sys
f = codecs.open(sys.argv[1],'r','utf-8')
txt = f.read()

ct = collections.Counter(list(txt))     #Dictionary of counts of every character in the file

#Creating a list of unicode characters of all Devanagari consonants 
cons = ['\u091' + str(i) for i in range(5,10)] + ['\u091' + chr(i) for i in range(ord('a'), ord('g'))]  
cons.extend(['\u092' + str(i) for i in range(10)] + ['\u092' + chr(i) for i in range(ord('a'), ord('g'))])
cons.extend(['\u093' + str(i) for i in range(10)])
cons_u = [unicode(i, 'unicode-escape') for i in cons]

final_ct = {i: ct[i] for i in cons_u}   #Creating dictionary of counts of only Devanagari consonants
final_ct_sorted_keys = sorted(final_ct, key=final_ct.get, reverse=True)     #Arranging with counts
for r in final_ct_sorted_keys[:10]:
    print r, final_ct[r]

