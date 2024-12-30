# *Snake Water Gun Game*
*In this game, the user plays against the the computer, and the computer's choice is randomly chosen from the <code>choices</code> list.*

## *How It Works*
1. ***Rules***:
     * *Snake drinks Water ---> Snake wins.*
     * *Water douses Gun ---> Water wins.*
     * *Gun shoots Snake ---> Gun wins.*
1. ***User Input***: *The user is prompted to enter their choice (snake, water or gun).*

1. ***Computer's Choice***: *The computer randomly chooses a choice.*
1. ***Result Calculation***: *The <code>game_result</code> function determines the winner based on the rules.*
1. ***Play Again***: *The game continues in a loop until the user types <code>quit</code> or the user exits the program.*

### *Example Run:*
```python
Welcome to the Snake-Water-Gun Game!
Rules: Snake beats Water, Water beats Gun, Gun beats Snake.
Enter your choice (snake/water/gun or 'quit' to exit): snake
Computer chose: gun
You lose!

Enter your choice (snake/water/gun or 'quit' to exit): water
Computer chose: gun
You win!

Enter your choice (snake/water/gun or 'quit' to exit): quit
Thanks for playing!
```