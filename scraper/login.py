# -*- coding: utf-8 -*-

import requests
from os.path import isfile

class Login(object):
	def __init__(self):
		super(Login, self).__init__()


	def isLogged(self):
		return False

	def getPassword(self):
		filename = 'account.info'

		if not isfile(filename):
			username = raw_input('Forum owner account login:\n')
			password = raw_input('Forum owner account password:\n')
			save = raw_input('Store password unencrypted? [yes/no]\n')

			if save.lower() == 'yes':
				with open(filename, 'a+') as fileout:
					fileout.write('username: %s\n' % username)
					fileout.write('password: %s' % password)
		else:
			with open(filename, 'r') as file:
				content = file.read()
				content = content.split('\n')

				username = content[0].split('username: ')[1]
				password = content[1].split('password: ')[1]

		return username, password