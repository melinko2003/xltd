# Getting Started Flow (CLI) #  

## Admin creates a project ##

A User with admin privileges creates a new project

	$ ./xltd --mode=admin --create-project <project_name> 

## Admin creates a new user ##

A User with admin privileges creates a new user 

	$ ./xltd --mode=admin --create-user <your_email> --role= ( Admin | User | Svc  )

RBAC Matrix ( TODO: Custom Role tooling )

	Roles:	Perms(Unix)	Description
	Admin 	(R+W+X+U+G)	Can CRUD Functions, Users, Svc
	User  	(R+W+X)		Can CRUD Functions + Execute
	Svc		(R+X)		Can Read + Execute functions

### If you forgot to add a Role ###

If you forget to add a role, simply "update" the User.

	$ ./xltd --mode=admin --update-project --add-user/--add-user-id <email>/<user_id> --role ( Admin | User | Svc  )

## Mandatory Password Change ##

Users will be forced to change password on first usage, account ages out or reset. 

	$ ./xltd --mode=user --update --user <email> --user-password <your_new_password>

### If you forget your password ###

How to reset a users password

	$ ./xltd --mode=admin --update-user <your_email> --reset-password

## Creating my first function ##

### Function Creation

Function creation requires the most information as this is your Serverless function.

	$ ./xltd --mode=(admin|user) \
			 --create-function <function_name> \
			 --requirements-(text|file)=(requests,sqlalchemy|requirements.txt) \
			 --python-version=<version#(ie. 3.9 , 3.10, latest)> \
			 --envars-file=<File containing any Vars> \
			 --secrets-entries=<prometheus,scuby> \
			 --linting=true \
			 --security=true \

On function creation, your function then enters xltd's pipeline. Setting linting/security to True will force linting 
and a security check. Pending xlts pipeline ( linting / security ) tasks, your function will be online shortly. If 
your function does/doesn't pass linting, security or other pipeline tasks you'll be able to view the results via 
"read functions" covered in the next step.

### Check the Status

For reading results of the lint, security piece, if / how to access your function, status of your function, and much 
more use the "read-function" bit.

	$ ./xltd --mode=(admin|user) --read-function <function_name> 

## Congrats ##

You've successfully have installed your first "function" as a service to your xltd "controller"

## Next ##

[Secret Management](secrets_management.md)
[RBAC expansion](rbac.md)



