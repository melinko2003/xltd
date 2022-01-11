# Architecture ( For Nowish )

	Python3 ->
		/opt/xltd/bin ->
			/opt/xltd/bin/python3.11
			/opt/xltd/bin/xltd ( #!/opt/xltd/bin/python3.11 )
		/opt/xltd/env ->
			/opt/xltd/env/$project ->
				/opt/xltd/env/$project/login ( reads/checks from project-user.db )
				/opt/xltd/env/$project/etc ->
					/opt/xltd/env/$project/etc/engine.yaml ( Python built in Webserver, WSGI, etc. )
					/opt/xltd/env/$project/etc/python-version.yaml ( version# drives runtime pyvenvs )
					/opt/xltd/env/$project/etc/runtime.yaml ( shared or isolation )
		/opt/xltd/runtime ->
			/opt/xltd/runtime/shared ->
				/opt/xltd/runtime/shared/$python-version ->
					/opt/xltd/runtime/shared/$python-version/$project_id ->
						/opt/xltd/runtime/shared/rt-$python-version/$project_id/$function-$version ( End Point )
						/opt/xltd/runtime/shared/rt-$python-version/$project_id/metrics
			/opt/xltd/runtime/isolation ->
				/opt/xltd/runtime/isolation/$project_id ->
					/opt/xltd/runtime/isolation/$project_id/$python-version ->
						/opt/xltd/runtime/isolation/$project_id/rt-$python-version/$function-$version ( End Point )
						/opt/xltd/runtime/isolation/$project_id/rt-$python-version/metrics ( End Point )
