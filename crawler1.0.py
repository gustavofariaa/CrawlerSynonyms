import crawler
import random

def recursiveRequest():
    while(True):
        text = readFile()
        try:
            word = findWordInFile(text)
        except:
            print("Empty word_list.txt")
            return None
        crawler.request_word(word)
        print("Synonyms of " + word + " added to word_list.txt")

def readFile():
    file = open('word_list.txt', 'r')
    text = file.read()
    text = text.split(" ")
    file.close()

    return text

def findWordInFile(text):
    pos = int(random.randint(0, int(len(text))))
    word = text[pos]
    
    return word

print("[1] Enter your word \n[2] Recursive \n[0] Exit")
while(True):
    choice = input('Choose: ')
    if choice == '1':
        word = input('Enter a word: ')
        crawler.request_word(word)
        print("Synonyms of " + word + " added to word_list.txt")
    elif choice == '2':
        recursiveRequest()
    elif choice == '0': break