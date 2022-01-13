#!/usr/bin/env python3
# import xltd.user
#
# User related Flags ( This should be build directly into our keystore )

# --create-user : Create user ( Admin Only )
# --read-user   : View user attributes ( Admin Only )
# --update-user : Update user attributes ( Admin Only )
# --delete-user : Remove user session ( Admin Only )

# Builtin RBAC
# Roles:	Perms(Unix)	Description
# Admin 	(R+W+X+U+G)	Can CRUD Functions, Users, Svc
# User  	(R+W+X)		Can CRUD Functions + Execute
# Svc		(R+X)		Can Read + Execute functions

class user():
	## Init of user class
	def __init__(self, user=self.user_id) :

	# Create user ( Admin Only )
	def create_user(self, username=self.username, role='user'):

	# View user attributes ( Admin Only )
	def read_user(self, username=self.username):

	# Update user attributes ( Admin Only )
	def update_user(self, username=self.username ):

	# Remove user ( Admin Only )
	def delete_user(self, username=self.username, session=self.user_session_id):
