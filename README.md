# crypto-icat

This script is inspired by [this project](https://github.com/ph04/pokemon-icat)

![Screenshot](screenshot.png)

## Installation

**Important**: this script currently works only on Kitty, but in [crypto-icat.sh](crypto-icat.sh) you can change this behaviour by editing the last line, which shows the picture in the terminal.

To install the script, you must first have all the necessary packages installed:

- Python 3.x
- pip3


After making sure that you have all of these installed, run this command:

```sh
git clone https://github.com/ph04/pokemon-icat && cd pokemon-icat && chmod +x install.sh && ./install.sh
```

which should start the installation process of the script, by downloading every picture of every Pokémon.

By default, this will download every Pokémon with an upscaling factor of the original image of `9`, but if you want to change this, run the last command with the option `--upscale [upscaling factor]`, for example:

```sh
./install.sh -u 15
```

## Usage

To show a random pokemon, simply run:

```sh
$HOME/.pokemon-icat/pokemon-icat.sh
```
