# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

class Users(object):
	def __init__(self):
		super(Users, self).__init__()
		
		self.url = '/memberlist'


	def memberlist(self, userdata):
		url = '%s%s%s' % (userdata['forum'], self.url, userdata['version'])
		request = requests.get(url)
		soup = BeautifulSoup(request.text, 'html.parser')

		members = soup.select('.avatar-mini')

		for member in members:
			# print member.contents[0]
			print member.select('strong')[0].contents[0]