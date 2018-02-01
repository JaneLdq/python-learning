from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string

def clean(input):
    input = re.sub('\n+', ' ', input)
    input = re.sub('\[[0-9]*\]', "", input)
    input = re.sub(' +', ' ', input)
    input = bytes(input, 'utf-8')
    input = input.decode('ascii', 'ignore')
    input = input.split(' ')
    cleanInput = []
    for item in input:
        item = item.strip(string.punctuation)
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput

def ngrams(input, n):
    input = clean(input)
    output = []
    for i in range(len(input) - n + 1):
        output.append(input[i:i+n])
    return output

def distinctNgrams(input, n):
    input = clean(input)
    output = dict()
    for i in range(len(input) - n + 1):
        newNgram = "".join(input[i:i+n])
        if newNgram in output:
            output[newNgram] += 1
        else:
            output[newNgram] = 1
    return output


html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, 'lxml')
content = bsObj.find('div', {'id': 'mw-content-text'}).get_text()
# ngrams = ngrams(content, 2)
ngrams = distinctNgrams(content, 2)
ngrams = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1]))
print(ngrams)
print("2-ngrams count is: " + str(len(ngrams)))
