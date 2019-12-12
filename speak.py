import os
import time

def sentence(sentence):
    sentence = sentence.split('.')
    for word in sentence:
        word = word.rstrip('\n')
        print(word)
        os.system('say ' + word)

def main():
    with open('quotes.txt', 'r') as quotes:
        lines = quotes.readlines()
        print(lines)
        for line in lines:
            line = line.rstrip('\n')
            sentence(line)

if __name__ == '__main__':
    main()
