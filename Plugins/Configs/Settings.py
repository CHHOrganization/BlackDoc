import os, time, sys
from Plugins.Configs.FireWall.Evil_TwiNinja import *
#Banner Data
B1 = "-----------------------------------------"
B2 = "-----------------------------------------"
B3 = "--- Cryptic Hats Hackers Organization ---"
B4 = "---         BlackDoc V0.0.05          ---"
B5 = "---       SAFWAL Level: 1.0.5+        ---"
B6 = "-----------------------------------------"
B7 = "-----------------------------------------"
Banner_msg = "Follow Us At Telegram To Stay Upto Date."
Line = "*****************************************"
Endl = "     100% BlackDoc Is Done Loading       "
Status_On = "Preminum Member"
Status_Off = "Unrecognized Member"

#Banner Data
FWB1 = "-----------------------------------------"
FWB2 = "-----------------------------------------"
FWB3 = "--- Cryptic Hats Hackers Organization ---"
FWB4 = "---         BlackDoc V0.0.05          ---"
FWB5 = "---       SAFWAL Level: 1.0.5+        ---"
FWB6 = "-----------------------------------------"
FWB7 = "-----------------------------------------"
FWBanner_msg = "Use RekORG Codes Details To Gain Access."
FWLine = "*****************************************"
FWEndl = "     100% BlackDoc Is Done Loading       "

#Menu Data
Menu_TB = "_________________________________________"
Menu1 = "||Updates // VPN Files // Yaaic Config ||" 
Menu2 = "||Darkweb Links // Apps // Memberships ||"
Menu3 = "||Hacking Lessons  /+/  Python Lessons ||"
Menu4 = "||PHP Lessons // |Chat| // SQL Lessons ||"
Menu5 = "||HTML Lessons // CSS Lessons // More? ||"
Menu_BB = "||-------------------------------------||"

#More Menu Data
Menu_TB = "_________________________________________"
More_Menu1 = "||Chat Info \ Org History / Org Rules! ||" 
More_Menu2 = "||BlcakDoc Info | Member's Projects.py ||"
More_Menu3 = "||Member's Projects.sh |[Script Games] ||"
More_Menu4 = "||Members List | MyAccount /\ About Us ||"
Menu_TB = "||-------------------------------------||"

Menu_msg = "Please select any of our menu\n\
to open the scripts"

#Colors Codes With Their Given Names
#Bright Text Colors
Dark_Black = "\u001b[30;1m"
Dark_Red = "\u001b[31;1m"
Dark_Green = "\u001b[32;1m"
Dark_Yellow = "\u001b[33;1m"
Dark_Blue = "\u001b[34;1m"
Dark_Magenta = "\u001b[35;1m"
Dark_Cyan = "\u001b[36;1m"
Dark_White = "\u001b[37;1m"

#Dark Text Colors 
Bright_Black = "\u001b[30m"
Bright_Red = "\u001b[31m"
Bright_Green = "\u001b[32m"
Bright_Yellow = "\u001b[33m"
Bright_Blue = "\u001b[34m"
Bright_Magenta = "\u001b[35m"
Bright_Cyan = "\u001b[36m"
Bright_White = "\u001b[37m"

#Bright Background Colors 
BG_Dark_Black = "\u001b[40;1m"
BG_Dark_Red = "\u001b[41;1m"
BG_Dark_Green = "\u001b[42;1m"
BG_Dark_Yellow = "\u001b[43;1m"
BG_Dark_Blue = "\u001b[44;1m"
BG_Dark_Magenta = "\u001b[45;1m"
BG_Dark_Cyan = "\u001b[46;1m"
BG_Dark_White = "\u001b[47;1m"

#Dark Background Colors 
BG_Bright_Black = "\u001b[40m"
BG_Bright_Red = "\u001b[41m"
BG_Bright_Green ="\u001b[42m"
BG_Bright_Yellow = "\u001b[43m"
BG_Bright_Blue = "\u001b[44m"
BG_Bright_Magenta = "\u001b[45m"
BG_Bright_Cyan = "\u001b[46m"
BG_Bright_White = "\u001b[47m"

#Rest Color
Rest = "\u001b[0m"


