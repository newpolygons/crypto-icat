#!/bin/bash

output=$(python3 $HOME/.crypto-icat/random_crypto.py $1)

echo $output

IFS=' ' read -r -a split <<< "$output"

crypto=${split[0]}

echo " "
echo " "

### CHANGE THIS LINE IF YOU NEED TO USE THIS SCRIPT ON ANOTHER TERMINAL
kitty icat --align left --silent $HOME/.crypto-icat/crypto-icons/$crypto
