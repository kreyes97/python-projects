import random
import time

min = 1
max = 6

answer = input("\nWould you like to roll the dice? Enter Y for yes and N for no.\n").lower()

thinking = ["\nHere goes\n", "\nRolling the dices\n", "\nLet's see what we get\n"]
thinking2 = ["The values are...\n", "We got...\n", "The numbers are...\n"]
idk = ["\nI'm not sure what you mean.", "\nCome again?", "\nI'm sorry, I didn't quite get that."]
more = ["\nWould you like to roll the dice again?\n", "\nWanna see what we'll get again?\n", "\nWanna keep rolling?\n"]
end = ["\nI see. Next time, then!\n", "\nAlright, see you next time!\n", "\nOkay! Come back soon.\n"]



while True:
    if answer == "n":
        print(end[random.randint(0, 2)])
        time.sleep(1)
        break
    elif answer != "y":
        print(idk[random.randint(0, 2)])
        answer = input(more[random.randint(0, 2)])
        continue
    else:
        print(thinking[random.randint(0, 2)])
        print(thinking2[random.randint(0, 2)])
        num1 = (random.randint(min, max))
        num2 = (random.randint(min, max))
        print(f"We got {num1} and {num2}!")
        answer = input(more[random.randint(0, 2)])
        continue
