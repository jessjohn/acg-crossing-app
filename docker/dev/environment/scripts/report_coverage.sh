#!/bin/bash
set -ex 

function join_by { local IFS="$1"; shift; echo "$*"; }

SRC_FILES_LIST=(
    "/live-app/schedule"
    "/live-app/livedata"
)

SRC_FILES="$(join_by , "${SRC_FILES_LIST[@]}")"

cd /live-app
coverage run --source="${SRC_FILES}" manage.py test
coverage report