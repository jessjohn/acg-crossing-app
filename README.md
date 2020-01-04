# acg-crossing-app api
The REST API for the ACG Crossing Guard App (RHoK #11). 

# Dependencies (Docker)
## Dependencies (Mac)
* Docker for Mac

## Dependencies (Windows)
* Docker Desktop for Windows

## Dependencies (Linux)
* [Docker Engine](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [Docker Compose](https://docs.docker.com/compose/install/)



# Dev Workflow (Docker)
## Building the images
### Commands
Assuming you are in the project root directory:
```bash
# Builds the environment image with all dependencies installed
pushd docker && update_pipfile && popd

# Build the runtime image, separate so we don't have to rebuild the environment every time if we aren't adding dependencies
pushd docker/dev/runtime && sh docker_build && popd
```
### Explanation
`update_pipfile` will be used for regenerating the Pipfile.lock when we make changes to the Pipfile by adding a new dependency. It also happens to build the environment so we can use it when we build the first time.

We will build the environment image separately from the runtime image to keep environment updates separate from code changes in the app.

It should also be noted that we will not be copying the app into the image. Rather we will mount our local repo and run the app from there in the container environement. This way we get the benefit of hot-reloading combined with 

---

## Adding a new dependency for the django app
Since we don't want to muck about with managing a python installation on our local machines, we will do everything in a standardized container that will work the same for everyone.

We will manage the environment and the app as separate images so we don't have to rebuild something massive each time and can update the Pipfile quickly when developing.

1. Add the dependency to the Pipfile
2. Run `docker/update_pipfile`

This will:
1. Build the image with your updated Pipfile in it and tag it
2. Install the environment from the updated Pipfile
3. Create a lockfile
4. Update the lockfile in your local git repo using docker volumes

## Running the app
### Set up Postgres
Now that you've built the images as described above, we will need a postgres instance for local development.

> Installing postgres in a hackathon setting also managed to waste away the better part of a day, so let's bring that down to a few simple steps independent of platform.

1. Navigate to the `docker` directory
2. Run `docker-compose up -d`

This will spin up a local postgres and persist data to `/var/lib/postgresql/data`. So while the process is ephemeral, your dev data will be persisted.

You can quickly validate it with `docker ps`

Also, feel free to connect to it with your favourite dbadmin tool like [DbVisualizer](https://www.dbvis.com/) or something.

To kill postgres when you're done developing, just run `docker-compose kill` in the `docker` directory.

### Running the app
Once postgres is up, you can run `sh run_dev runserver` to start the app.

This will be the code from your git repo mounted in the container, so it will be able to live-reload.

To exit, just ue Ctrl+C and the container will shut itself down.

> Note: Any command you pass to `manage.py` can be passed to the run_dev script and it will pass it to the container an execute it.
