#!/bin/bash

chmod +x crypto-icat.sh

mkdir -p $HOME/.crypto-icat
mkdir -p $HOME/.crypto-icat/crypto-icons

cp ./*.py $HOME/.crypto-icat
cp crypto-icat.sh $HOME/.crypto-icat
cp manifest.json $HOME/.crypto-icat

python3 $HOME/.crypto-icat/setup_icons.py $1 $2
