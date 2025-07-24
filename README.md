# Paladle
Paladle is a command line based quiz game for the video game "Paladins".

## Overview
Currently there are 5 different categories:
  1. Guessing the Champion by their ult voice lines (text)
  2. Guessing the Champion by one of their voice lines (audio)
  3. Guessing the Champion by the name of their weapon / one ability
  4. Guessing the VGS input keys by the VGS command output
  5. Guessing the talent of a Champion based on the talent description

There will also be more categories in the future!  

Use `paladle` with command line options to only play one selected category.  
For example `paladle -a` to only play the "Guess the VGS key combination" category.  
To see all available command line options, type `paladle -h`.

- "Betty La Bomba" has been shortened to just "Betty".  
- Currently you have to write the apostrophe (') in Talent names etc. (for example: Rogue's Gambit, instead of Rogues Gambit). So keep that in mind!

## Planned categories & features
- Random trivia questions about the game
- Guessing the Announcer Pack based on one voice line
- Guessing the item from the item shop

## Known Issues
Currently every input is still case sensitive. This means Champion names, weapon names, ability names, and talent names have to be entered with the first letter in upper case.
The VGS input keys in contrast have to be entered in all lower case.

## Dependencies
- [pipx](https://pipx.pypa.io/latest/installation/)
- [Python](https://www.python.org/downloads/) 3.12 or older. When trying to use __Python 3.13__ or newer the __installation will fail!__

## Installation
__Using pipx__
- `pipx install git+https://github.com/lulkaorg/paladle.git` (This may take like 2 - 3 minutes)
- Then follow the instructions on screen to add it to the PATH environment variable, to be able to run paladle from everywhere
- Now you can just type `paladle` to run it from everywhere

## Updating
- To update Paladle, you have to reinstall it
`pipx reinstall paladle`

## Uninstall
`pipx uninstall paladle`

## Disclaimer
All of the audio files of the champions belong to Hi-Rez Studios.
