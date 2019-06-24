# mastermind-gui
An implementation of mastermind in python 3, using tkinter for a gui

## IMPORTANT
the gui was optimized for my 768x1366 monitor on OSX. therefore on larger monitors you may have to increase `SIZE` on line 4.
if the window is partially obscured, decrease `window_availability_factor` on line 3.

### RULES
if you've never played mastermind, see https://en.wikipedia.org/wiki/Mastermind_(board_game) for rules.
this version allows you to select the number of colors to use from 3 to 8, how many pegs the combination consistes of, and how many attempts you get (the original game uses 6, 4, and 10 respectively).
to guess a combination simply click the squares at the bottom, and when the row is filled up, it will display small squares to the right of the row with black representing a guess that is in the correct spot and the correct color, and gray representing a guess that is the correct color, but the wrong position.
