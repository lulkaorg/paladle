# Paladle
Paladle is a command line based quiz game for the video game "Paladins".

## Overview
Currently there are 5 different categories:
  1. Guessing the Champion by their ult voice lines (text)
  2. Guessing the Champion by one of their voice lines (audio)
  3. Guessing the Champion by the name of their weapon / one ability
  4. Guessing the VGS input keys by the VGS command output
  5. Guessing the talent of a Champion based on the talent description

All Champions are currently only available in categories 1 and 2.
More Champions will be added to categories 3 and 5 over time.

There will also be more categories in the future!

## Planned categories & features
- Random trivia questions about the game
- Guessing the Announcer Pack based on one voice line
- Guessing the item from the item shop

- Being able to use command line options to only play one category

## Known Issues
Currently every input is still case sensitive. This means Champion names, weapon names, ability names, and talent names have to be entered with the first letter in upper case.
The VGS input keys in contrast have to be entered in all lower case.

When the randomly selected Champion to guess is "Bomb King", the game crashes.

## Dependencies
- [pipx](https://pipx.pypa.io/latest/installation/)
- [Python](https://www.python.org/downloads/) 3.12 or older. When trying to use __Python 3.13__ or newer the __installation will fail!__

## Installation
__Using pipx__
- `pipx install git+https://github.com/lulkaorg/paladle.git` (This may take like 2 - 3 minutes)
- Then follow the instructions on screen to add it to the PATH environment variable, to be able to run paladle from everywhere
- Now you can just type `paladle` to run it from everywhere

## Uninstall
`pipx uninstall paladle`

## Disclaimer
All of the audio files of the champions belong to Hi-Rez Studios.
