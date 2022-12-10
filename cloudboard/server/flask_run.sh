#!/bin/zsh
source ~/.zshrc
export FLASK_APP=/home/adisri/dcsc/cloudboard/cloudboard/server
export FLASK_DEBUG=1

workon v311
flask run