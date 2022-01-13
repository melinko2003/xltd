#!/usr/bin/env python3
# import xltd
# Ideal method of execution is like pip ... ie. 
# python3 -m xltd --mode= ...

# Parser Arguements
parser = argparse.ArgumentParser(description='Help Construct Messages')

# Mode Flags

# --mode : ( Admin | User )
parser.add_argument('-m','--mode', type=str, required=True, help='Mode: Admin, Svc, User, $Custom_Def ')
# Username : 
parser.add_argument('-u','--user', type=str, required=True, help='Mode: Admin, Svc, User, $Custom_Def ')
# Password : 
parser.add_argument('-p','--pass', type=str, required=True, help='Mode: Admin, Svc, User, $Custom_Def ')

# User related Flags ( Admin Only )

# --create-user : Create users ( Admin Only)
parser.add_argument('-cu','--create-user', type=str, required=True, help='')
# --read-user   : View user attributes ( Admin Only )
parser.add_argument('-ru','--read-user', type=str, required=True, help='')
# --update-user : Update user attributes ( Admin Only )
parser.add_argument('-uu','--update-user', type=str, required=True, help='')
# --delete-user : Remove Users ( Admin Only )
parser.add_argument('-du','--delete-user', type=str, required=True, help='')

# Project related Flags

# --create-project : Create projects ( Admin Only )
parser.add_argument('-cp','--create-project', type=str, required=True, help='')
# --read-project   : View project attributes ( Admin, User, Svc )
parser.add_argument('-rp','--read-project', type=str, required=True, help='')
# --update-project : Update project attributes ( Admin, User )
parser.add_argument('-up','--update-project', type=str, required=True, help='')
# --delete-project : Remove projects ( Admin, User )
parser.add_argument('-dp','--delete-project', type=str, required=True, help='')

# Function related Flags

# --create-function : Create functions ( Admin, User )
parser.add_argument('-cf','--create-function', type=str, required=True, help='')
# --read-function   : View function attributes ( Admin, User, Svc )
parser.add_argument('-rf','--read-function', type=str, required=True, help='')
# --update-function : Update function attributes ( Admin, User )
parser.add_argument('-uf','--update-function', type=str, required=True, help='')
# --delete-function : Remove functions ( Admin, User )
parser.add_argument('-df','--delete-function', type=str, required=True, help='')

# Runtime related Flags

# --create-runtime : Create runtime ( Admin, User, Svc )
parser.add_argument('-cr','--create-runtime', type=str, required=True, help='')
# --read-function   : View runtime attributes ( Admin, User, Svc )
parser.add_argument('-rr','--read-runtime', type=str, required=True, help='')
# --update-runtime : Update runtime attributes ( Admin, User, Svc )
parser.add_argument('-ur','--update-runtime', type=str, required=True, help='')
# --delete-runtime : Remove runtime ( Admin, User, Svc )
parser.add_argument('-dr','--delete-runtime', type=str, required=True, help='')

# Util related Flags ( Admin Only )

# --new-install : Sets up a new installation ( Admin Only )
parser.add_argument('-ni','--new-install', type=str, required=True, help='')
# --import-item : Imports ( user , project , function , runtime ) ( Admin Only )
parser.add_argument('-ii','--import-item', type=str, required=True, help='')
# --export-item : Imports ( user , project , function , runtime ) ( Admin Only )
parser.add_argument('-ei','--export-item', type=str, required=True, help='')

# Colonize



# Parser Arguements



if "svc_" in parser.parse_args().task.lower():
	svc.cli(task=parser.parse_args().task.lower(),params=parser.parse_args())
else:
	xli.cli(task=parser.parse_args().task.lower(),params=parser.parse_args())