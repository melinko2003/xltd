# Architecture ( For Nowish )

	Python3 ->
		~/xltd/bin ->
			~/xltd/bin/python3.11
			~/xltd/bin/xltd ( #!/opt/xltd/bin/python3.11 ) 
			~/xltd/bin/xltd-pipeline-linter
			~/xltd/bin/xltd-pipeline-security
			~/xltd/bin/xltd-runtime

		~/xltd/etc ->
			~/xltd/etc/xltd.conf
			~/xltd/etc/xltd-runtime.conf

		~/xltd/env ->
			~/xltd/env/$project_id ->
				~/xltd/env/$project_id/login ( reads/checks from project-user.db )
				~/xltd/env/$project_id/etc ->
					~/xltd/env/$project_id/etc/config.yaml
						webserver: 		(python|wsgi|???)
						python_version:	$(python -v)
						runtime:		(isolated|shared|both|user-defined)

		~/xltd/runtime ->
			~/xltd/runtime/shared ->
				~/xltd/runtime/shared/$python-version ->
					~/xltd/runtime/shared/$python-version/$project_id ->
						~/xltd/runtime/shared/rt-$python-version/$project_id/$version/$function ( End Point )
						~/xltd/runtime/shared/rt-$python-version/$project_id/$version/metrics ( Prometheus Point )
			~/xltd/runtime/isolation ->
				~/xltd/runtime/isolation/$project_id ->
					~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id ->
						~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id/$version/$function ( End Point )
						~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id/$version/metrics ( Prometheus Point )
