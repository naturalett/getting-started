#!/bin/bash
REPO=naturalintmma
APP_NAME=echo-server
VERSION=${1:-v1.0.0}
FULL_TAG="${REPO}/${APP_NAME}:${VERSION}"
docker build . -t "${FULL_TAG}"
docker push "${FULL_TAG}"
