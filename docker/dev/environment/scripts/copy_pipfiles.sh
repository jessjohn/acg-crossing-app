#!/bin/bash
set -e

# overwrite the mounted pipfile.lock
cp /app/Pipfile.lock /live-app/
