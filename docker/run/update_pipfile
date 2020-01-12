#!/bin/bash
set -e

# Build the image with new dependencies installed and new lockfile generated
pushd "$(git rev-parse --show-toplevel)/docker/dev/environment/"
    bash docker_build
popd

# build the runtime stuff too, since we need to update it when we build the env anyway
pushd "$(git rev-parse --show-toplevel)/docker/dev/runtime/"
    bash docker_build
popd

# The location of the django app folder we want to bind to the running container
APP="$(git rev-parse --show-toplevel)/ACGCrossingApp"

# Run a container from the image and update the lockfile in our local git project
docker run \
    --mount type=bind,source=${APP},target=/live-app \
    crosswatch-dev-environment:latest pipfile
