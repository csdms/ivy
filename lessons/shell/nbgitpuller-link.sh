#! /usr/bin/env bash
# Make links through the nbgitpuller-link CLI.

HUB=https://explore.openearthscape.org
REPO=https://github.com/csdms/ivy
BRANCH=main
FILE=lessons/pymt/index.ipynb

nbgitpuller-link --version

nbgitpuller-link \
    --jupyterhub-url=$HUB \
    --repository-url=$REPO \
    --branch=$BRANCH \
    --launch-path="$FILE" \
    --interface="lab"
