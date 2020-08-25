"""
Script to accept a search term and display the list 10 movies matching the search term
"""

import requests
import json


def main():
    key = 'aa9e49f'
    term = input('Enter search text: ')
    url = 'http://www.omdbapi.com/'
    params = dict(s=term, apikey=key)  # params = {'s': term, 'apikey': key}
    resp = requests.get(url, params)
    data = json.loads(resp.text)

    for movie in data['Search']:
        print('Title  : %s' % movie['Title'])
        print('Year   : %s' % movie['Year'])
        print('Type   : %s' % movie['Type'])
        print('IMDB   : %s' % movie['imdbID'])
        print('-' * 50)


if __name__ == '__main__':
    main()
