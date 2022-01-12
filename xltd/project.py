#!/usr/bin/env python3
#
# Project related Flags

# --create-project : Create project ( Admin Only )
# --read-project   : View project attributes ( Admin, User, Svc )
# --update-project : Update project attributes ( Admin, User )
# --delete-runtime : Remove project ( Admin Only )

class project():
    ## Init of project class
	def __init__(self, ???):

	# Create project ( Admin Only )
	def create_project(self, user=self.user_id, project=???)

	# View project attributes ( Admin, User, Svc )
	def read_project(self, user=self.user_id, project=self.project_id):

	# Update project attributes ( Admin, User )
	def update_project(self, user=self.user_id, project=self.project_id):

	# Remove project ( Admin Only )
	def delete_project(self, user=self.user_id, project=self.project_id):