#Application Welcome Messages
Title = "Cryptic Hats Hackers Organization"
Header = "Welcome To CHH.Org BlackDocument Script"
Main_msg = "Note; This script is only for all"
Main_msg2 = "Preminum Members of the Org!"
Main_msg_discription = "This script is created to update members \n\
about The Org and BlackDoc is also our\n\
way to teach our members IT Fundamentals.\n\
\n\
This Scritp Must Not Be Copyrighted \n\
Or Shared To None 'Preminum Members'\n\
Or You Might Lose Your Membership!."
Main_msg_disc = "As DarkDoor is offline you may use this"
Main_msg_disc2 = "script to Chat with; \n\
'Mr RekcahDA_Bot' by typing Chat!"

Main_msg_disc3 = "'By the Offline DarkDoor we talk about\n\
the website.'\n\
\n\
Note: If Mr Bot Can't Assist You\n\
Please Connect To Your Yaaic App.\n\
If you are a new member please see\n\
the Menu on how to Install it and\n\
how to Configure it after da \n\
Installation."

Unlocked_Version_msg = "BlackDoc Is a  Cryptic Hats Hackers\n\
Organization Script to teach IT\n\
Fundamentals For Free. This Script\n\
Must not be misused and everything\n\
You learn in there must stay between\n\
You and your heart as we are not \n\
Responsable about any misuse of our\n\
Teachings cause we Teach Ethical hacking\n\
What you do with the skills you will\n\
Otain with us, is your own benefit and\n\
Study at your own knowledge of risk you\n\
Might obtain in real acts.\n\
If you practice!!!"
Membership = "RekcahHC_"
#Membership Numbers Data
Ms1 = "I"
Ms2 = "II"
Ms3 = "III"
Ms4 = "IV"
Ms5 = "V"
Ms6 = "VI"
Ms7 = "VII"
Ms8 = "VIII"
Ms9 = "IX"
Ms10 = "X"
Ms11 = "XI"
Ms12 = "XII"
Ms13 = "XIII"
Ms14 = "XIV"
Ms15 = "XV"
Ms16 = "XVI"
Ms17 = "XVII"
Ms18 = "XVIII"
Ms19 = "IXX"
Ms20 = "XX"
Ms21 = "XXI"
Ms22 = "XXII"
Ms23 = "XXIII"
Ms24 = "XXIV"
Ms25 = "XXV"
Ms26 = "XXVI"
Ms27 = "XXVII"
Ms28 = "XXVIII"
Ms29 = "IXXX"
Ms30 = "XXX"
Ms31 = "XXXI"
Ms32 = "XXXII"
Ms33 = "XXXIII"
Ms34 = "XXXIV"
Ms35 = "XXXV"
Ms36 = "XXXVI"
Ms37 = "XXXVII"
Ms38 = "XXXVIII"
Ms39 = "IXXXX"
Ms40 = "XXXX"
Ms41 = "XXXXI"
Ms42 = "XXXXII"
Ms43 = "XXXXIII"
Ms44 = "XXXXIV"
Ms45 = "XXXXV"
Ms46 = "XXXXVI"
Ms47 = "XXXXVII"
Ms48 = "XXXXVIII"
Ms49 = "IXXXXX"
Ms50 = "XXXXX"
Ms51 = "XXXXXI"
Ms52 = "XXXXXII"
Ms53 = "XXXXXIII"
Ms54 = "XXXXXIV"
Ms55 = "XXXXXV"
Ms56 = "XXXXXVI"
Ms57 = "XXXXXVII"
Ms58 = "XXXXXVIII"
Ms59 = "IXXXXXX"
Ms60 = "XXXXXX"
Ms61 = "XXXXXXI"
Ms62 = "XXXXXXII"
Ms63 = "XXXXXXIII"
Ms64 = "XXXXXXIV"
Ms65 = "XXXXXXV"
Ms66 = "XXXXXXVI"
Ms67 = "XXXXXXVII"
Ms68 = "XXXXXXVIII"
Ms69 = "IXXXXXXX"
Ms70 = "XXXXXXX"
Ms71 = "XXXXXXXI"
Ms72 = "XXXXXXXII"
Ms73 = "XXXXXXXIII"
Ms74 = "XXXXXXXIV"
Ms75 = "XXXXXXXV"
Ms76 = "XXXXXXXVI"
Ms77 = "XXXXXXXVII"
Ms78 = "XXXXXXXVIII"
Ms79 = "IXXXXXXXX"

