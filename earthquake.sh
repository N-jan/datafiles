#!/bin/bash
git clone https://github.com/GoogleCloudPlatform/training-data-analyst

ls

cd /training-data-analyst/courses/bdml_fundamentals/demos/earthquakevm

./ingest.sh

./install_missing.sh

./transform.py


gcloud auth login

