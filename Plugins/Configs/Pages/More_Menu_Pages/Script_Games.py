import os, time, sys
from Plugins.Configs.Settings import *

def Menu_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "")
    Auto_Text_20 = "Error78; The Selected Menu Is Not Found."
    for char in Auto_Text_20:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)

    print("")
    Auto_Text_21 = "Or you have entered invailed Text!"
    for char in Auto_Text_21:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")    
    print(Bright_Green +"If Menu is Chat, write 'Chat' not 'chat'")
    print("Note: You can use 'Chat' to chat with;")
    print("Mr RekcahDA_Bot!")

def Script_Games():
    Script_Games = "-------BlackDocument Script Games--------"
    print(BG_Bright_Cyan + Bright_Magenta)
    for char in Script_Games:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(Rest + "" + Bright_Green)
    #Script Games
    Print_Games = "[+] -> Games List\n\
Windows & Linux Games;\n\
\n\
I). Hacking Game: EvilNinja\n\
II). Guessing Game: Black WareMoney\n\
<(B.W.M)>"
#End Line Of Games List
    for char in Print_Games:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    print(Bright_Red + "Please Use The Name Of A Game\n\
You Want To Open As It Is...")
    Answer = input(Bright_Cyan + "Which Game You Wanna Play? ")
    if Answer == "EvilNinja":
        Answer = input(Bright_Magenta + "RekcahDA_Bot: "+ Bright_Red + "You Use Linux Or Windows? <(L/W)> ")
        if Answer == CD_OS[0]: 
            Linux = "cd Plugins && cd Configs && bash CDir_Config_Games.sh "
            os.system(Linux)
        elif Answer == CD_OS[1]:
            Windows = "cd Plugins && cd Games && cd EvilNinja && python EvilNinja.py"
            os.system(Windows)
        else:
            print("")
            Auto_Text_129 = "RekcahDA_Bot: Please Use L or W As Your Answer"
            for char in Auto_Text_129:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
            for char in TO_msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
    else:
        Menu_Error()
