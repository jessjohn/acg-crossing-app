#!/bin/bash
set -ex

ARG="$1"

case "${ARG}" in
    # For updating the pipfile.lock in the project when a new dependency is added
    pipfile)
        CMD=("/scripts/copy_pipfiles.sh")
        ;;
    # For running any of the django management commands
    manage)
        shift 1
        CMD=("/usr/local/bin/python" "/live-app/manage.py" "${@}")
        ;;
    # For passing through a command (will be run as executable)
    *)
        echo "Command provided is not defined in the entrypoint script. Proceeding in passthrough mode..."
        CMD=("$@")
        ;;
esac

exec /usr/bin/tini -s -- "${CMD[@]}"