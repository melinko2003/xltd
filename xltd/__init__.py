#!/usr/bin/env python3

# Mode Flags

# --mode : ( Admin | User )

# User related Flags ( Admin Only )

# --create-user : Create users ( Admin Only)
# --read-user   : View user attributes ( Admin Only )
# --update-user : Update user attributes ( Admin Only )
# --delete-user : Remove Users ( Admin Only )

# Project related Flags

# --create-project : Create projects ( Admin Only )
# --read-project   : View project attributes ( Admin, User, Svc )
# --update-project : Update project attributes ( Admin, User )
# --delete-project : Remove projects ( Admin, User )

# Function related Flags

# --create-function : Create functions ( Admin, User )
# --read-function   : View function attributes ( Admin, User, Svc )
# --update-function : Update function attributes ( Admin, User )
# --delete-function : Remove functions ( Admin, User )

# Runtime related Flags

# --create-runtime : Create runtime ( Admin, User, Svc )
# --read-function   : View runtime attributes ( Admin, User, Svc )
# --update-runtime : Update runtime attributes ( Admin, User, Svc )
# --delete-runtime : Remove runtime ( Admin, User, Svc )

# Util related Flags ( Admin Only )

# --new-install : Sets up a new installation ( Admin Only )
# --import-item : Imports ( user , project , function , runtime ) ( Admin Only )
# --export-item : Imports ( user , project , function , runtime ) ( Admin Only )
