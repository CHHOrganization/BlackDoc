import os,sys,time
import Functions as Config

def clearConsole():
    Refresh = 'clear'
    if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
        Refresh = 'cls'
    os.system(Refresh)
clearConsole()

#This Script Must Not Be Copyrighted As It Will Make The Org Ban Your Membership!
#Developed By: CHHOrg
#Promoted By: DarkDoor
#Organization Director: GoldenThug RSS
#Membership: RekcahHC_I

#RHC_I; I created this script to keep members of the org upto date and teach plus also
#       Solving some Organization members problems they sometimes face like the Config of Yaaic App
#       Then added more features to the script to be more complex on it's own without access it with 
#       Data, all you need is Terminal then you good to go!

#Please Use The Classified information of this Org to this Org!
#No Copyrighting
#Dont Share This Script With Others.

#All BlackDocument Stored Data -------- IF You May Change Something Here Your Program Wont Work Right.

#Banner Data
B1 = "-----------------------------------------"
B2 = "-----------------------------------------"
B3 = "--- Cryptic Hats Hackers Organization ---"
B4 = "---         BlackDoc V0.0.04          ---"
B5 = "---       Security Level: 1.04        ---"
B6 = "-----------------------------------------"
B7 = "-----------------------------------------"
Banner_msg = "Follow Us At Telegram To Stay Upto Date."
Line = "*****************************************"
Endl = "     100% BlackDoc Is Done Loading       "

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
Bright_Black = "\u001b[30;1m"
Bright_Red = "\u001b[31;1m"
Bright_Green = "\u001b[32;1m"
Bright_Yellow = "\u001b[33;1m"
Bright_Blue = "\u001b[34;1m"
Bright_Magenta = "\u001b[35;1m"
Bright_Cyan = "\u001b[36;1m"
Bright_White = "\u001b[37;1m"

#Dark Text Colors 
Dark_Black = "\u001b[30m"
Dark_Red = "\u001b[31m"
Dark_Green = "\u001b[32m"
Dark_Yellow = "\u001b[33m"
Dark_Blue = "\u001b[34m"
Dark_Magenta = "\u001b[35m"
Dark_Cyan = "\u001b[36m"
Dark_White = "\u001b[37m"

#Bright Background Colors 
Bright_Black = "\u001b[40;1m"
BG_Bright_Red = "\u001b[41;1m"
BG_Bright_Green = "\u001b[42;1m"
BG_Bright_Yellow = "\u001b[43;1m"
BG_Bright_Blue = "\u001b[44;1m"
BG_Bright_Magenta = "\u001b[45;1m"
BG_Bright_Cyan = "\u001b[46;1m"
BG_Bright_White = "\u001b[47;1m"

#Dark Background Colors 
BG_Dark_Black = "\u001b[40m"
BG_Dark_Red = "\u001b[41m"
BG_Dark_Green ="\u001b[42m"
BG_Dark_Yellow = "\u001b[43m"
BG_Dark_Blue = "\u001b[44m"
BG_Dark_Magenta = "\u001b[45m"
BG_Dark_Cyan = "\u001b[46m"
BG_Dark_White = "\u001b[47m"

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

#Membership Data Storage
iD = " "
Membership = "RekcahHC_"
Location = " "
Telegram = "T.me/RekcahHC_"
Secret = "BDU"
Password = ""

#EVilNinja Data
Level_1_Names = ["Kerry", "Jackey", "Mary", "Blackey", "Melisa", "Susan"]
Level_1_Surnames = ["White", "Rockafeller", "Chinano", "Kingsley", "Martinez", "White"]
Level_1_DOBs = ["1980-12-26", "1966-03-09", "1972-06-23", "1994-08-08", "1982-11-10", "1961-06-16" ]
EL_Passwords = ["26White12", "6603Jackey", "197206Mary", "Kingsley08", "1982Martinez", "Susan1961"]

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

#Logout System Data
Logout_msg = "Please Scroll Up Then Use This Logout\n\
System To Quit Later or Type 'Chat'"
MT_msg = "You Got All The Time You Need To Finish\n\
Reading"
TO_msg = "Thank You For Using BlackDocument..."
Exit_msg = "To Check On More Options Please Reopen\n\
BlackDocument.py or try RekcahDA_Bot\n\
(Chat)"
MT_msg2 = "You So Slow, Bye Bye..."
Empty = "/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-/-/\n\
-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-"

