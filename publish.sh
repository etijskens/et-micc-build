#!/bin/bash

cd ../et-micc       && micc version -p
cd ../et-micc-build && micc version -p

./align_versions.py

cd ../et-micc       && poetry publish --build
cd ../et-micc-build && poetry publish --build
