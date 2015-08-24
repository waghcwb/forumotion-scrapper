# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup


class Forumotion(object):

    def __init__(self):
        super(Forumotion, self).__init__()

        print('''
  █▀▀ █▀▄▀█ ░░ █▀▀ █▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀█
  █▀▀ █░▀░█ ▀▀ ▀▀█ █░░ █▄▄▀ █▄▄█ █░░█ █▀▀ █▄▄▀
  ▀░░ ▀░░░▀ ░░ ▀▀▀ ▀▀▀ ▀░▀▀ ▀░░▀ █▀▀▀ ▀▀▀ ▀░▀▀
                                    by: waghcwb
  ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀''')

        self.get_page()

    #
    #   Get the page DOM string
    #

    def get_page(self):
        # text = '  Please, insert the forum URL: '
        memberlist = '/memberlist'
        phpbb3 = '?change_version=prosilver&keep_theme=2'

        try:
            # forum = str(input('%s' % text) + memberlist + phpbb3)
            forum = str('http://www.bestskins.net/' + memberlist + phpbb3)
            request = requests.get(forum)

            self.get_users_length(request)

        except:
            print('Something went wrong while doing the request')

    #
    #   Get how many users page we need to extract
    #

    def get_users_length(self, html):
        soup = BeautifulSoup(html.text, 'html5lib')
        users = len(soup.select('.avatar-mini a'))
        pages = soup.select('.pagination > span > a')
        total = users * int(pages[-2].get_text())
        feedback = '  Aproximadamente %d usuários para extrair' % total

        print('=' * len(feedback))
        print(feedback)

        # with open('index.html', 'w') as result:
        #     result.write(html.text)

        # for link in soup.select('.avatar-mini a'):
        # print(link.get('href').replace('
        # ?change_version=prosilver&keep_theme=2', ''))

if __name__ == "__main__":
    forumotion = Forumotion()
