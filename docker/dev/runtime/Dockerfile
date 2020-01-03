ARG COMMIT_HASH

FROM crosswatch-dev-environment:${COMMIT_HASH}

LABEL "Maintainer"="CrossWatch Team"

ARG COMMIT_HASH
ARG BRANCH_NAME
ARG PROJ_ROOT

RUN rm -rf /app
ENTRYPOINT [ "/scripts/entrypoint.sh" ]

LABEL "Commit Hash"="${COMMIT_HASH}"
LABEL "Commit URL"="https://github.com/jessjohn/acg-crossing-app/commit/${COMMIT_HASH}"
LABEL "Branch Name"="${BRANCH_NAME}"
LABEL "Branch URL"="https://github.com/jessjohn/acg-crossing-app/tree/${BRANCH_NAME}"
