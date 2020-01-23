#!/bin/bash[

# sh path/to/init.sh win 

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


# sh path/to/init.sh mac

mac() {
    
    echo "export PATH=/Library/Frameworks/Python.framework/Versions/3.7/bin:$PATH >> ~/.bash_profile"
    echo export PATH='/Library/Frameworks/Python.framework/Versions/3.7/bin:$PATH' >> ~/.bash_profile
    source ~/.bash_profile

    echo "alias python=python3 >> ~/.bashrc"
    echo 'alias python="python3"' >> ~/.bashrc
    source ~/.bashrc

    set -ex

    pip3 install --upgrade pip \
                        opencv-python \
                        pygame \
                        mutagen \
                        boto3
    exec $SHELL -l
}

case $1 in
    win ) win;;
    mac ) mac;;
esac
