import random


def main():
    player = 1
    stone = 20
    while stone > 0:
        print("There are " + str(stone) + " stones left")
        amount = int(input("Player " + str(player) + " would you like to remove 1 or 2 stones? "))

        while amount <= 0 or amount > 2:
            amount = int(input("Please enter 1 or 2: "))

        print()
        if amount == 1:
            stone = stone - 1
        elif amount == 2:
            stone = stone - 2
        if player == 1:
            player += 1
        else:
            player -= 1

    print("Player " + str(player) + " wins!")


if __name__ == '__main__':
    main()