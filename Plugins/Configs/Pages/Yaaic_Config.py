import os, time, sys
from Plugins.Configs.Settings import *


def Yaaic_Config():
    clearConsole()
    Index_Banner()
    print(Bright_Yellow +"Yaaic Configurations and Installation")
    answer = input(Bright_Cyan +"Do you to Config or Install? (C/I) ")
    if answer == "C":

        #Configurations Script
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                                    
        CI_Title = "Configurations Instructions;"
        CI_msg = "To Configure Your New Yaaic Installation\n\
Please Follow All of This Steps Below;"
        print(Bright_Yellow + CI_Title)
        print(Bright_Green + CI_msg)

        #First Configure
        print(Bright_Red +"Step "+ Ms1)
        print(Bright_Green +"As a member of CHHOrg we use Yaaic App to\n\
Connect and in order to do so you must\n\
Follow this steps carefully")
        print("Is gonna be a long journey but please\n\
Believe me if I say 'Is Worthy It'")
        print(Bright_Magenta + Ms1 + Bright_Green +". To begin your first step after the\n\
Installation open your App")
        answer = input(Bright_Cyan +"Are You Done? (Y/N) ")
        if answer == Binary_Firewall[1]:

            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            print(Bright_Yellow + CI_Title)
            print(Bright_Green + CI_msg)
            #Second Configure
            print(Bright_Red +"Step "+ Ms2)
            print(Bright_Magenta + Ms1 + Bright_Green +"). As you have opened the App now you\n\
Need to Connect to The organization\n\
Server")
            print(Bright_Magenta + Ms2 + Bright_Green +"). To do so, you need to tap that + Add\n\
Button then on the next windown;")
            print(Bright_Magenta + Ms3 + Bright_Green +"). Fill This In")
            print(Bright_Magenta + Ms4 + Bright_Green +"). Title: The Organization")
            print(Bright_Magenta + Ms5 + Bright_Green +"). Host: irc.anonops.com")
            print(Bright_Magenta + Ms6 + Bright_Green +"). Port: 6697")
            print(Bright_Magenta + Ms7 + Bright_Green +"). Now enter your own password you\n\
Will remember.")
            print(Bright_Magenta + Ms8 + Bright_Green +"). Then Tick 'Use SSL'")
            print(Bright_Magenta + Ms9 + Bright_Green +"). Here goes your membership alone\n\
With your iD, e.g RekcahHC_XXXIV")
            print(Bright_Magenta + Ms10 + Bright_Green +"). On ALIASES just use one of your\n\
Hackers name as a real name...")
            print(Bright_Red +"Note: We don't Allow anyone to use their\n\
Real Details in this registration!")
            print(Bright_Magenta + Ms11 + Bright_Green +"). Then Tap 'Authentication'")
            print(Bright_Magenta + Ms12 + Bright_Green +"). On the next screen Tick\n\
Authenticate with Nickserv'")
            print(Bright_Magenta + Ms13 + Bright_Green +"). Then enter the same password you\n\
Used earlier in this configurations")
            print(Bright_Magenta + Ms14 + Bright_Green +"). Tap 'Ok'")
            print(Bright_Magenta + Ms15 + Bright_Green +"). On the next screent Tap 'Channels'")
            print(Bright_Magenta + Ms16 + Bright_Green +"). Then All type 'darkdoor' it will\n\
Look like this '#darkdoor'")
            print(Bright_Magenta + Ms17 + Bright_Green +"). Tap 'Add'")
            print(Bright_Magenta + Ms18 + Bright_Green +"). Then add the last channel\n\
'chhorg' it will look like this '#chhorg'")
            print(Bright_Magenta + Ms19 + Bright_Green +"). Tap 'ok'")
            print(Bright_Magenta + Ms20 + Bright_Green +"). On the next screen Tap 'Commands'")
            print(Bright_Magenta + Ms21 + Bright_Green +"). Then add this command;\n\
/msg NickServ IDENTIFY ****** ")
            print(Bright_Red +"Note: '******' Must Be Replaced By Your\n\
Password You Used In Yaaic App...") 
            print("your Password must match all 3 of them!")
            print(Bright_Magenta + Ms22 + Bright_Green +"). Tap 'Add' and 'ok'")
            print(Bright_Magenta + Ms23 + Bright_Green +"). Then Tap 'Save'")
            answer = input(Bright_Cyan +"Are You Done? (Y/N) ")
            if answer == "Y" or answer == "y":

                print(Dark_Blue + BG_Dark_Green + Line + Rest)
                print(Dark_Blue + BG_Dark_Green + Line + Rest)

                #Third Configurations
                print(Bright_Yellow + CI_Title)
                print(Bright_Green + CI_msg)
                print("Lastly....")
                print(Bright_Red +"Step "+ Ms3)
                print(Bright_Magenta + Ms1 + Bright_Green +"). Now that you done with the big")
                print("configuration let's register you in the\n\
Network")
                print(Bright_Magenta + Ms2 + Bright_Green +"). Tap 'The Organization Server to turn your online light green")
                print(Bright_Magenta + Ms3 + Bright_Green +"). After it connect you to our network")
                print(Bright_Red +"Note: You will see an error message that\n\
You cant create #darkdoor and #chhorg\n\
Channels")
                print(Bright_Magenta + Ms4 + Bright_Green +"). You will need to wait 180 sec to be\n\
Able to register so for now lets try to\n\
Add a channel that will keep you busy.")
                print(Bright_Magenta + Ms5 + Bright_Green +"). Tap the + button then type 'anonops'\n\
It will look like this '#anonops'")
                print(Bright_Magenta + Ms6 + Bright_Green +"). After 180 sec then go back to the\n\
Organization Channel")
                print(Bright_Magenta + Ms7 + Bright_Green +"). Then type this command below")
                print(Bright_Magenta + Ms8 + Bright_Green +"). /msg NickServ REGISTER ******") 
                print("info@chhorg.net")
                print(Bright_Red +"Note: Those '*****' Must Be Replaced By\n\
Your Password You Used In yaaic App...")
                print("your password must match to all 4")
                print("passwords you have entered now")
                print("You must then see a nickserv registered\n\
Notification, if you need help chat at")
                print("t.me/cryptichatshackers")

                answer = input(Bright_Cyan +"Did you get a nickserv registered? (Y/N) ")
                if answer == "Y" or answer == "y":

                    print(Dark_Blue + BG_Dark_Green + Line + Rest)
                    print(Dark_Blue + BG_Dark_Green + Line + Rest)

                    #Fourth Configure Script
                    print(Bright_Yellow + CI_Title)
                    print(Bright_Green + CI_msg)
                    print("Congradulations You Made It....")
                    print(Bright_Red +"Step "+ Ms4)
                    print(Bright_Magenta + Ms1 + Bright_Green +"). Now tap those '"+ Ms3 +" dots' at the top\n\
Right")
                    print(Bright_Magenta + Ms2 + Bright_Green +"). Tap 'Disconnect'")
                    print(Bright_Magenta + Ms3 + Bright_Green +"). Then Connect again")
                    print(Bright_Magenta + Ms4 + Bright_Green +"). If you get #darkdoor and #chhorg\n\
Channels error messages just inbox us at\n\
t.me/cryptichatshackers")
                                            
                    #Logout Config
                    print(Bright_Red + "")
                    for char in Logout_msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.5)
                    print("")
                    Logout = input(BG_Dark_Red + Bright_Black +"Logout? <(Y/N)> ")
                    if Logout == "N":
                        print(Rest + Bright_Green + "")
                        for char in MT_msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)

                        print("" + Bright_Yellow + BG_Dark_Cyan)
                        for char in Empty:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.5)
                            print(""+ Rest)

                        Moretime = input(BG_Dark_Red + Bright_Black +"Are You Done Yet? <(Y/N)> ")
                        print(Rest + Bright_Red + "")
                        if Moretime == "N":
                            for char in MT_msg2:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)

                        elif Moretime == "Chat":
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

                        else:
                            print(Rest +""+ Bright_Red +"The End...")
                            print("")
                            for char in TO_msg:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.1)

                    elif Logout == "Chat":
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

                    else:
                        print("")
                        print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
                        for char in TO_msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.3)
                elif Answer == "Chat":
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

                else:
                    print(Bright_Red +"You Slow Bye!")
                    print(quit())
                                            
                    #End Part
            elif Answer == "Chat":
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

            else:
                print(Dark_Blue + BG_Dark_Green + Line + Rest)
                print(Dark_Blue + BG_Dark_Green + Line + Rest)

                print(Bright_Yellow + CI_Title)
                print(Bright_Green + CI_msg)
                #Second Configure !Repeat
                print(Bright_Red +"Step "+ Ms2)
                print(Bright_Magenta + Ms1 + Bright_Green +"). As you have opened the App now you    need to Connect to The organization    Server")
                print(Bright_Magenta + Ms2 + Bright_Green +"). To do so, you need to tap that + Add button then on the nest windown;")
                print(Bright_Magenta + Ms3 + Bright_Green +"). Fill This In")
                print(Bright_Magenta + Ms4 + Bright_Green +"). Title: The Organization")
                print(Bright_Magenta + Ms5 + Bright_Green +"). Host: irc.anonops.com")
                print(Bright_Magenta + Ms6 + Bright_Green +"). Port: 6697")
                print(Bright_Magenta + Ms7 + Bright_Green +"). Now enter your own password you will remember.")
                print(Bright_Magenta + Ms8 + Bright_Green +"). Then Tick 'Use SSL'")
                print(Bright_Magenta + Ms9 + Bright_Green +"). Here goes your membership alone with your iD, e.g RekcahHC_XXXIv")
                print(Bright_Magenta + Ms10 + Bright_Green +"). On ALIASES just use one of your hackers name as a real name...")
                print(Bright_Red +"Note: We don't Allow anyone to use their real Details in this registration")
                print(Bright_Magenta + Ms11 + Bright_Green +"). Then Tap Authentication")
                print(Bright_Magenta + Ms12 + Bright_Green +"). On the next screen Tick 'Authenticate with Nickserv'")
                print(Bright_Magenta + Ms13 + Bright_Green +"). Then enter the same password you\n\
Used earlier in this configurations")
                print(Bright_Magenta + Ms14 + Bright_Green +"). Tap 'Ok'")
                print(Bright_Magenta + Ms15 + Bright_Green +"). On the next screent Tap 'Channels'")
                print(Bright_Magenta + Ms16 + Bright_Green +"). Then All type 'darkdoor' it will    look like this '#darkdoor'")
                print(Bright_Magenta + Ms17 + Bright_Green +"). Tap 'Add'")
                print(Bright_Magenta + Ms18 + Bright_Green +"). Then add the last channel 'chhorg' it will look like this '#chhorg'")
                print(Bright_Magenta + Ms19 + Bright_Green +"). Tap 'ok'")
                print(Bright_Magenta + Ms20 + Bright_Green +"). On the next screen Tap 'Commands'")
                print(Bright_Magenta + Ms21 + Bright_Green +"). Then add this command; /msg NickServ IDENTIFY ****** ")
                print(Bright_Red +"Note: '******' Must Be Replaced By Your Password You Used In Yaaic App... your\n\
Password must match all 3 of them!")
                print(Bright_Magenta + Ms22 + Bright_Green +"). Tap 'Add' and 'ok'")
                print(Bright_Magenta + Ms23 + Bright_Green +"). Then Tap 'Save'")
                answer = input(BG_Bright_Cyan +"Are You Done? (Y/N) ")
                if answer == "Y":
                    print(Dark_Blue + BG_Dark_Green + Line + Rest)
                    print(Dark_Blue + BG_Dark_Green + Line + Rest)
                                                
                    print(Dark_Blue + BG_Dark_Green + Line + Rest)
                    print(Dark_Blue + BG_Dark_Green + Line + Rest)

                    #Third Configurations
                    print(Bright_Yellow + CI_Title)
                    print(Bright_Green + CI_msg)
                    print("Lastly....")
                    print(Bright_Red +"Step "+ Ms3)
                    print(Bright_Magenta + Ms1 + Bright_Green +"). Now that you done with the big")
                    print("configuration let's register you in the network")
                    print(Bright_Magenta + Ms2 + Bright_Green +"). Tap 'The Organization Server to turn your online light green")
                    print(Bright_Magenta + Ms3 + Bright_Green +"). After it connect you to our network;")
                    print(Bright_Red +"Note: You will see an error message that you cant create #darkdoor and #chhorg\n\
Channels")
                    print(Bright_Magenta + Ms4 + Bright_Green +"). You will need to wait 180 sec to be\n\
Able to register so for now lets try to\n\
Add a channel that will keep you busy.")
                    print(Bright_Magenta + Ms5 + Bright_Green +"). Tap the + button then type 'anonops'\n\
It will look like this '#anonops'")
                    print(Bright_Magenta + Ms6 + Bright_Green +"). After 180 sec then go back to the\n\
Organization Channel")
                    print(Bright_Magenta + Ms7 + Bright_Green +"). Then type this command below")
                    print(Bright_Magenta + Ms8 + Bright_Green +"). /msg NickServ REGISTER ******") 
                    print("info@chhorg.net")
                    print(Bright_Red +"Note: Those '*****' Must Be Replaced By\n\
Your Password You Used In yaaic App...")
                    print("your password must match to all 4")
                    print("passwords you have entered now")
                    print("You must then see a nickserv registered\n\
Notification, if you need help chat at")
                    print("t.me/cryptichatshackers")
                    answer = input(Bright_Cyan +"Did you get a nickserv registered? (Y/N) ")
                    if answer == "Y":

                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)

                        #Fourth Configure Script
                        print(Bright_Yellow + CI_Title)
                        print(Bright_Green + CI_msg)
                        print("Congradulations You Made It....")
                        print(Bright_Red +"Step "+ Ms4)
                        print(Bright_Magenta + Ms1 + Bright_Green +"). Now tap those '"+ Ms3 +" dots' at the top   right")
                        print(Bright_Magenta + Ms2 + Bright_Green +"). Tap 'Disconnect'")
                        print(Bright_Magenta + Ms3 + Bright_Green +"). Then Connect again")
                        print(Bright_Magenta + Ms4 + Bright_Green +"). If you get #darkdoor and #chhorg     Channels error messages just inbox us at  t.me/cryptichatshackers")
                                                
                    elif answer == "Chat":
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

                    else:
                        print(Bright_Red +"You Slow Bye!")
                        print(quit())

                elif answer == "Chat":
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

                else:
                    print(Bright_Red +"You Slow Bye!")
                    print(quit())

        #End Of Second Configurations   
        elif answer == "Chat":
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

        else:
            #Configurations Script !Repeat
            print("Configurations Instructions;")
            print("To Configure Your New Yaaic Installation Please Follow All of This Steps Below;")
            print("Step "+ Ms1)
            print("As a member of CHHOrg we use Yaaic App to connect and in order to do so you must follow this step carefully")
            print("Is gonna be a long journey but please believe me if I say 'Is Worthy It'")
            print("1. To begin your first step after the installation open your App")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            answer = input("Are You Done? (Y/N) ")
            if answer == "Y":
                print(Dark_Blue + BG_Dark_Green + Line + Rest)
                print(Dark_Blue + BG_Dark_Green + Line + Rest)

                print(Bright_Yellow + CI_Title)
                print(Bright_Green + CI_msg)
                #Second Configure
                print(Bright_Red +"Step "+ Ms2)
                print(Bright_Magenta + Ms1 + Bright_Green +"). As you have opened the App now you    need to Connect to The organization    Server")
                print(Bright_Magenta + Ms2 + Bright_Green +"). To do so, you need to tap that + Add button then on the nest windown;")
                print(Bright_Magenta + Ms3 + Bright_Green +"). Fill This In")
                print(Bright_Magenta + Ms4 + Bright_Green +"). Title: The Organization")
                print(Bright_Magenta + Ms5 + Bright_Green +"). Host: irc.anonops.com")
                print(Bright_Magenta + Ms6 + Bright_Green +"). Port: 6697")
                print(Bright_Magenta + Ms7 + Bright_Green +"). Now enter your own password you will remember.")
                print(Bright_Magenta + Ms8 + Bright_Green +"). Then Tick 'Use SSL'")
                print(Bright_Magenta + Ms9 + Bright_Green +"). Here goes your membership alone with your iD, e.g RekcahHC_XXXIv")
                print(Bright_Magenta + Ms10 + Bright_Green +"). On ALIASES just use one of your hackers name as a real name...")
                print(Bright_Red +"Note: We don't Allow anyone to use their real Details in this registration")
                print(Bright_Magenta + Ms11 + Bright_Green +"). Then Tap Authentication")
                print(Bright_Magenta + Ms12 + Bright_Green +"). On the next screen Tick 'Authenticate with Nickserv'")
                print(Bright_Magenta + Ms13 + Bright_Green +"). Then enter the same password you   used earlier in this configurations")
                print(Bright_Magenta + Ms14 + Bright_Green +"). Tap 'Ok'")
                print(Bright_Magenta + Ms15 + Bright_Green +"). On the next screent Tap 'Channels'")
                print(Bright_Magenta + Ms16 + Bright_Green +"). Then All type 'darkdoor' it will    look like this '#darkdoor'")
                print(Bright_Magenta + Ms17 + Bright_Green +"). Tap 'Add'")
                print(Bright_Magenta + Ms18 + Bright_Green +"). Then add the last channel 'chhorg' it will look like this '#chhorg'")
                print(Bright_Magenta + Ms19 + Bright_Green +"). Tap 'ok'")
                print(Bright_Magenta + Ms20 + Bright_Green +"). On the next screen Tap 'Commands'")
                print(Bright_Magenta + Ms21 + Bright_Green +"). Then add this command; /msg NickServ IDENTIFY ****** ")
                print(Bright_Red +"Note: '******' Must Be Replaced By Your Password You Used In Yaaic App... your  Password must match all 3 of them!")
                print(Bright_Magenta + Ms22 + Bright_Green +"). Tap 'Add' and 'ok'")
                print(Bright_Magenta + Ms23 + Bright_Green +"). Then Tap 'Save'")
                answer = input(BG_Bright_Cyan +"Are You Done? (Y/N) ")
                if answer == "Y":

                    print(Dark_Blue + BG_Dark_Green + Line + Rest)
                    print(Dark_Blue + BG_Dark_Green + Line + Rest)

                    #Third Configurations
                    print(Bright_Yellow + CI_Title)
                    print(Bright_Green + CI_msg)
                    print("Lastly....")
                    print(Bright_Red +"Step "+ Ms3)
                    print(Bright_Magenta + Ms1 + Bright_Green +"). Now that you done with the big")
                    print("configuration let's register you in the network")
                    print(Bright_Magenta + Ms2 + Bright_Green +"). Tap 'The Organization Server to turn your online light green")
                    print(Bright_Magenta + Ms3 + Bright_Green +"). After it connect you to our network;")
                    print(Bright_Red +"Note: You will see an error message that you cant create #darkdoor and #chhorg    channels")
                    print(Bright_Magenta + Ms4 + Bright_Green +"). You will need to wait 180 sec to be  able to register so for now lets try to  add a channel that will keep you busy.")
                    print(Bright_Magenta + Ms5 + Bright_Green +"). Tap the + button then type 'anonops'  it will look like this '#anonops'")
                    print(Bright_Magenta + Ms6 + Bright_Green +"). After 180 sec then go back to the    Organization Channel")
                    print(Bright_Magenta + Ms7 + Bright_Green +"). Then type this command below")
                    print(Bright_Magenta + Ms8 + Bright_Green +"). /msg NickServ REGISTER ******") 
                    print("info@chhorg.net")
                    print(Bright_Red +"Note: Those '*****' Must Be Replaced By  Your Password You Used In yaaic App...")
                    print("your password must match to all 4")
                    print("passwords you have entered now")
                    print("You must then see a nickserv registered  notification, if you need help chat at")
                    print("t.me/cryptichatshackers")

                    answer = input(Bright_Cyan +"Did you get a nickserv registered? (Y/N) ")
                    if answer == "Y":

                        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                        print(Dark_Blue + BG_Dark_Green + Line + Rest)

                        #Fourth Configure Script
                        print(Bright_Yellow + CI_Title)
                        print(Bright_Green + CI_msg)
                        print("Congradulations You Made It....")
                        print(Bright_Red +"Step "+ Ms4)
                        print(Bright_Magenta + Ms1 + Bright_Green +"). Now tap those '"+ Ms3 +" dots' at the top   right")
                        print(Bright_Magenta + Ms2 + Bright_Green +"). Tap 'Disconnect'")
                        print(Bright_Magenta + Ms3 + Bright_Green +"). Then Connect again")
                        print(Bright_Magenta + Ms4 + Bright_Green +"). If you get #darkdoor and #chhorg     Channels error messages just inbox us at  t.me/cryptichatshackers")
                                                
                    elif answer == "Chat":
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

                    else:
                        print(Bright_Red +"You Slow Bye!")
                        print(quit())
                                            
                    #End Part
                elif answer == "Chat":
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

                else:
                    print(Bright_Red +"You Slow Bye!")
                    print(quit())   
            else:
                print(Bright_Red +"You Slow Bye!")
                print(quit()) 
    elif answer == "Chat":
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

    else:
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
                                
        clearConsole()
        #Installation Configurations
        #Banner
        Index_Banner()
        print(Bright_Yellow +"Yaaic App Installation")
        print(Bright_Red +"Please download Yaaic at google playstore or download the app directly")
        print("Link: https://www.bit.ly/chhorg-yaaic-app")
        print("Note: We recommand the above Link.")
        print("Thank You For Using BlackDoc")

        #Logout Config
        print(Bright_Red + "")
        for char in Logout_msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.5)
        print("")
        Logout = input(BG_Dark_Red + Bright_Black +"Logout? <(Y/N)> ")
        if Logout == "N":
            print(Rest + Bright_Green + "")
            for char in MT_msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            print("" + Bright_Yellow + BG_Dark_Cyan)
            for char in Empty:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            print(""+ Rest)

            Moretime = input(BG_Dark_Red + Bright_Black +"Are You Done Yet? <(Y/N)> ")
            print(Rest + Bright_Red + "")
            if Moretime == "N":
                for char in MT_msg2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

            elif Moretime == "Chat":
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

            else:
                print(Rest +""+ Bright_Red +"The End...")
                print("")
                for char in TO_msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)

        elif Logout == "Chat":
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

        else:
            print("")
            print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
            for char in TO_msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)