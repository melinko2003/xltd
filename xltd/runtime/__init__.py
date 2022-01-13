#!/usr/bin/env python3
# import xltd.runtime
#
# Runtime related Flags

# --create-runtime : Create runtime session ( Admin, User, Svc )
# --read-function   : View runtime attributes ( Admin, User, Svc )
# --update-runtime : Update runtime attributes ( Admin, User, Svc )
# --delete-runtime : Remove runtime session ( Admin, User, Svc )

class runtime():
	## Init of runtime class
	def __init__(self, session=self.runtime_session_id) :

	# Create runtime ( Admin, User, Svc )
	def create_runtime(self, user=self.user_id, function=self.function_id, project=self.project_id, version=self.function_version):

	# View function attributes ( Admin, User, Svc )
	def read_runtime(self, user=self.user_id, session=self.runtime_session_id):

	# Update runtime attributes ( Admin, User, Svc )
	def update_runtime(self, user=self.user_id, session=self.runtime_session_id, function=self.function_id, project=self.project_id, version=self.function_version):

	# Remove runtime ( Admin, User, Svc )
	def delete_runtime(self, user=self.user_id, session=self.runtime_session_id):
