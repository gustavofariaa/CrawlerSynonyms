from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import time

def extract_links(content):
    soup = BeautifulSoup(content, "html.parser")
    links = set()

    for tag in soup.find_all("a", {"class": "sinonimo"}, text=True):
        tag = clean_text(tag) 
        tam = int(len(tag)/2)
        tag = tag[:tam]
        links.add(tag)

    return links

def request_word(word):
    req = Request('https://www.sinonimos.com.br/' + word + '/', headers={'User-Agent': 'Mozilla/5.0'})
    
    content = recursiveExcept(req)

    content = str(content)
    links = extract_links(content) 

    if(len(links) != 0):
        writeWordList(links)
    
    return None

def recursiveExcept(req):
    try:
        content = urlopen(req).read()
    except:
        return None

    return content

def clean_text(text):
    text = str(text).replace('<a class="sinonimo" href="/', '')
    text = str(text).replace('</a>', '')
    text = str(text).replace('/">', '')
    
    try:
        pos = str(text).index('\\')
        text = text[:pos] + text[pos+3:]
    except:
        text = text

    try:
        pos = str(text).index('\\')
        text = text[:pos] + text[pos+3:]
    except:
        text = text
    
    return text

def writeWordList(links):
    wordList = open('word_list.txt','a')
    for link in links:
        wordList.write(link + " ")
    wordList.write("\n")

    wordList.close()