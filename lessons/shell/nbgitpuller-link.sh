#! /usr/bin/env bash
# Make links through the nbgitpuller CLI.

HUB=https://lab.openearthscape.org
REPO=https://github.com/csdms/espin
BRANCH=main
FILE=lessons/pymt/index.ipynb  # Note: escape space in path with backslash

nbgitpuller-link --version

nbgitpuller-link \
    --jupyterhub-url=$HUB \
    --repository-url=$REPO \
    --branch=$BRANCH \
    --launch-path="$FILE" \
    --interface="lab"
