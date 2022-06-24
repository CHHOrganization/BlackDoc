import os, time, sys
from Plugins.Configs.Settings import *

def Chat_App():

    def Chat_Config():
        Answer = input(Bright_Magenta + "RekcahDA_Bot: "+ Bright_Red + "Do you want to chat? <(Y/N)> ")
        if Answer != Binary_Firewall[0]:
            Answer = input(Bright_Magenta + "RekcahDA_Bot: "+ Bright_Red + "You Use Linux Or Windows? <(L/W)> ")
            if Answer == CD_OS[0]: 
                Linux = "cd Plugins && cd Configs && bash CDir_Config.sh "
                os.system(Linux)
            elif Answer == CD_OS[1]:
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

    def Firewall_CodeBase_Scanner2():
        while True:
            global Nickname
            if Nickname != Firewall_CodeBase[0]:
                Broken_User2()
                if Nickname != Firewall_CodeBase[1]:
                    Broken_User2() 
                    if Nickname != Firewall_CodeBase[2]:
                        Broken_User2()
                        if Nickname != Firewall_CodeBase[3]:
                            Broken_User2()
                            if Nickname != Firewall_CodeBase[4]:
                                Broken_User2()
                                if Nickname != Firewall_CodeBase[5]:
                                    Broken_User2()
                                    if Nickname != Firewall_CodeBase[6]:
                                        Broken_User2()
                                        if Nickname != Firewall_CodeBase[7]:
                                            Broken_User2()
                                            if Nickname != Firewall_CodeBase[8]:
                                                Broken_User2()
                                                if Nickname != Firewall_CodeBase[9]:
                                                    Broken_User2()
                                                    if Nickname != Firewall_CodeBase[10]:
                                                        Broken_User2()
                                                        if Nickname != Firewall_CodeBase[11]:
                                                            Broken_User2()
                                                            if Nickname != Firewall_CodeBase[12]:
                                                                Broken_User2()
                                                                if Nickname != Firewall_CodeBase[13]:
                                                                    Broken_User2()
                                                                    break

                                                                else:
                                                                    Chat_Config()
                                                            else:
                                                                Chat_Config()
                                                        else:
                                                            Chat_Config()
                                                    else:
                                                        Chat_Config()
                                                else:
                                                    Chat_Config()
                                            else:
                                                Chat_Config() 
                                        else:
                                            Chat_Config() 
                                    else:
                                        Chat_Config() 
                                else:
                                    Chat_Config() 
                            else:
                                Chat_Config() 
                        else:
                            Chat_Config() 
                    else:
                        Chat_Config()
                else:
                    Chat_Config() 
            else:
                Chat_Config()

    Firewall_CodeBase_Scanner2()