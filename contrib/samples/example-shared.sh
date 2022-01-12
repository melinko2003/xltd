#!/bin/bash
# Contrib File: example-shared.sh
# Author: lcurran <melinko2003@gmail.com>
#
# Structure:
#		~/xltd/runtime ->
#			~/xltd/runtime/shared ->
#				~/xltd/runtime/shared/$python-version ->
#					~/xltd/runtime/shared/$python-version/$project_id ->
#						~/xltd/runtime/shared/rt-$python-version/$project_id/$version/$function ( End Point )
#						~/xltd/runtime/shared/rt-$python-version/$project_id/$version/metrics ( Prometheus Point )

# Sample Set: 10000001, rt-system-default, hello_world, 1.0
PROJECT_ID="10000001"
PYTHON_VER="system-version"
FUNC_NAME="hello_world"
FUNC_VER="1-0"
RUNTIME="../../runtime/shared/rt-${PYTHON_VER}/${PROJECT_ID}/${FUNC_VER}"

mkdir -p "${RUNTIME}"

cp hello_world "${RUNTIME}/"
