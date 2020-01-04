# Stage 1
# - Make sure pipenv is installed
# - Check if Pipfile has changed
# - If it has, reinstall dependencies so it's FRESH
# - Generate a new Pipefile.lock and update it in the project
# - Now we have an updated environment
# ---------------------------------------------------------
FROM python:3 as build-system

RUN mkdir /code && \
    pip install --user pipenv

ADD ACGCrossingApp /code

# Stage 2
# ---------------------------------------------------------
FROM build-system as runtime

LABEL "Maintainer"="CrossWatch Team"

ARG COMMIT_HASH
ARG BRANCH_NAME

ENV PYTHONUNBUFFERED 1

LABEL "Commit Hash"="${COMMIT_HASH}"
LABEL "Commit URL"="https://github.com/jessjohn/acg-crossing-app/commit/${COMMIT_HASH}"
LABEL "Branch Name"="${BRANCH_NAME}"
LABEL "Branch URL"="https://github.com/jessjohn/acg-crossing-app/tree/${BRANCH_NAME}"