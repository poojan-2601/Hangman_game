# Hangman_game
# HangMan
### Problem Statement
Hangman is a popular word guessing game where the player attempts to build a missing word by guessing one letter at a time. After a certain number of incorrect guesses, the game ends and the player loses. The game also ends if the player correctly identifies all the letters of the missing word.
### About
It is a command line based game developed in java in which player has 5 lives to guess the word.
### Rules of the game

-   Random word is selected from a list of words using API [https://random-word-api.herokuapp.com/word?number=10](https://random-word-api.herokuapp.com/word?number=10)
    
-   The user will get only 5 lives to play the game
    
-   Initially the user is shown “_” (underscore) in the console for each letter in the word. For example, if the word is “banana”, user will see “_ _ _ _ _ _”
    
-   For every correct letter guess, replace the “_” (underscore) with the letter. For example, if user guessed “n”, user will see “_ _ n _ n _”
    
-   If the user guesses the same letter again, don’t do anything and continue with the game. For example, if the user guessed “n” again, show “_ _ n _ n _” and continue.
    
-   For every incorrect guess, reduce the number of lives by 1
    
-   The game ends when the user guesses the word correctly or there are no lives remaining.
### Screen Shots
![Screenshot from 2022-01-08 20-52-35](https://user-images.githubusercontent.com/57809488/148649961-09981b5e-fa00-4392-a4a4-28a24b32b27e.png)
![Screenshot from 2022-01-08 20-53-14](https://user-images.githubusercontent.com/57809488/148649974-93299dad-d249-451a-901d-a65d77f7871c.png)
![Screenshot from 2022-01-08 20-53-43](https://user-images.githubusercontent.com/57809488/148649977-e1e8e99f-b011-4987-b03e-d9a411dc9d2c.png)
![Screenshot from 2022-01-08 20-53-48](https://user-images.githubusercontent.com/57809488/148649980-b402b056-f3e6-41ea-918a-6fca97b36a18.png)
![Screenshot from 2022-01-08 20-53-53](https://user-images.githubusercontent.com/57809488/148649986-13b9dc59-1bb3-40cb-ab1e-be33e86776e1.png)
