# version 1 of the wordle bot
# this one doesn't have proper letter highlighting
# it operates on {'h': 2} dicts, instead of ('h', 'green') pairs
# it doesn't calculate points correctly yet

color_dict = {
    -1: "gray",
    0: "white",
    1: "yellow",
    2: "green"
}

secret = "aloft"
tries = 8

win = False
data = []


keyboard = {char: 0 for char in "qwertyuiopasdfghjklzxcvbnm"}


for attempt in range(tries):
    print(f"Attempt number {attempt + 1}: ")

    guess = ""
    while len(guess) != len(secret):
        guess = input("type a word")


    guess_data = [{char: 0} for char in guess]
    keyboard_before = keyboard.copy()
    secret_temp = list(secret)

    print(secret_temp)


    # well this works, I just have to adjust how the data is collected
    for i in range(len(guess)):
        if guess[i] == secret_temp[i]:  # green
            guess_data[i] = {guess[i]: 2}
            keyboard[guess[i]] = max(keyboard[guess[i]], 2)
            secret_temp[i] = '*'

    print(secret_temp)

    for i in range(len(guess)):
        if guess[i] in secret_temp:  # yellow
            guess_data[i] = {guess[i]: 1}
            keyboard[guess[i]] = max(keyboard[guess[i]], 1)
            secret_temp[secret_temp.index(guess[i])] = '*'


    print(secret_temp)



    keyboard_after = keyboard
    data.append(guess_data)
    print(guess_data)
    print(data)

    print(keyboard_before)
    print(keyboard_after)

    def non_negative(num):
        if num >= 0:
            return True
        return False

    points = sum(filter(non_negative, keyboard_after.values())) - sum(filter(non_negative, keyboard_before.values()))
    print(f"\nPOINTS: {points}\n")

    print(guess)
    print(secret)

    if guess == secret:
        win = True
        break


if win is True:
    print("you won")
else:
    print("rip")
