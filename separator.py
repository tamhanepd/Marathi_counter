"""run as 'python separator.py filename' from terminal where filename is the name/path to a text file. This will print output in the terminal and save the same in a file named as 'ouput_filename'."""
import codecs, collections, sys, unicodedata, string

def splitclusters(s):
    """Generate the grapheme clusters for the string s. (Not the full
    Unicode text segmentation algorithm, but probably good enough for
    Devanagari.)

    Copied this function from a Stackoverflow answer https://stackoverflow.com/a/6806203/3638137 and modified a bit.

    """
    virama = u'\N{DEVANAGARI SIGN VIRAMA}'
    cluster = u''
    last = None
    for c in s:
        cat = unicodedata.category(c)[0]
        if cat == 'M' or cat == 'L' and last == virama:     
        # Adding this character to previous character as a letter, if this character is a vowel OR this character is a consonant and previous character was halanta

            cluster += c
        else:
            if cluster:
                try:
                    if unicodedata.name(cluster[0])[0] == 'D':
                    # Ensuring that only Devanagari characters are counted.
                        yield cluster
                    else:
                        yield None
                except ValueError:
                # Using this because 'unicodedata' is not complete and some characters don't have their info in that module.
                    yield None
            cluster = c
        last = c
    if cluster:
        try:
            if unicodedata.name(cluster[0])[0] == 'D':
                yield cluster
            else:
                yield None
        except ValueError:
            yield None

f = codecs.open(sys.argv[1],'r','utf-8')
txt = f.read()
f.close()
characters_list = list(splitclusters(txt))
count = collections.Counter(characters_list)
dev_numbers = ['\u096' + str(i) for i in range(6,10)] + ['\u096' + chr(i) for i in range(ord('a'), ord('g'))]
dev_numbers_u = [unicode(i, 'unicode-escape') for i in dev_numbers]

# Most unicode punctuations
pp=[unichr(i) for i in xrange(8100,8250) if unicodedata.category(unichr(i)).startswith('P')]
ignore = list(string.printable) + dev_numbers_u + pp + [None]
# Ignoring punctuations, numbers, spaces etc.

for char in ignore:
    if char in count:
        del count[char]

tot_letters = float(sum(count.values()))
tot_freq_letters = len([i for i in count.values() if i>10]) 
print 'Total number of letters', tot_letters 
print 'Total number of distinct letters', len(count)
print 'Total number of frequent (>10) distinct letters', tot_freq_letters
count_sorted_keys = sorted(count, key=count.get, reverse=True)


f2 = codecs.open('output_'+sys.argv[1],'w','utf-8')  # Saves print output to a file output.txt
f2.write('Total number of letters \t'+str(tot_letters)+'\n')
f2.write('Total number of distinct letters \t'+str(len(count))+'\n')
f2.write('Total number of frequent (>10) distinct letters \t'+str(tot_freq_letters)+'\n')
for r in count_sorted_keys:
    #print r, count[r], '{0:.2e}'.format(count[r]/tot_letters)
    print(r +'\t'+str(count[r]) + '\t' + '{0:.2e}'.format(count[r]/tot_letters))
    f2.write(r +'\t'+str(count[r]) + '\t' + '{0:.2e}'.format(count[r]/tot_letters) + '\n')
f2.close()

