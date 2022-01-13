#!/usr/bin/env python3
# import xltd.util
#
# Util related Flags ( This should be build directly into our keystore )

# --new-install : Sets up a new installation ( Admin Only )
# --import-item : Imports ( user , project , function , runtime ) ( Admin Only )
# --export-item : Imports ( user , project , function , runtime ) ( Admin Only )

class util():
	## Init of util class
	def __init__(self, ???) :
		roles=['none']

	# Imports an 'item' ( ie. user , project , function , runtime ) ( Admin Only )
	def import_item(self,item):
		roles=['none']

	# Exports an 'item' ( ie. user , project , function , runtime ) ( Admin Only )
	def export_item(self,item):
		roles=['none']

	# New Install 
	def new_install(self):
		# Create all DBs
		self.create_xltd_dbs(db='all')
		# Set a Random Password & set reset password bit
		self.password_reset(self,user='admin',func='new_user',table='admin')

	# Created DBs for ( admin , svc , user , project , function , runtime , all ) 
	def create_xltd_dbs(self, db='all'):
		roles=['none']

	# 
	def password_reset(self,user='admin',func='new_user',table='admin'):
	