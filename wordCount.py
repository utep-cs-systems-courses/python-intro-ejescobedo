#!/usr/bin/env python3
import sys

def get_word_list(text):
    # Receives a string containing a document
    # Returns a list of strings containing the words in the document
    text = text.lower()
    word_list = []
    curr_wrd = ''
    for c in text:
        if ord(c)>=97 and ord(c)<=122:
            curr_wrd = curr_wrd+c
        else:
            if len(curr_wrd)>0:
                word_list.append(curr_wrd)
                curr_wrd = ''
    return word_list
def main():
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    f = open(inputFile, 'r', encoding="utf8")
    text = f.read()
    f.close()
    text = get_word_list(text)
    text = sorted(text)
    dc = {}
    for word in text:
        if word not in dc:
            dc[word] = 1
        else:
            dc[word] += 1
    f = open(outputFile, "w")
    for word in dc:
        f.write(word+" "+str(dc.get(word))+"\n")
    f.close()
if __name__== "__main__":
  main()