#Game Data
Trying_Again = 0
Live = 3


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
    time.sleep(0.1)
print(Rest + Bright_Green + BG_Dark_Blue)
for char in Endl:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0)
print(Rest + "")

print(BG_Dark_Blue + Bright_Cyan + "Game; EvilNinja V1.0.0 | Dev Date; 27/02 "+ Bright_Yellow + BG_Bright_Magenta)
EvilNinja_msg = "          Welcome To EvilNinja           \n\
      <info>Hacking Dumpfall</info>      "
for char in EvilNinja_msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
print(Rest +"")

print(Bright_Green)
Prove_msg = "Are you a hacker or wanna be?\n\
Prove Your Self..."
for char in Prove_msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
print("")

Levels = "               Easy Level                \n\
              Normal Level               \n\
               Hard Level                "
print(BG_Dark_Magenta + Bright_Yellow + Levels + Rest)

#Easy Level ..................................................................................................................................................................................................................
Answer = input(Bright_Green + "Enter Level: ")
if Answer == "Easy Level":
    Easy_Level_msg = "EvilNinja Level: Easy\n\
Note: You Only Got 3 Chances\n\
To Get This Password Right!"
    print(Bright_Red)
    for char in Easy_Level_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

    while True:
        try:    
            Config.Victims_DDB()
            Config.Victims_Data_ELS1()

            Stage1 = input(Bright_Cyan + "Password: ")
            if len(Stage1) < 9 or len(Stage1) > 9:
                print(Bright_Red + "The Password Contain 9 Characters.")
                continue
            if Stage1 == EL_Passwords[0]:
                print(BG_Dark_Magenta + Bright_Yellow)
                Stage1_msg = "            Congradulations              \n\
                You Won                  "
                for char in Stage1_msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                print(Rest)
                print(BG_Dark_Blue + "         " + Bright_Green + Stage1 + " Is Correct!           "+ Rest)
                Answer = input(BG_Bright_Green + Bright_Blue + "Next Stage? <(Y|N)>" + Rest + Bright_Green + " ")
                if Answer == "N":
                    print(Dark_Red + "Thank You For Playing EvilNinja.")
                    break
                else:
                    Config.Victims_DDB()
                    Config.Victims_Data_ELS2()
                    Stage2 = input(Bright_Cyan + "Password: ")
                    if len(Stage2) < 10 or len(Stage2) > 10:
                        print(Bright_Red + "The Password Contain 10 Characters.")
                        continue
                    if Stage2 == EL_Passwords[1]:
                        print(BG_Dark_Magenta + Bright_Yellow)
                        Stage2_msg = "            Congradulations              \n\
                You Won                  "
                        for char in Stage2_msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)
                        print(Rest)
                        print(BG_Dark_Blue + "         " + Bright_Green + Stage2 + " Is Correct!          "+ Rest)
                        
                        Answer = input(BG_Bright_Green + Bright_Blue + "Next Stage? <(Y|N)>" + Rest + Bright_Green + " ")
                        if Answer == "N":
                            print(Dark_Red + "Thank You For Playing EvilNinja.")
                            break
                        else:
                            Config.Victims_DDB()
                            Config.Victims_Data_ELS3()
                            Stage3 = input(Bright_Cyan + "Password: ")
                            if len(Stage3) < 10 or len(Stage3) > 10:
                                print(Bright_Red + "The Password Contain 10 Characters.")
                                continue
                            if Stage3 == EL_Passwords[2]:
                                print(BG_Dark_Magenta + Bright_Yellow)
                                Stage3_msg = "            Congradulations              \n\
                You Won                  "
                                for char in Stage3_msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                print(Rest)
                                print(BG_Dark_Blue + "         " + Bright_Green + Stage3 + " Is Correct!          "+ Rest)
                            else:
                                Config.Try_Again()
                                
                        break
                    else:
                        Config.Try_Again()

            else:
                Config.Try_Again()
                
        except:
            print(Bright_Red + "Hack The Password\n\
the Password Might Contain\n\
Mix Of Letters and Numbers")
            continue
