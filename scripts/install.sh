#!/usr/bin/env bash
cd ..

rm env
rm build
rm dist

python3 -m venv env
source env/bin/activate

python -m pip install --upgrade pip
pip install --upgrade setuptools
python setup.py install
