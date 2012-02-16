#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Copyright (C) 2012 Deepin Inc.
#
# Author: YunQiang Su <wzssyqa@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA.

import os
from ConfigParser import ConfigParser
from Prefix import *
from lockfile import FileLock

BuildStats={
	'needs-build':1,
	
	'dep-wait':101,
	'BD-Uninstallable':102,
	'failed':103,
	
	'building':201,
	'uploaded':202,
	'not-for-us':203,
	'installed':204
}

class LockDB:
	lock = FileLock('/tmp/dwanna-buildd-stats.db')
	
	def lock():
		self.lock.acquire()

	def release():
		self.lock.release()

class Options:
	config = ConfigParser.ConfigParser()
	
	def __init__(self):
		self.config.read([sysconffile, os.path.expanduser(userconffile)])
	
	def get(section, key):
		return self.config.get(section, key)
