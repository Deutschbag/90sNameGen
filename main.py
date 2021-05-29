import random
from dict_names import first_name, middle_name, last_name


def name_gen():
    num_of_name = random.randint(1, 3)
    if num_of_name == 1:
        return random.choice(first_name)
    elif num_of_name == 2:
        return random.choice(first_name) + random.choice(last_name)
    elif num_of_name == 3:
        return random.choice(first_name) + random.choice(middle_name) + random.choice(last_name)


pick_name = input("Generate username? (Y/N) ").lower()
while pick_name == "y":
    name = name_gen()
    if len(name) >= 20:
        continue
    else:
        print(name)

    pick_name = input("Re-pick? (Y/N) ").lower()
else:
    print("Goodbye")