#Login System Data
Login_Main_msg = "Please Use 8 or More Characters\n\
In Password!\n\
[Mix of numbers and letters Allowed]"
CPassword_Error_msg = "Please Make Sure Your Password\n\
Match And It Must Be 8 or More\n\
characters Again."
#Logout System Data
Logout_msg = "Please Scroll Up Then Use This Logout\n\
System To Quit Later or Type 'Chat'"
MT_msg = "You Got All The Time You Need To Finish\n\
Reading"
TO_msg = "Thank You For Using BlackDocument..."
Exit_msg = "To Check On More Options Please Reopen  \n\
BlackDocument.py or try RekcahDA_Bot\n\
(Chat)"
MT_msg2 = "You So Slow, Bye Bye..."
Empty = "/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/\n\
-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-"
Short_Empty = "/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/"

x = 0
PM_Active = False
#Functions
def clearConsole():
    Refresh = 'clear'   
    if os.name in ('nt', 'dos'): 
        #If Machine is running on Windows, it will use cls
        Refresh = 'cls'
    os.system(Refresh)

def Login_Banner():
    print(Bright_Red + "Note; Wait For 50sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.500)

    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Red + Bright_Green)
    for char in Status_Off:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")

def Login_System():
    print(Bright_Green)
    for char in Header:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Bright_Yellow + "")
    Auto_Text_1 = "Please Login To Begin"
    for char in Auto_Text_1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Bright_Red + "")
    Auto_Text_2 = "Please Note Your iD is Your Membership"
    for char in Auto_Text_2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    Auto_Text_3 = "Number in Roman Numerals."
    for char in Auto_Text_3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    print("e.g III // IV // VII")
    print(""+ Bright_Green)
    for char in Login_Main_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def Welcome_Messages():
    #Index Texts In Animated Format
    print(Bright_Green)
    for char in Header:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg_discription:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Bright_Red +"")
    for char in Main_msg_disc:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg_disc2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg_disc3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def Moretime_Load():
    print(Bright_Yellow + BG_Dark_Cyan)
    for char in Short_Empty:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(""+ Rest)

def Index_Banner():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 20sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.500)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Blue + Bright_Green)
    for char in Status_On:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")

def NoLoad_Banner():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 0sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Blue + Bright_Green)
    for char in Status_On:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")

def NoLoad_Banner2():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 0sec, It Will Finish Soon"+ Bright_Yellow)
    for char in B1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in B7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in Banner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Red + Bright_Green)
    for char in Status_Off:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")

def Firewall_Banner():
    #Welcoming Index Texts
    #Banner
    print(Bright_Red + "Note; Wait For 0sec, It Will Finish Soon"+ Bright_Yellow)
    for char in FWB1:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB5:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB6:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print("")
    for char in FWB7:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Bright_Cyan + "")
    for char in FWBanner_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Dark_Blue + BG_Dark_Green + "")
    for char in Line:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest + Bright_Green + BG_Dark_Blue)
    for char in Endl:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    
    print(BG_Dark_Red + Bright_Green)
    for char in Status_Off:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.0)
    print(Rest +"")

def Index_Welcome_msg():
    #Index Texts In Animated Format
    print(Bright_Green)
    for char in Header:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg_discription:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print(Bright_Red +"")
    for char in Main_msg_disc:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg_disc2:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Main_msg_disc3:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def Index_Welcome_msg2():
    #Index Texts In Animated Format
    print(Bright_Green)
    for char in Header:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    for char in Unlocked_Version_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")

def Main_Menu():
    #Script Menu
    Auto_Text_4 = "[+] -> Menu"
    print(Bright_Magenta + "")
    for char in Auto_Text_4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)
    print("")

    #Building Menu
    print(Bright_Cyan + BG_Bright_Magenta + Menu_TB + Rest)
    print(Bright_Cyan + BG_Bright_Magenta + Menu1 + Rest)
    print(Bright_Cyan + BG_Bright_Magenta + Menu2 + Rest)
    print(Bright_Cyan + BG_Bright_Magenta + Menu3 + Rest)
    print(Bright_Cyan + BG_Bright_Magenta + Menu4 + Rest)
    print(Bright_Cyan + BG_Bright_Magenta + Menu5 + Rest)
    print(Bright_Cyan + BG_Bright_Magenta + Menu_BB + Rest)

    print(Bright_Magenta + "")
    for char in Menu_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print("")

