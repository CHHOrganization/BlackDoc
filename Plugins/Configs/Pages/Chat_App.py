import os, time, sys
from Plugins.Configs.Settings import *

def Chat_App():
    Answer = input(Bright_Magenta + "RekcahDA_Bot: "+ Bright_Red + "Do you want to chat? <(Y/N)> ")
    if Answer !="N":
        Answer = input(Bright_Magenta + "RekcahDA_Bot: "+ Bright_Red + "You Use Linux Or Windows? <(L/W)> ")
        if Answer == "L": 
            Linux = "cd Plugins && cd Configs && bash CDir_Config.sh "
            os.system(Linux)
        elif Answer == "W":
            Windows = "cd Plugins && cd RekcahDA_Bot && python Chat.py"
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
        print(Bright_Magenta + "RekcahDA_Bot: "+ Bright_Red +"Thank You For Your Time.")
