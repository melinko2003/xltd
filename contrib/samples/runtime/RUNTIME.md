# runtime 
runtime is where the functions are hosted

## Structure:
### Shared: 
		~/xltd/runtime ->
			~/xltd/runtime/shared ->
				~/xltd/runtime/shared/$python-version ->
					~/xltd/runtime/shared/$python-version/$project_id ->
						~/xltd/runtime/shared/rt-$python-version/$project_id/$version/$function ( End Point )
						~/xltd/runtime/shared/rt-$python-version/$project_id/$version/metrics ( Prometheus Point )
### Isolation
Isolation groups functions by the project Id 

		~/xltd/runtime ->						
			~/xltd/runtime/isolation ->
				~/xltd/runtime/isolation/$project_id ->
					~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id ->
						~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id/$version/$function ( End Point )
						~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id/$version/metrics ( Prometheus Point )

Ref: [architecture.md](../docs/design/architecture.md)  