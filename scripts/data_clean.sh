#!/bin/bash

# Exit on error
set -e

# Run the data cleaning script
python steps_pipelines/data_cleaning_pipeline.py
