FROM python:3

LABEL "Maintainer"="CrossWatch Team"

ARG COMMIT_HASH
ARG BRANCH_NAME
ARG PROJ_ROOT

ENV PYTHONUNBUFFERED 1
ENV PATH="/root/.local/bin:${PATH}"

ENV TINI_VERSION v0.18.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini

RUN chmod +x /usr/bin/tini && \
    mkdir /app && \
    pip install --user pipenv

ADD ACGCrossingApp/ /app/
ADD scripts/ /scripts/

WORKDIR /app
RUN chmod 755 /scripts/* && \
    pipenv lock && \
    pipenv install --system

ENTRYPOINT [ "/scripts/entrypoint.sh" ]

LABEL "Commit Hash"="${COMMIT_HASH}"
LABEL "Commit URL"="https://github.com/jessjohn/acg-crossing-app/commit/${COMMIT_HASH}"
LABEL "Branch Name"="${BRANCH_NAME}"
LABEL "Branch URL"="https://github.com/jessjohn/acg-crossing-app/tree/${BRANCH_NAME}"
