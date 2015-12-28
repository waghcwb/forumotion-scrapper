# -*- coding: utf-8 -*-

import requests
from os.path import isfile

class Login(object):
	def __init__(self):
		super(Login, self).__init__()

		self.version = '?change_version=prosilver&keep_theme=2'


	def login(self, forum, username, password):
		session = requests.Session()
		url = forum + '/login' + self.version

		payload = {
			'username': username,
			'password': password,
			'autologin': 1,
			'redirect': '',
			'query': '',
			'tt': 1
		}

		# request = session.post(url, data=payload)

		# print request.history
		# print request.text
		# print request.headers
		# print request.cookies


	def isValidURL(self, url):
		try:
			response = requests.get(url)

			if response.status_code == 200:
				return True

		except Exception, e:
			raise e


	def getPassword(self):
		filename = 'account.info'

		if not isfile(filename):
			forum = raw_input('Forum URL:\n')
			
			if not self.isValidURL(forum): return

			username = raw_input('Forum owner account login:\n')
			password = raw_input('Forum owner account password:\n')
			save = raw_input('Store password unencrypted? [yes/no]\n')

			if save.lower() == 'yes':
				with open(filename, 'a+') as fileout:
					fileout.write('forum: %s\n' % forum)
					fileout.write('username: %s\n' % username)
					fileout.write('password: %s' % password)
		else:
			with open(filename, 'r') as file:
				content = file.read().split('\n')

				forum    = content[0].split('forum: ')[1]
				username = content[1].split('username: ')[1]
				password = content[2].split('password: ')[1]

		self.login(forum, username, password)

		return {
			'username': username,
			'password': password,
			'forum': forum,
			'version': self.version
		}