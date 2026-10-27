## Treasure Island

'''**Uses:** `input()`, nested `if`/`else`

A "choose your own adventure" text game. At each step, ask the player a
question (e.g. "left or right?") and use `if`/`else` — nested where a
choice only makes sense after an earlier one — to branch the story
towards different endings ("you found the treasure" / "you got eaten by
a dragon" / ...). Plan the branches on paper first before writing the
`if`s.

*Adapted from: 100 Days of Code, Day 3.*'''
print("Welcome to Treasure Island")

choice = input("Left or Right? ")

if choice.lower() == "left":
    action = input("Swim or Wait? ")

    if action.lower() == "wait":
        door = input("Red, Blue or Yellow door? ")

        if door.lower() == "yellow":
            print("You found the treasure! You win!")
        elif door.lower() == "red":
            print("Burned by fire. Game Over.")
        elif door.lower() == "blue":
            print("Eaten by beasts. Game Over.")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
else:
    print("You fell into a hole. Game Over.")

    

