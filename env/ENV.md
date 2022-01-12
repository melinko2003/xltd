# env 
Env is the project config section.

## Structure:

		~/xltd/env ->
			~/xltd/env/$project_id ->
				~/xltd/env/$project_id/login ( reads/checks from project-user.db )
				~/xltd/env/$project_id/etc ->
					~/xltd/env/$project_id/etc/config.yaml
						webserver: 		(python|wsgi|???)
						python_version:	$(python -v)
						runtime:		(isolated|shared|both|user-defined)
Ref: [architecture.md](../docs/design/architecture.md)  

