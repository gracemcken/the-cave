![amiresponsive](readme_docs/amiresponsive.png)
# Table of Contents
- [Table of Contents](#table-of-contents)
  - [Manual Testing](#manual-testing)
    - [Features](#features)
    - [Errors](#errors)
  - [Validator](#validator)


## Manual Testing
Manual testing was done on a MacBook Pro 2015 13in, running Mojave version 10.14.6 in Google Chrome.

### Features

Feature Tested | Expected Result | Actual Result | Pass/Fail
---------------|-----------------|---------------|----------
Press 'enter' on intro screen | Receive message "The game will now begin" and the next stage should trigger | As expected | Pass
Type a name into terminal when prompted | Receive message "Hello {name}. Welcome to the Cave." | As expected | Pass
Pick a race from the options | Receive message "Nice to meet you, {race}. You are the first {race} to be seen here in a long time. Please, give me one moment to prepare your tale." | As expected | Pass
Pick a class from the options | Receive message "Ah, a {player_class}." | As expected | Pass
Pick weapon from the options | Receive message "The mighty {weapon}, of course... of course." | As expected | Pass
Player name, race, class and weapon upload to spreadsheet and stats alter | Should be visible on spreadsheet and stats should be updated depending on player choices | As expected | Pass
Player picks exit game option | Receive message "You close your eyes and fall asleep. The game is over. You will never know what could have been. Want to start again? Please type yes or no." | As expected | Pass
Player types yes during exit game | Restart game at enter name stage | As expected | Pass
Player types no during exit game | Receive message "GAME OVER. THANK YOU FOR PLAYING." | As expected | Pass
Player type option number during decisions | Should progress to next stage | As expected | Pass
Game checks google sheet if certain items are in inventory | Should trigger specific events | As expected | Pass
Player wins game | Give option to play again | As expected | Pass
Player chooses to play again after winning | Restart at name section | As expected | Pass
Player chooses not to play again after winning | Receive message "Thank you again for playing!" | As expected | Pass
Player dies | Receive message "YOU HAVE DIED. GAME OVER" and option to play again | As expected | Pass
Player chooses to play again after losing | Restart at name section | As expected | Pass
Player chooses not to play again after losing | Receive message "Thank you for playing!" | As expected | Pass

### Errors

Error Tested | Expected Result | Actual Result | Pass/Fail
-------------|-----------------|---------------|----------
Press something before 'enter' on intro screen | Receive message ""You typed '{input}'. The game will not start yet." and should remain on intro screen | As expected | Pass
Type something other than letters when asked for name | Receive message "Please enter letters only." | As expected | Pass
Type something other than races listed or with capital letters | Receive message "Please type one of the races listed and ensure to use lowercase." | As expected | Pass
Type something other than class listed or with capital letters | Receive message "Please type one of the classes listed and ensure to use lowercase." | As expected | Pass
Type something other than weapons listed or with capital letters | Receive message "Please type one of the weapons listed and ensure to use lowercase. | As expected | Pass
Type something other than yes/Yes or no/No during exit game | Receive message "Please type either yes/Yes or no/No" | As expected | Pass
Type something other than 1, 2 or 3 during decision stages | Receive message "Please type either '1', '2', or '3'." | As expected | Pass
Type something other than 1 or 2 during option to play again after winning | Receive message "Please type either '1', or '2'." | As expected | Pass
Type something other than 1 or 2 during option to play again losing| Receive message "Please type either '1', or '2'." | As expected | Pass

## Validator

Due to PEP8 being down, this project was validated by installing pycodestyle and enabling it as the Python linter. At the time of writing, there are no errors appearing and so it passes.