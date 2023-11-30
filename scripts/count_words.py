#!/bin/python3

# Takes 1 argument, the file path

import json, sys

word_len = {}

if len(sys.argv) > 1:
    data = {}
    with open(sys.argv[1]) as f:
        data = json.load(f)
    for i in data["cells"]:
        words = i["source"].split()
        if i["cell_type"] not in word_len:
            word_len[i["cell_type"]] = 0
        word_len[i["cell_type"]] += len(words)
    
    total_words = 0
    for i in word_len:
        total_words += word_len[i]
    print(f"\nTotal words: {total_words}\nCode: {word_len['code']}\nMarkdown: {word_len['markdown']}")