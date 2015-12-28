#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scraper.users import Users
from scraper.login import Login
from scraper.database import Database

import requests

class Forumotion(object):
	def __init__(self):
		super(Forumotion, self).__init__()

		self.users = Users()
		self.login = Login()
		self.database = Database()

		userdata = self.login.getPassword()

		connection = self.database.connect('scraper/database.db')
		cursor = connection.cursor()
		cursor.execute('INSERT INTO users VALUES (0, "waghcwb", 1451322521, "0", "")')
		connection.commit()
		connection.close()

		# self.users.memberlist(userdata)

def main():
	forumotion = Forumotion()

if __name__ == '__main__':
	main()