def More_Menu():
    #Script Menu
    Auto_Text_4 = "[+] -> Menu"
    print(Bright_Magenta + "")
    for char in Auto_Text_4:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.5)
    print("")

    #Building Menu
    print(Bright_Cyan + BG_Dark_Magenta + Menu_TB + Rest)
    print(Bright_Cyan + BG_Dark_Magenta + More_Menu1 + Rest)
    print(Bright_Cyan + BG_Dark_Magenta + More_Menu2 + Rest)
    print(Bright_Cyan + BG_Dark_Magenta + More_Menu3 + Rest)
    print(Bright_Cyan + BG_Dark_Magenta + More_Menu4 + Rest)
    print(Bright_Cyan + BG_Dark_Magenta + Menu_BB + Rest)

    print(Bright_Magenta + "")
    for char in Menu_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print("")

def Chat_App():
    global PM_Active
    if PM_Active == True:
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
        print(Bright_Magenta + "RekcahDA_Bot: "+ Bright_Red +"Only Preminum Members Allowed\n\
To Open Chat...\n\
\n\
Please Register First!!!")

def Logout_System():
    #Logout Config
    while True:
        print(Bright_Red + "")
        for char in Logout_msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.3)
        print("")
        Logout = input(BG_Bright_Red + Bright_Yellow +"Logout? <(Y/N)> "+ Rest + Bright_Green)
        if Logout == Binary_Firewall[0]:
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

            Moretime = input(BG_Bright_Red + Bright_Yellow +"Are You Done Yet? <(Y/N)> " + Rest + Bright_Green)
            print(Rest + Bright_Red + "")
            if Moretime == Binary_Firewall[0]:
                for char in MT_msg2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                break

            elif Moretime == DemonFireWall[7]:
                Chat_App()

            elif Moretime == Binary_Firewall[1]:
                print(Rest +""+ Bright_Red +"The End...")
                print("")
                print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
                for char in TO_msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                break
        elif Logout == "Chat":
            Chat_App()
            break
        else:
            print(Rest +""+ Bright_Red +"The End...")
            print("")
            print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
            for char in TO_msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            break

def Logout_System2():
    #Logout Config
    while True:
        print(Bright_Red + "")
        for char in Logout_msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.3)
        print("")
        Logout = input(BG_Bright_Red + Bright_Yellow +"Logout? <(Y/N)> "+ Rest + Bright_Green)
        if Logout == Binary_Firewall[0]:
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

            Moretime = input(BG_Bright_Red + Bright_Yellow +"Are You Done Yet? <(Y/N)> " + Rest + Bright_Green)
            print(Rest + Bright_Red + "")
            if Moretime == Binary_Firewall[0]:
                for char in MT_msg2:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                break

            elif Moretime == DemonFireWall[7]:
                Chat_App()

            elif Moretime == Binary_Firewall[1]:
                print(Rest +""+ Bright_Red +"The End...")
                break
        elif Logout == "Chat":
            Chat_App()
            break
        else:
            print(Rest +""+ Bright_Red +"The End...")
            break

def Loading_Prograss():
    print(Bright_Yellow + BG_Dark_Cyan)
    for char in Empty:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print(""+ Rest)

def Broken_User():
    clearConsole()
    NoLoad_Banner2()
    Nickname = ""
    print(Bright_Red + Nickname + "\n\
              *\n\
            * U *\n\
        *   Just    *\n\
    *   Got Hacked!!   *\n\
*****************************\n\
*****************************\n\
Sorry you are not our Member!\n\
*****************************\n\
*****************************")

def Broken_User2():
    clearConsole()
    NoLoad_Banner2()
    Nickname = ""
    print(Bright_Red + Nickname + "\n\
              *\n\
            * U *\n\
        *   Just    *\n\
    *   Got Hacked!!   *\n\
*****************************\n\
*****************************\n\
Sorry you are not our Member!\n\
You Not Allowed To Open Chat!\n\
*****************************\n\
*****************************")
   