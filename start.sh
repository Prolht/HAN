#!/bin/bash
conda_env=han
source activate $conda_env
nohup python manage.py runserver 0.0.0.0:8000 >> server.log 2>&1 &
ps -ef |grep 8000
