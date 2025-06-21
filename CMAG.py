import os
import time
import random
import json

#ProgramBy => nico :)

chances = {
    "common": 60,
    "uncommon": 20,
    "rare": 10,
    "legendary": 7,
    "mythical": 2.8,
    "???": 0.2
}

own = True

data = {
    "playername": "",
    "cronium": 100,
    "genox": 5,
    "characters": ["lune"],
    "level": 1,
    "xp": 0
}

cmds = [
    "!start",
    "!step",
    "!Z",
    "!help",
    "!gacha",
    "!gift",
    "!character",
    "!settings",
    "xx",
    ";Z"
]

pre_txt = {
    "leave": [
        "you took a step, ",
        "you took off, ",
        "you ran off, "
    ],
    "mid": [
        "while you were moving, you got ...",
        "while you were wandering, you picked up ...",
    ]
}

if os.path.exists("C19290.json"):
    with open("C19290.json", "r") as f:
        print(f)

def start():
    print("   · - ♦-------♦ - ·")
    print("   |    welcome!   |")
    print("   · - ♦-------♦ - ·")
    print("prepare for an extraordinary\nadventure!")
    print("  · - ♦ COMMANDS ♦ - ·")
    print("    main prefix ['!']")
    print("- prefix used for main/official cmds")
    print("   modded prefix ['?']")
    print("- prefix used for mods")
    awaitcmd()

def awaitcmd():
    global own
    ipt = input(" > ")
    lol = "---------"
    if ipt != "!fmo":
        if ipt not in cmds:
            lol = "---------"
            print("Invalid! "+ipt)
            for txt in range(len(ipt)):
                lol += "^"
            print(lol+"--------")
            print(" is not a command!")
            print(" type '!Z' or '!help' to view all command")
            awaitcmd()
    if ipt == "!fmo":
        if own == True:
            own = False
            print("you are no longer an owner!")
        if own == True:
            own = False
            print("you are now an owner!")
        awaitcmd()
    elif ipt == "!help":
        cmHelp()
    elif ipt == "!Z":
        cmHelp()
    elif ipt == ";Z":
        cmSemZ()
    elif ipt == "xx":
        print("game not saved!")
        exit()
    elif ipt == "!start":
        cmStart()
    elif ipt == "!gacha":
        cmGacha()
    
def cmGacha():
    if data["genox"] >= 1:
        data["genox"] -= 1
        print(f"you have {data['genox']}gn left!✨")
        print("- ♦-------♦ -")
        time.sleep(3)
        print("you took your chances...")
        time.sleep(3)
        print("is it happiness or rage?")
        time.sleep(3)
        print("the roll begins...")
        print("- ♦-------♦ -")
        time.sleep(3)
        print("you got... => ") 
        awaitcmd()
    else:
        print("uh oh! insufficient amount of genox!")

    
def cmHelp():
    print("here's a list of all commands!")
    print("       - ♦-------♦ -")
    for i in range(len(cmds)):
        if cmds[i].startswith("!"):
            print("•- "+cmds[i]+"  <-•")
            print("<>---------------------<>")
        elif cmds[i].startswith("x"):
            print("•- "+cmds[i]+" (warning! commands with 'x'\n are usually unsafe!) <-•")
            print("<>---------------------<>")
        elif cmds[i].startswith(";"):
            if own == False:
                print("•- only the creator is allowed to see this... <-•")
                print("<>---------------------<>")
            if own == True:
                print("•- "+cmds[i]+" (owner cmd) <-•")      
                print("<>---------------------<>")
        time.sleep(0.1)
    awaitcmd()

def cmSemZ():
    if own == True:
        print("welcome... 😎")
        print("<>----------<>")
        time.sleep(3)
        print("this is a secret lair...")
        time.sleep(3)
        print("for non other than the creator")
        time.sleep(3)
        for key in data:
            print(f"{key}: {data[key]}")
    else:
        print("you're so brave...")
    awaitcmd()

def cmStart():
    txt = ""
    txt += random.choice(pre_txt["leave"])
    txt += random.choice(pre_txt["mid"])
    print(txt)
    awaitcmd()
    
start()
