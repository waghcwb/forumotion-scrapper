# -*- coding: utf-8 -*-

import sqlite3

class Database(object):
	def __init__(self):
		super(Database, self).__init__()

	def connect(self, database):
		try:
			return sqlite3.connect(database)
		except Exception, error:
			raise error