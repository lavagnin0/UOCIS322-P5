# UOCIS322 - Project 4 #
Brevet time calculator.
Author: Jeremy Lavagnino, jlavagni@uoregon.edu
## Overview

Reimplementation of the RUSA ACP controle time calculator with Flask and AJAX.

## About ACP controle times

That's *"controle"* with an *e*, because it's French, although "control" is also accepted. Controls are points where a rider must obtain proof of passage, and control[e] times are the minimum and maximum times by which the rider must arrive at the location.

The algorithm for calculating controle times is described here [https://rusa.org/pages/acp-brevet-control-times-calculator](https://rusa.org/pages/acp-brevet-control-times-calculator). Additional background information is given here [https://rusa.org/pages/rulesForRiders](https://rusa.org/pages/rulesForRiders). Some of the specifications are somewhat ambiguous, so the current RUSA ACP control time calculator ([https://rusa.org/octime_acp.html](https://rusa.org/octime_acp.html)) has been used to clarify them. Specifically, the table with minimum/maximum speeds has the boundary distances (such as 200 km) in multiple rows, making unclear which one to use. I determined that the first row the value appears in is always used (so for 200 km, that would mean a max speed of 34 km/h instead of 32), which is what my program uses. Additionally, I determined through experimentation with the online calculator that it rounds up to the nearest minute from 30+ seconds and down from 29 seconds and below, which is how I implemented the rounding behaviour in this program. Also, the algorithm now takes into account the set close times for brevets available at https://en.m.wikipedia.org/wiki/Randonneuring.

## Usage
Use docker-compose in the brevets directory to run and build the images for the site and database. To use the website, simply input the distances from the start of the controle locations in either of the first two columns depending on whether you prefer to use miles or kilometers, and the start/close time columns will be calcualted and automatically filled in. Note that all distances are converted to km for backend calculations.

## Saving times

You can save one set of time calculations at a time to the database for seperate viewing by pressing the "Submit" button. Pressing "Submit" will save the distance in kilometers, open time, and close time of all the controles currently in the form, and will overwrite any previously-saved values. If there are multiple controls at the same distance in the form, only one of them will be saved in the database. Pressing "Display" will open a seperate page displaying all of the most-recently submitted control information. If no times have been submitted, "Display" will only display an error message on the main page.

## Credits

Michal Young, Ram Durairajan, Steven Walton, Joe Istas.
