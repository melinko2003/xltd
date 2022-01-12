#!/bin/bash
# Contrib File: example-isolation.sh
# Author: lcurran <melinko2003@gmail.com>
#
# Structure:
#		~/xltd/runtime ->
#			~/xltd/runtime/isolation ->
#				~/xltd/runtime/isolation/$project_id ->
#					~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id ->
#						~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id/$version/$function ( End Point )
#						~/xltd/runtime/isolation/$project_id/rt-$python-version-$function_id/$version/metrics ( Prometheus Point )

# Sample Set: 10000001, rt-system-default, hello_world, 1.0
PROJECT_ID="10000001"
FUNCTION_ID="10000001"
PYTHON_VER="system-version"
FUNC_NAME="hello_world"
FUNC_VER="1-0"
RUNTIME="../../runtime/isolation/${PROJECT_ID}/rt-${PYTHON_VER}-${FUNCTION_ID}/${FUNC_VER}"

mkdir -p "${RUNTIME}"

cp hello_world "${RUNTIME}/"

