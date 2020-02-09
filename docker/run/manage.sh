#!/bin/bash

APP="$(git rev-parse --show-toplevel)/ACGCrossingApp"
echo "${APP} will be mounted to /live-app directory"

echo "Running ${APP}"

# winpty will need to be prepended to "docker" in windows bash environments
if [[  "$OSTYPE" == "msys" ]] 
then
    winpty docker run \
        -it \
        -p 8000:8000 \
        --network=docker_crosswatch-dev \
        --mount type=bind,source=${APP},target=/live-app \
        crosswatch-dev:latest manage "${@}"

else
    docker run \
        -it \
        -p 8000:8000 \
        --network=docker_crosswatch-dev \
        --mount type=bind,source=${APP},target=/live-app \
        crosswatch-dev:latest manage "${@}"
fi
    
