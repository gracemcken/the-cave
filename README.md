![cave_banner](readme_docs/the_cave_banner.png)

![Last commit](https://img.shields.io/github/last-commit/gracemcken/the-cave) 
![Languages used](https://img.shields.io/github/languages/count/gracemcken/the-cave)
![Top Language used](https://img.shields.io/github/languages/top/gracemcken/the-cave)


# Table of Contents

- [Table of Contents](#table-of-contents)
- [Site Overview](#site-overview)
  - [Goal](#goal)
  - [Technologies used](#technologies-used)
- [UX](#ux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Design](#design)
- [Testing](#testing)
  - [Bugs](#bugs)
  - [Known Issues](#known-issues)
- [Deployment](#deployment)
  - [How to Fork](#how-to-fork)
- [Credits](#credits)
  - [Code](#code)
    - [Version Control](#version-control)
- [Acknowledgments](#acknowledgments)
   
  - [Future Features](#future-features)
- [Table of Contents](#table-of-contents)
- [Site Overview](#site-overview)
  - [Goal](#goal)
  - [Technologies used](#technologies-used)
- [UX](#ux)
  - [Target Audience](#target-audience)
  - [User Stories](#user-stories)
- [Features](#features)
  - [Existing Features](#existing-features)
  - [Future Features](#future-features)
- [Design](#design)
- [Testing](#testing)
  - [Bugs](#bugs)
  - [Known Issues](#known-issues)
- [Deployment](#deployment)
  - [How to Fork](#how-to-fork)
- [Credits](#credits)
  - [Code](#code)
    - [Version Control](#version-control)
- [Acknowledgments](#acknowledgments)


# Site Overview
The Cave is a text adventure RPG game where the player choses their race, class and preferred weapon. These initial decisions impact the player's stats in-game and whether or not they will be able to escape the cave alive! Decisions that impact the game are stored in Google Sheets and are retrieved when relevant to the game.

## Goal
I wanted to create a text based adventure game based on the "Choose your own adventure" books I used to read as a child, while also incorporating some Dungeons & Dragons elements to the game. My goal was to create something that has been done before but with an added twist of your decisions actually impacting whether or not luck will be on your side.

<hr>

## Technologies used

- [Python](https://www.python.org/) for the main game-play.
- [GitHub](https://github.com/) as a remote repository.
- [Heroku](https://heroku.com) to deploy the website.
- [Visual Studio Code](https://code.visualstudio.com/) as a local IDE & repository.
- [diagram.net](https://diagram.net) for making the flowchart for the game.

# UX
## Target Audience

- Old school RPGers who would have played choose your own adventure novels in their youth
- People who are fans of Dungeons and Dragons
- Those who enjoy basic text adventure games
- Those who enjoy interactive novels
## User Stories

- As a user:

# Features

## Existing Features



## Future Features


# Design
Below is the flowchart I made to follow along while coding. I initially wrote this out on paper and then used [diagrams.net](https://www.diagrams.net/) to create it digitally.
![flowchart](readme_docs/flowchart.png)

<hr>

# Testing
Testing document can be found [here](TESTING.md)
## Bugs

Bug | Status | Fix | Images of bug
----|--------|-----|--------------
Regardless of class chosen, player was only given warrior options for weapons | Resolved | Rather than just use '==' for one class and 'or' for second option, use '==' for both classes. | ![class-bug](readme_docs/bug_screenshots/class_bug.png)
Large gap between line breaks instead of starting on new line | Resolved | Instead of using 'backslash', started new string. | ![gap-bug](readme_docs/bug_screenshots/gap_bug.png)
Health points were not being updated after player suffers HP loss | Resolved | I had forgotten to add .value to the statement. | ![hp-bug](readme_docs/bug_screenshots/hp_bug.png)
Using if statements in main file caused the failure function to trigger and prevented HP from updating | Resolved | Placed update hp function in events.py in failure function | ![placement-bug](readme_docs/bug_screenshots/placement_bug.png)
Dagger would not upload to sheet and caused UnboundLocalError | Resolved | I only assigned the worksheet variable in one of the if statements rather than all of them. I fixed this by adding it to each if statement | ![var_bug](readme_docs/bug_screenshots/var_bug.png)
## Known Issues



# Deployment 


## How to Fork
1. Login/signup to [GitHub](https://github.com/).
2. Locate the relevant repository - in this case [gracemcken/the-cave](https://github.com/gracemcken/the-cave)
3. Click on the 'Fork' button in the upper left.
4. Your forked version of this repo will be generated!
# Credits
## Code
- fprint and some game logic ideas were sourced from [Elijah Henderson](https://github.com/elijah-henderson) and his youtube tutorials.


<hr>

### Version Control
*   Git was used as the version control software. Commands such as git add ., git status, git commit and git push were used to add, save, stage and push the code to the GitHub repository where the source code is stored.



# Acknowledgments



