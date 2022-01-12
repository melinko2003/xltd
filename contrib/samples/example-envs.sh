#!/bin/bash
# Contrib File: example-envs.sh
# Author: lcurran <melinko2003@gmail.com>
#
# Structure:
#		~/xltd/env ->
#			~/xltd/env/$project_id ->
#				~/xltd/env/$project_id/login ( reads/checks from project-user.db )
#				~/xltd/env/$project_id/etc ->
#					~/xltd/env/$project_id/etc/config.yaml
#						webserver: 		(python|wsgi|???)
#						python_version:	$(python -v)
#						runtime:		(isolated|shared|both|user-defined)

# Sample Set: 10000001
PROJECT_ID="10000001"
ENV="../../env/shared/${PROJECT_ID}"

mkdir -p "${ENV}/etc"

cp login "${ENV}/"

echo "---\nwebserver: 'python'\npython_version: '3.10'\nruntime: 'both'" > ${ENV}/etc/config.yaml

