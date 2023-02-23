![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome chloemay-1,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!


# Battle Ship 

Battle ship is a terminal python game designed to be a one player game, against the computer. 

This game of battle ship is a single board game, with just the computer board showing. 

## My Version of Battleship

In this version of battleship, the player (you) will pick at letter from A-G and a number from 1-8. Either the player hits one of the computer ships, or not. Both prompt a different response. The player has a limited amount of turns to win the game. 
Both misses and hits will have a different symbol for clarity. 
If the player hits all of the computers ships in the limited amount of turns, the player wins. If not, another triumph for computers.

## Features

This game allows for a single person to play a game against a computer. The main features of this game come from the original game, which was a boardgame. 

Although some features that are different will be the fact users can not choose where their battleships are placed, the computer (python code) chooses this at random. 

Also the users are unable to change the size of the board they are playing on, therefore unable to have a long game of battleship. 

Users are unable to play multiplayer in this version of Battleship. 

I would have preferred to have a multiplayer game. 



