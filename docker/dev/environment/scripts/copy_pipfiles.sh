#!/bin/bash
set -ex

# overwrite the mounted pipfile.lock
cp /app/Pipfile.lock /live-app/
