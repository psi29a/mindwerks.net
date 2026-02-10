#!/bin/bash

# Crash on errors.
set -e

DIR_VENV=$(dirname "$0")/.venv
if [ -d "$DIR_VENV" ]; then
    echo "deleting existing venv ..."
    rm -fr $DIR_VENV
else
    echo "venv does not exist"
fi

# Check if uv is installed
if ! [ -x "$(command -v uv)" ]; then
    echo "uv not found. Installing it..."
    curl -LsSf https://astral.sh/uv/install.sh | sh
fi

echo "syncing dependencies with uv ..."
uv sync

echo "Done! Activate with: source .venv/bin/activate"
