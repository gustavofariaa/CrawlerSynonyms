# Crawler Synonyms
A crawler to find synonyms on [website](https://www.sinonimos.com.br/).

## Getting Started

Clone the repository into a folder of your preference:

```
git clone git@bitbucket.org:gustavofariaa/crawler-synonyms.git
```

After completing the download, go to the created folder:

```
cd Crawler-Synonyms
```

## Running

Open your terminal or cmd and enter this command:

```
python3 crawler1.0.py
```

## Crawler

In the main view, choose a option:

```
[1] Enter your word 
[2] Recursive 
[0] Exit
Choose: 
```

* [1] You will enter a word and the synonyms of your word will be added to a line of word_list.txt.
* [2] The crawler will take a random word from the word_list.txt file and adds the synonyms back to a new line of word_list.txt. This process will occur recursively, until you force the program exit, closing the terminal or the prompt.
* [0] You will exit the program.
* Another choice won't be processed.
