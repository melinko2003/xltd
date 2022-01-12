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
			~/xltd/env/$project ->
				~/xltd/env/$project/login ( reads/checks from project-user.db )
				~/xltd/env/$project/etc ->
					~/xltd/env/$project/etc/engine.yaml ( Python built in Webserver, WSGI, etc. )
					~/xltd/env/$project/etc/python-version.yaml ( version# drives runtime pyvenvs )
					~/xltd/env/$project/etc/runtime.yaml ( shared or isolation )

		~/xltd/runtime ->
			~/xltd/runtime/shared ->
				~/xltd/runtime/shared/$python-version ->
					~/xltd/runtime/shared/$python-version/$project_id ->
						~/xltd/runtime/shared/rt-$python-version/$project_id/$function-$version ( End Point )
						~/xltd/runtime/shared/rt-$python-version/$project_id/metrics
			~/xltd/runtime/isolation ->
				~/xltd/runtime/isolation/$project_id ->
					~/xltd/runtime/isolation/$project_id/$python-version ->
						~/xltd/runtime/isolation/$project_id/rt-$python-version/$function-$version ( End Point )
						~/xltd/runtime/isolation/$project_id/rt-$python-version/metrics ( End Point )
