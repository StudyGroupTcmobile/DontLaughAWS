#!/bin/bash

win() {
    echo export PATH=\$HOME/AppData/Local/Programs/Python/Python37/Scripts:\$HOME/AppData/Local/Programs/Python/Python37:\$PATH >> ~/.bashrc

    # export AWS_ACCESS_KEY_ID=
    # export AWS_SECRET_ACCESS_KEY=
    # export REGION_NAME=

    source ~/.bashrc
    set -ex

    pip3 install --upgrade pip \
                        opencv-python \
                        pygame \
                        mutagen \
                        boto3

    exec $SHELL -l
}

mac() {
    echo $HOME
}

case $1 in
    win ) win;;
    mac ) mac;;
esac