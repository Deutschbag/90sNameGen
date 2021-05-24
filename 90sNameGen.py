import random

first_name = [
    "HOT_",
    "butterfly_",
    "BAD_",
    "Freak_",
    "xXx",
    "SK8R_",
    "deathcab4",
    "xXCORE_",
    "sunshine_",
    "CoolRANCH_"
    "Sporty_",
    "Bucket_Hat_",
    "Lil_",
    "sweetNsour",
    "FASHION_",
    "Goth_",
    "KING_",
    "Nach0_",
    "BeanieBB_",
    "RainBow_",
    "JNC0",
    "Poopie_",
    "Angel",
    "foxy_",
    "I_heart_",
    "Soccer"
]

middle_name = [
    "BRATgrl_",
    "boi_",
    "kitty_",
    "Babeee_",
    "QT_",
    "Emokid_",
    "taco",
    "CHICKA",
    "baby_",
    "daddy",
    "punkGRL",
    "4lyfe_",
    "LOSEr",
    "witch",
    "MoNsTeR",
    "sugah_",
    "LOCO_",
    "hotdog_",
    "CAT_",
    "Queen",
    "raver",
    "rOcKer",
    "cutie_",
    "mama_",
    "Mcgee"
]

last_name = [
    "007",
    "_4EVA",
    "911",
    "FACe33",
    "CHICKA08",
    "420",
    "6969",
    "chic_70",
    "SK8R",
    "2000",
    "16",
    "Xcore",
    "300",
    "D00D",
    "500",
    "xXx",
    "SLAYER99",
    "playah",
    "3000",
    "x3",
    "42069",
    "666",
    "88",
    "BB",
    "50",
    "BOSS"
]


def char_check():
    test = name_gen()
    total = 0
    for i in test:
        total += 1
    if total >= 20:
        print("Username too long!" + "\n" + str(total))
    else:
        print(test + "\n" + str(total))


def name_gen():
    num_of_name = input("Two or Three names? (2/3) ")
    if num_of_name == "2":
        return random.choice(first_name) + random.choice(last_name)
    elif num_of_name == "3":
        return random.choice(first_name) + random.choice(middle_name) + random.choice(last_name)
    else:
        print("error")


pick_name = input("Generate username? (Y/N) ").lower()
while pick_name == "y":
    char_check()
    pick_name = input("Re-pick? (Y/N) ").lower()
else:
    print("Goodbye")
