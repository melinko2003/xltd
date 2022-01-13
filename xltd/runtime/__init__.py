#!/usr/bin/env python3
# import xltd.runtime
#
# Runtime related Flags

# --create-runtime : Create runtime session ( Admin, User, Svc )
# --read-runtime   : View runtime attributes ( Admin, User, Svc )
# --update-runtime : Update runtime attributes ( Admin, User, Svc )
# --delete-runtime : Remove runtime session ( Admin, User, Svc )

class runtime():
	## Init of runtime class
	def __init__(	self,
		auth_token="admin", # Setting Admin here until Auth system is in place.
		project_id="1",
		location="/var/xltd/runtime/", 
		runtime_mode="isolation",
		python_version="default",		
		function_id="1000000",
		function_version="1",  
		function_name="hello_world" ):
		# Security First ( Login/Auth method )
		roles=['admin'] # Roles allowed to access runtime
		# VERY VERY Basic Challenge ( todo: revamp auth )
		if auth_token not in roles:
			exit(1)

		# Variable Assignment

		# Init Mapping 
		self.project_id=project_id
		self.location=location
		self.runtime_mode=runtime_mode
		self.python_version=python_version
		self.function_id=function_id
		self.function_version=function_version
		self.function_name=function_name

		# Runtime Mapping 
		self.runtime_map=(	
			self.project_id,
			self.location,
			self.runtime_mode,
			self.python_version,
			self.function_id,
			self.function_version,
			self.function_name )

	# Create runtime ( Admin, User, Svc )
	def create_runtime(self,runtime=self.runtime_map):
		roles=['None']

		# Need to sit down and work out how to support:
		# ~/xltd/runtime/shared/rt-$python-version/$project_id/$version/$function ( End Point )
		# $XLTD_PATH/runtime
		# ~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id/$version/$function ( End Point )
							
	# View function attributes ( Admin, User, Svc )
	def read_runtime(self, user=self.user_id, session=self.runtime_session_id):
		roles=['None']

	# Update runtime attributes ( Admin, User, Svc )
	def update_runtime(self, user=self.user_id, session=self.runtime_session_id, function=self.function_id, project=self.project_id, version=self.function_version):
		roles=['None']

	# Remove runtime ( Admin, User, Svc )
	def delete_runtime(self, user=self.user_id, session=self.runtime_session_id):
		roles=['None']
