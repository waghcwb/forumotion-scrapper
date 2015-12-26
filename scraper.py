#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scraper import users

class Forumotion(object):
    def __init__(self):
        super(Forumotion, self).__init__()

        self.version = '?change_version=prosilver&keep_theme=2'


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

def main():
    forumotion = Forumotion()

if __name__ == '__main__':
    main()