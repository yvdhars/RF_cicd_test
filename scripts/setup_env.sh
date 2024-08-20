#!/bin/bash

# Exit on error
set -e

# Update pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

PYTHONPATH=$(pwd) python src
