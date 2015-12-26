#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scraper.users import Users
from scraper.login import Login

import requests

class Forumotion(object):
	def __init__(self):
		super(Forumotion, self).__init__()

		self.users = Users()
		self.login = Login()

		userdata = self.login.getPassword()

def main():
	forumotion = Forumotion()

if __name__ == '__main__':
	main()