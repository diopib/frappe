#  -*- coding: utf-8 -*-

# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# MIT License. See license.txt

from __future__ import unicode_literals
import unittest

from frappe.utils.bot import BotReply

class TestBot(unittest.TestCase):
	def test_hello(self):
		reply = BotReply().get_reply('hello')
		self.assertEquals(reply, 'Hello Administrator')

	def test_open_notifications(self):
		reply = BotReply().get_reply('whatsup')
		self.assertTrue('your attention' in reply)

	def test_find(self):
		reply = BotReply().get_reply('find user in doctypes')
		self.assertTrue('[User](#Form/DocType/User)' in reply)

	def test_not_found(self):
		reply = BotReply().get_reply('find yoyo in doctypes')
		self.assertTrue('Cound not find' in reply)

	def test_list(self):
		reply = BotReply().get_reply('list users')
		self.assertTrue('[test@example.com]' in reply)