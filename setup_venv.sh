#!/bin/bash

# Crash on errors.
set -e

DIR_VENV=$(dirname "$0")/venv
if [ -d "$DIR_VENV" ]; then
    echo "deleting existing venv ..."
    rm -fr $DIR_VENV
else
    echo "venv does not exist"
fi

# Install pipx to manage poetry.
if ! [ -x "$(command -v pipx)" ]; then
    echo "pipx not found. Installing it. This step requires that you are not inside a venv."
    make install-pipx
fi


echo "creating new venv ..."
python3.12 -mvenv venv

echo "activating venv ..."
. ${DIR_VENV}/bin/activate

# Install poetry to manage the environment.
if ! [ -x "$(command -v poetry)" ]; then
    echo "installing packages ..."
    make install-poetry
fi

# update paths so e.g. venv/bin/pytest is the $PATH
hash -r

poetry config virtualenvs.path venv --local
poetry config virtualenvs.create false --local
poetry install --no-root -v
