import os,sys,time

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
B4 = "---         BlackDoc V0.0.03          ---"
B5 = "---       Security Level: 1.03        ---"
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
Secret_Chat = "X7ksLyChat-"

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

#Banner
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
print(Rest +"")

#Login System & Instructions
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
Login_Main_msg = "Please Use 8 or More Characters\n\
In Password!\n\
[Mix of numbers and letters Allowed]"
print(""+ Bright_Green)
for char in Login_Main_msg:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
print("")
iD = input(Bright_Cyan +"iD: ")
Password = input("Password: ")
if len(Password) >= 8:    
    Cpassword = input("Confirm Password: ")
    if Password == Cpassword:
        Location = input("Location: ")
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        print(Dark_Blue + BG_Dark_Green + Line + Rest)
        def clearConsole():
            Refresh = 'clear'
            if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                Refresh = 'cls'
            os.system(Refresh)
        clearConsole() 

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
        print(Rest +"")

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

        #Logged in User Details
        User_Data = "-----Here is your Membership Details-----"
        print(BG_Bright_Cyan + Bright_Yellow)
        for char in User_Data:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.3)
        print(Rest +"")
        print(Bright_Red + "User iD: " + iD)
        print("Membership: "+ Membership + iD)
        print("Yaaic Password: "+ iD + Location[1] + Password[0] + Location[3] + iD[0] + Password[4] + Password[6])
        print("Telegram: "+ Bright_Magenta + "@" + Bright_Red + Telegram + iD)
        print("Location: "+ Location)
        print("Unique Code: "+ Secret + iD + "-" + Location[0] + Password[3] + Location[4] + iD[0] + Password[1] + Password[0])

        #Script Menu
        Auto_Text_4 = "[+] -> Menu"
        print(Bright_Magenta + "")
        for char in Auto_Text_4:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.5)
        print("")

        #Building Menu
        print(Bright_Cyan + BG_Dark_Yellow + Menu_TB)
        print(Bright_Cyan + BG_Dark_Yellow + Menu1)
        print(Bright_Cyan + BG_Dark_Yellow + Menu2)
        print(Bright_Cyan + BG_Dark_Yellow + Menu3)
        print(Bright_Cyan + BG_Dark_Yellow + Menu4)
        print(Bright_Cyan + BG_Dark_Yellow + Menu5)
        print(Bright_Cyan + BG_Dark_Yellow + Menu_BB + Rest)

        print(Bright_Magenta + "")
        for char in Menu_msg:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.2)
        print("")

        Answer = input(Bright_Cyan +"Select: ")
        if Answer == "Updates":
            #Updates Script
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                os.system(Refresh)
            clearConsole()

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
            print(Rest +"")

            print(Bright_Yellow) 
            Auto_Text_15 = "Updates"
            for char in Auto_Text_15: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")

            #The Org Message
            print(Bright_Yellow)
            Auto_Text_11 = "The Organization Updates"
            for char in Auto_Text_11: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")

            print(Dark_Cyan)
            Auto_Text_12 = "Date: 20/02/2022 Updates"
            for char in Auto_Text_12: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            print("")

            print(Bright_Green +"The Org is finally in it's own level of\n\
trust with it's members to share and make use of this script. This Script")
            print("Containing The Org data as our members\n\
agreed to share their public cryptic info throw the BlackDoc")
            print(Bright_Red +"Please Note; All information in this\n\
document is classified to unmembers of\n\
The Org")
            print("Make sure you dont share this script!")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
        
            #New Members Updates
            print(Bright_Yellow)
            Auto_Text_13 = "New Members List"
            for char in Auto_Text_13: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")

            print(Dark_Cyan)
            Auto_Text_14 = "Date: 20/02/2022 Updates "
            for char in Auto_Text_14: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            print("")

            print(Dark_Magenta + Ms1 + Bright_Red +". Membership: "+ Membership + Ms7) 
            print("Date: 20/02/2022")
            print(Dark_Magenta + Ms2 + Bright_Red +". Membership: "+ Membership + Ms8)
            print("Date: 20/02/2022")
            print(Dark_Magenta + Ms3 + Bright_Red +". Membership: "+ Membership + Ms9)
            print("Date: 20/02/2022")
            print(Dark_Magenta + Ms4 + Bright_Red +". Membership: "+ Membership + Ms10)
            print(Bright_Green +"Use Menu -> Then Cammand; 'Memberships'  To See More...")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            #About The BlackDoc
            print(Bright_Yellow)
            Auto_Text_17 = "About BlackDoc Updates"
            for char in Auto_Text_17: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            print(Bright_Cyan)
            Auto_Text_16 = "Date: 22/02 - 01/03/2022 Updates"
            for char in Auto_Text_16: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            print()

            print(Bright_Green +"About The Script.")
            print("You using;")
            print("Name: BlackDocument.py")
            print("Version: V0.0.03")
            print("Security Level: "+ Ms1 + ".03")
            print("Developed By: CHHOrg")
            print("Promoted By: DarkDoor")
            print("Released Date: 20/02/2022")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            
            print(Bright_Yellow)
            Auto_Text_18 = "Errors, Fixed Errors and New Features\n\
            Updates"
            for char in Auto_Text_18: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")

            print(Dark_Cyan)
            Auto_Text_10 = "Date: 21/02/2022 Updates\n\
[(Old Version)]"
            for char in Auto_Text_10: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            print("")

            print(Bright_Red)
            Auto_Text_9 = "[+] -> FIXED Errors"
            for char in Auto_Text_9: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            print("")

            print(Bright_Magenta + Ms1 + Bright_Green +"). Fixed all spelling errors")
            print(Bright_Magenta + Ms2 + Bright_Green +"). Fixed all cutting words")
            print(Bright_Magenta + Ms3 + Bright_Green +"). Fixed underlinings Lan")
            print(Bright_Magenta + Ms4 + Bright_Green +"). Fixed underlining divisions")
            print("for each page in our Menu")
            print(Bright_Magenta + Ms5 + Bright_Green +"). Fixed directory folder in Zip")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            print(Bright_Red)
            Auto_Text_8 = "[+] -> New Features"
            for char in Auto_Text_8: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            print("")

            print(Bright_Magenta + Ms1 + Bright_Green +"). We added Colors")
            print(Bright_Magenta + Ms6 + Bright_Green +"). We added Banner")
            print(Bright_Magenta + Ms7 + Bright_Green +"). We added more error messages")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            print(Bright_Cyan + "")
            Auto_Text_7 = "Date: 22/02 - 01/03/2022 Updates\n\
([New Version])"
            for char in Auto_Text_7: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            
            print(Bright_Red + "")
            Auto_Text_6 = "[+] -> FIXED Errors"
            for char in Auto_Text_6: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            print("")

            print(Bright_Magenta + Ms1 + Bright_Green +"). Fixed Menu Borders")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            print(Bright_Red + "")
            Auto_Text_5 = "[+] -> New Features"
            for char in Auto_Text_5: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            print("")

            print(Bright_Magenta + Ms1 + Bright_Green +"). We added new menu items")
            print(Bright_Magenta + Ms2 + Bright_Green +"). We added script animation")
            print(Bright_Magenta + Ms3 + Bright_Green +"). We added new security for exits")
            print(Bright_Magenta + Ms3 + Bright_Green +"). We added a Bot")
            print(Bright_Magenta + Ms3 + Bright_Green +"). We added Commands")
            print(Bright_Magenta + Ms3 + Bright_Green +"). We added Org Rules at More. in Menu")
            print(Bright_Magenta + Ms3 + Bright_Green +"). We added Loading Progress")
        
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            print(Bright_Red +"")
            Auto_Text_4 = "[+] -> Errors"
            for char in Auto_Text_4: 
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            print("")
            print(Bright_Magenta + Ms1 + Bright_Green +"). Chat Option in Menu for Termux/Linux\n\
Is not working!!!\n\
    \n\
Note: In Termux we run TermuxRun.sh after\n\
Installations.")
            print(Bright_Magenta + Ms2 + Bright_Green +"). Other Items in Menu they are\n\
Unavailable")
            print(Bright_Magenta + Ms3 + Bright_Green +"). The script is still under Developing")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

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

                elif Moretime == "Y":
                    print(Rest +""+ Bright_Red +"The End...")
                    print("")
                    print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
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

            elif Logout == "Y":
                print("")
                print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
                for char in TO_msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3)

        #End Part

        elif Answer == "VPN Files":

            #VPN Files Script
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                os.system(Refresh)
            clearConsole() 
            
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
            print(Rest +"")

            print(Bright_Yellow +"VPN Files")
            print(Bright_Green +"To use our VPN Files please download HA\n\
Tunnel plus at Google playstore")
            print("Then in telegram DarkDoor Chatroom has\n\
files and instructions for Passwords.")

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
        
        #End Part

        elif Answer == "Yaaic Config":
            
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                os.system(Refresh)
            clearConsole()


            #Yaaic Config Script
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
            print(Rest +"")

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
                if answer == "Y":

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
'Authenticate with Nickserv'")
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
                    if answer == "Y":

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
                        if answer == "Y":

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

                        #End Of Second Configurations   
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
                            print(Bright_Red +"You Slow Bye!")
                            print(quit())   
                    else:
                        print(Bright_Red +"You Slow Bye!")
                        print(quit()) 
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
                def clearConsole():
                    Refresh = 'clear'
                    if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                        Refresh = 'cls'
                    os.system(Refresh)
                clearConsole()

                #Installation Configurations
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
                print(Rest +"")
                
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

        #End Part

        elif Answer == "Darkweb Links":
            #DarkWeb Links Script

            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                os.system(Refresh)
            clearConsole()
        
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
            print(Rest +"")

            print(Bright_Yellow)
            Auto_Text_23 = "DarkWeb Links"
            for char in Auto_Text_23:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            print("" + Bright_Magenta)

            Auto_Text_24 = "Top 20 .onion websites from the depths of\n\
The dark web. \n\
Want to explore the dark web? Here is our\n\
List of the best .onion websites in 2022."
            for char in Auto_Text_24:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_25 = "Last updated: 23/02/2022"
            print("" + Bright_Cyan)
            for char in Auto_Text_25:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)

        
            Auto_Text_26 = "The deep web is the part of the internet \n\
that is not indexed by search engines. A \n\
part of the deep web is the dark web, \n\
which exists inside layered proxy networks \n\
—known as darknets. Of these darknets, \n\
Tor (short for “The Onion Router”) is by far \n\
the largest."
            print("" + Bright_Green)
            for char in Auto_Text_26:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)


            Auto_Text_27 = "Tor and the Onion Browser"
            print("" + Bright_Magenta)
            for char in Auto_Text_27:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_28 = "Inside the Tor network, sites cannot use\n\
regular domain names. Instead, they use \n\
pseudo-domain names ending in .onion. \n\
These domain names are not registered \n\
with a central authority but are instead \n\
derived from cryptographic keys."
            print("" + Bright_Green)
            for char in Auto_Text_28:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_29 = "You can’t access these .onion sites from \n\
your normal web browser—the one you’re \n\
probably viewing this page on. Before \n\
clicking any of the links below, you’ll need \n\
to get the Tor Browser (also called the \n\
Onion Browser)."
            print("")
            for char in Auto_Text_29:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_30 = "Once you’ve downloaded and installed the \n\
Tor Browser, copy and paste the following \n\
URL into the address bar:"
            print("")
            for char in Auto_Text_30:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_31 = "http://expressobutiolem.onion/blog/\n\
best-onion-sites-on-dark-web/"
            print("" + Bright_Magenta)
            for char in Auto_Text_31:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_32 = "Then you’ll be viewing the .onion version of \n\
this page. From there you’ll be able to click \n\
each link and visit each site directly."
            print("" + Bright_Green)
            for char in Auto_Text_32:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_33 = "(Note that connections inside of the Tor \n\
network are end-to-end encrypted by \n\
default, meaning there is no separate \n\
encryption layer necessary as with regular \n\
websites. That’s why most onion sites, \n\
including this page, do not have the S in \n\
HTTPS. Fear not; the Tor Browser will show \n\
an onion instead of the familiar lock icon \n\
when your connection is secure.)"
            print("" + Bright_Red)
            for char in Auto_Text_33:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)
            print("")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            Auto_Text_34 = "Best onion sites by category"
            print("" + Bright_Yellow)
            for char in Auto_Text_34:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)

            Auto_Text_35 = "hough the dark web is infamous for \n\
hosting all manner of illicit content—dark \n\
web marketplaces for buying illegal drugs,\n\
gore sites, and worse—there are plenty of \n\
legitimate sites and services available if \n\
you know where to look."
            print("" + Bright_Green)
            for char in Auto_Text_35:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")

            Auto_Text_36 = "Here are some of the best .onion sites on the dark web, grouped by category:"
            print("")
            for char in Auto_Text_36:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            #DarkWeb Links List

            Auto_Text_37 = "Dark web search engines"
            print("" + Bright_Yellow)
            for char in Auto_Text_37:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)

            Auto_Text_38 = "[+] -> Ahmia"
            print("" + Bright_Magenta)
            for char in Auto_Text_38:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)

            Auto_Text_39 = "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/"
            print("" + Bright_Red)
            for char in Auto_Text_39:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_40 = "Ahmia's onion site on the dark web\n\
Search engines on the dark web are a bit \n\
of a contradiction because dark web sites \n\
by definition are not indexed by traditional \n\
search engines."
            print(""+ Bright_Green)
            for char in Auto_Text_40:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_41 = "Ahmia, however, is not a traditional search \n\
engine. Founded by security researcher \n\
Juha Nurmi, Ahmia is essentially a list of \n\
“hidden” sites that do want to be found. \n\
Onion sites are “crawled” and added to the \n\
list provided their “robots.txt” file permits \n\
it, and if it is not on their blacklist of sites \n\
with abuse material. Site operators can \n\
also submit their own .onion sites for \n\
indexing."
            print("")
            for char in Auto_Text_41:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            

            Auto_Text_42 = "[+] -> Haystak"
            print("" + Bright_Magenta)
            for char in Auto_Text_42:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)

            Auto_Text_43 = "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_43:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_44 = "Haystak's onion site on the dark web\n\
Similar to Ahmia, Haystak also uses a \n\
custom dark web crawler and filters out \n\
dangerous content."
            print(""+ Bright_Green)
            for char in Auto_Text_44:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_45 = "Haystak also offers a premium version that\n\
allows advanced search, access to \n\
historical content, and email alerts."
            print("")
            for char in Auto_Text_45:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_46 = "[+] -> Torch"
            print("" + Bright_Magenta)
            for char in Auto_Text_46:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_47 = "http://xmh57jrknzkhv6y3ls3ubitzfqnkrwxhopf5aygthi7d6rplyvk3noyd.onion/"
            print("" + Bright_Red)
            for char in Auto_Text_47:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_47 = "Torch's onion site on the dark web\n\
Torch is one of the oldest and most \n\
popular search engines on the dark web, \n\
serving over 80,000 requests per day. \n\
Torch is funded primarily through \n\
advertising—purchased in BTC, of course\n\
—which is why you’ll find the front page \n\
blanketed with old-school banner ads of \n\
dubious origins."
            print(""+ Bright_Green)
            for char in Auto_Text_47:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            

            Auto_Text_48 = "[+] -> DuckDuckGo"
            print("" + Bright_Magenta)
            for char in Auto_Text_48:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)   
            Auto_Text_49 = "https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_49:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_50 = "DuckDuckGo's onion site on the dark web\n\
The internet’s favorite alternative to Google \n\
made a name for itself by not logging your \n\
search activity yet still providing decent \n\
results. This focus on privacy makes it the \n\
Tor Browser’s default search engine."
            print(""+ Bright_Green)
            for char in Auto_Text_50:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_51 = "Unlike Ahmia and Haystak, however, \n\
DuckDuckGo doesn’t search .onion sites. \n\
Use it to search the normal internet from \n\
the privacy of your Tor Browser."
            print("")
            for char in Auto_Text_51:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            
            Auto_Text_52 = "[+] -> The Hidden Wiki"
            print("" + Bright_Magenta)
            for char in Auto_Text_52:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)    
            Auto_Text_53 =  "http://zqktlwiuavvvqqt4ybvgvi7tyo4hjl5xgfuvpdf6otjiycgwqbym2qad.onion/wiki/"
            print("" + Bright_Red)
            for char in Auto_Text_53:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_54 = "The Hidden Wiki's onion site on the dark web\n\
One of the most popular ways to get \n\
around the dark web is not to use a search \n\
engine at all. Just like in the old days of the \n\
internet, the dark web maintains numerous \n\
indexes of sites, like The Hidden Wiki."
            print(""+ Bright_Green)
            for char in Auto_Text_54:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_55 = "This community-edited .onion Wikipedia \n\
contains a bunch of links to a wide variety \n\
of services and sources running on the \n\
dark web. Many of those links are defunct, \n\
and even more of them link to scams or \n\
potentially illegal activities. Click at your \n\
own risk!"
            print("")
            for char in Auto_Text_55:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            

            Auto_Text_56 = "News, media, and other organizations"
            print(""+ Bright_Yellow)
            for char in Auto_Text_56:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)

            Auto_Text_57 = "[+] -> ProPublica"
            print(""+ Bright_Magenta)
            for char in Auto_Text_57:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_58 = "http://p53lf57qovyuvwsc6xnrppyply3vtqm7l6pcobkmyqsiofyeznfu5uqd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_57:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_58 = "ProPublica's onion site on the dark web\n\
The first online publication that won a \n\
Pulitzer is now also the first major \n\
publication with a .onion address."
            print(""+ Bright_Green)
            for char in Auto_Text_58:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            
            Auto_Text_59 = "ProPublica does a lot of things differently. \n\
Its source of funding is the deep wallet of \n\
the Sandler Foundation and various other \n\
similar organizations."
            print("")
            for char in Auto_Text_59:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_60 = "Browsing ProPublica’s work through its \n\
.onion site works well, and the site’s very \n\
existence is a big win for privacy and free \n\
speech."
            print("")
            for char in Auto_Text_60:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_61 = "[+] -> Archive Today"
            print(""+ Bright_Magenta)
            for char in Auto_Text_61:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_62 = "http://archiveiya74codqgiix​o33q62qlrqtkgmcitqx5​u2oeqnmn5bpcbiyd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_62:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_63 = "Archive Today's onion site on the dark web\n\
Archive.today (formerly known as \n\
Archive.is) is a platform that aims to \n\
preserve the web’s cultural and scientific \n\
heritage."
            print(""+ Bright_Green)
            for char in Auto_Text_63:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_64 = "Founded in 2012, it stores snapshots of \n\
websites, making it possible to “go back in \n\
time” and see what websites used to look \n\
like and what information they contained."
            print("")
            for char in Auto_Text_64:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_65 = "Archive.today is considered an important \n\
tool to track changes across government \n\
and corporate websites, preserve cultural \n\
heritage, and keep knowledge outside of \n\
autocrats’ reach. You can archive any site \n\
you want, or retrieve historical records \n\
wherever available."
            print("")
            for char in Auto_Text_65:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            
            Auto_Text_66 = "[+] -> The New York Times"
            print(""+ Bright_Magenta)
            for char in Auto_Text_66:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_67 = "https://www.nytimes3xbfgragh.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_67:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_68 = "The New York Times's onion site on the dark web\n\
To make their journalism more accessible \n\
to readers around the world, the New York \n\
Times launched their onion service in 2017. \n\
You won’t find any “hidden” stories here—\n\
it’s the same content as the normal web \n\
edition—but users in countries with \n\
government censorship will appreciate \n\
having a secure way to access it."
            print(""+ Bright_Green)
            for char in Auto_Text_68:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_69 = "[+] -> BBC"
            print(""+ Bright_Magenta)
            for char in Auto_Text_69:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_70 = "https://www.bbcnewsd73hkzno2ini43t4gblxvycyac5aw4gnv7t2rccijh7745uqd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_70:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_71 = "BBC's onion site on the dark web\n\
Following the NYT, the BBC launched a \n\
dark web “mirror” of their international \n\
edition in 2019. Note that some features of \n\
the normal website are not available on the \n\
.onion version, including BBC iPlayer."
            print(""+ Bright_Green)
            for char in Auto_Text_71:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_72 = "[+] -> Facebook"
            print(""+ Bright_Magenta)
            for char in Auto_Text_72:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_73 = "https://www.facebookwkhpilnemxj7asaniu7vnjjbiltxjqhye3mhbshg7kx5tfyd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_73:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_74 = "Facebook's onion site on the dark web\n\
Why would one of the largest organizations \n\
known for its invasive stance on privacy\n\
and controversial clear-name policy have a \n\
.onion address?"
            print(""+ Bright_Green)
            for char in Auto_Text_71:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_75 = "While Facebook might collect everything \n\
you say and do on its platform, it isn’t \n\
happy with sharing this information with \n\
others. Facebook is also keenly aware of \n\
attempts by many governments to restrict \n\
access to a tool that allows strangers \n\
across the web to talk and collaborate \n\
freely."
            print("")
            for char in Auto_Text_75:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_76 = "Facebook’s .onion address doesn’t make it \n\
much easier to maintain an anonymous \n\
account, but it does make Facebook more \n\
accessible in places where it’s censored."
            print("")
            for char in Auto_Text_76:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            
            Auto_Text_77 = "[+] -> CIA"
            print(""+ Bright_Magenta)
            for char in Auto_Text_77:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_78 = "http://ciadotgov4sjwlzihbbgxnqg3xiyrg7so2r2o3lt5wz5ypk4sxyjstad.onion"
            print(""+ Bright_Red)
            for char in Auto_Text_78:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_79 = "CIA's onion site on the dark web\n\
The CIA might seem an odd inclusion in a \n\
list for privacy enthusiasts, but Tor actually \n\
has an unlikely history with the U.S. \n\
government: it was first developed by the \n\
U.S. Navy to help informants posted in \n\
foreign countries to relay information back \n\
safely. In that spirit, the CIA launched an \n\
Onion site to help people around the world \n\
access its resources securely."
            print("")
            print(""+ Bright_Green)
            for char in Auto_Text_79:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            Auto_Text_80 = "Bitcoin wallets"
            print(""+ Bright_Yellow)
            for char in Auto_Text_80:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)

            Auto_Text_81 = "[+] -> Wasabi Wallet"
            print(""+ Bright_Magenta)
            for char in Auto_Text_81:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_82 = "http://wasabiukrxmkdgve5kynjztuovbg43uxcbcxn6y2okcrsg7gb6jdmbad.onion"
            print(""+ Bright_Red)
            for char in Auto_Text_82:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_83 = "Wasabi Wallet's onion site on the dark web\n\
Wasabi Wallet is a Bitcoin wallet that not \n\
only hides all your data in the Tor Network \n\
but also allows you to ‘join’ your \n\
transactions with others to increase your \n\
anonymity. This makes it incredibly difficult \n\
to find out who you are paying."
            print(""+ Bright_Green)
            for char in Auto_Text_83:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_84 = "The process costs a fee, but unlike with \n\
other ‘tumbler’ or ‘mixing’ services, there is \n\
no risk that Wasabi or any of its users \n\
could scam you out of your coins."
            print("")
            for char in Auto_Text_84:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_85 = "[+] -> The Hidden Wallet"
            print(""+ Bright_Magenta)
            for char in Auto_Text_85:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_86 = "http://d46a7ehxj6d6f2cf4hi3b424uzywno24c7qtnvdvwsah5qpogewoeqid.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_86:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_87 = "Hidden Wallet's onion site on the dark web\n\
Like Wasabi Wallet, the Hidden Wallet \n\
mixes your Bitcoins with other users for \n\
extra anonymity. Unlike Wasabi, however, \n\
the Hidden Wallet service is only available \n\
through its .onion site."
            print("")
            print(""+ Bright_Green)
            for char in Auto_Text_87:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            Auto_Text_88 = "Email services"
            print(""+ Bright_Yellow)
            for char in Auto_Text_88:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)

            Auto_Text_89 = "[+] -> ProtonMail"
            print(""+ Bright_Magenta)
            for char in Auto_Text_89:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_90 = "https://protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_90:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_91 = "ProtonMail's onion site on the dark web\n\
Based in Switzerland, ProtonMail is an \n\
encrypted email service that is very \n\
popular with cryptocurrency enthusiasts. \n\
It’s not free, but it’s extremely secure."
            print(""+ Bright_Green)
            for char in Auto_Text_91:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_92 = "[+] -> Riseup"
            print(""+ Bright_Magenta)
            for char in Auto_Text_92:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            Auto_Text_93 = "http://vww6ybal4bd7szmgncyruucpgfkqahzddi37ktceo3ah7ngmcopnpyyd.onion"
            print(""+ Bright_Red)
            for char in Auto_Text_93:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_94 = "Riseup's onion site on the dark web\n\
Riseup is a volunteer-run email provider for \n\
activists around the world."
            print(""+ Bright_Green)
            for char in Auto_Text_94:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_95 = "Founded around 1999 by activists in \n\
Seattle, it has since grown to over six \n\
million users worldwide. It publishes a \n\
newsletter in multiple languages and not \n\
only runs Onion services for its website but \n\
all its email and chat services."
            print("")
            for char in Auto_Text_95:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            print("")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            Auto_Text_96 = "Other privacy tools and services"
            print(""+ Bright_Yellow)
            for char in Auto_Text_96:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)

            Auto_Text_97 = "[+] -> Keybase"
            print(""+ Bright_Magenta)
            for char in Auto_Text_97:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_98 = "http://keybase5wmilwokqirssclfnsqrjdsi7jdir5wy7y7iu3tanwmtp6oid.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_98:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_99 = "Keybase's onion site on the dark web\n\
Keybase is an exciting identity service that \n\
aims to make it easy for you to link the \n\
presence of your online identities together \n\
in a cryptographic way. You can upload \n\
your PGP key, or have the site create one \n\
for you, and use it to cryptographically link \n\
your Twitter profile, Github account, or \n\
Bitcoin address together."
            print(""+ Bright_Green)
            for char in Auto_Text_99:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_100 = "Keybase also offers extremely user-\n\
friendly secure chat and file-sharing \n\
services through its app."
            print("")
            for char in Auto_Text_100:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            
            Auto_Text_101 = "[+] -> ZeroBin"
            print(""+ Bright_Magenta)
            for char in Auto_Text_101:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_102 = "http://zerobinftagjpeeebbvyzjcqyjpmjvynj5qlexwyxe7l3vqejxnqv5qd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_102:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_103 = "ZeroBin's onion site on the dark web\n\
Pastebins are text sharing services, useful \n\
for sending and sharing large snippets of \n\
code or text. ZeroBin offers an extra \n\
secure version of this service by only \n\
encrypting and decrypting text in the \n\
browser, meaning their servers have no \n\
knowledge of what is passing through it."
            print(""+ Bright_Green)
            for char in Auto_Text_103:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            
            Auto_Text_104 = "[+] -> SecureDrop"
            print("" + Bright_Magenta)
            for char in Auto_Text_104:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_105 = "http://sdolvtfhatvsysc6l34d65ymdwxcujausv7k5jk4cy5ttzhjoi6fzvyd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_105:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_106 = "SecureDrop's onion site on the dark web\n\
A favorite of journalists and their \n\
anonymous sources, SecureDrop makes it \n\
easy to share confidential information \n\
without revealing your identity. Many news \n\
publications, like the ones listed above, \n\
have a SecureDrop on their .onion sites."
            print(""+ Bright_Green)
            for char in Auto_Text_106:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_107 = "[+] -> MEGATor"
            print(""+ Bright_Magenta)
            for char in Auto_Text_107:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_108 = "http://crqkllx7afomrokwx6f2sjcnl2do2i3i77hjjb4eqetlgq3cths3o6ad.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_108:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_109 = "MegaTor's onion site on the dark web\n\
MegaTor is a super-simple anonymous file sharing service that’s not available on the normal internet. Best of all, it’s free and decently fast."
            print(""+ Bright_Green)
            for char in Auto_Text_109:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)

            Auto_Text_110 = "[+] -> PrivacyTools"
            print(""+ Bright_Magenta)
            for char in Auto_Text_110:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            Auto_Text_111 = "http://privacy2zbidut4m4jyj3ksdqidzkw3uoip2vhvhbvwxbqux5xy5obyd.onion/"
            print(""+ Bright_Red)
            for char in Auto_Text_111:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)

            Auto_Text_112 = "PrivacyTools's onion site on the dark web\n\
The tools we’ve listed above are just the tip of the iceberg. If you’re interested in privacy and the dark web, take a deep dive into PrivacyTools, an extensive directory of anti-surveillance tools, services, and educational materials."
            print(""+ Bright_Green)
            for char in Auto_Text_112:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.1)
            

            Auto_Text_113 = "Dark web FAQ: More about onion sites"
            print(""+ Bright_Yellow)
            for char in Auto_Text_113:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            
            Auto_Text_114 = "[+] -> What are onion sites used for?"
            print(""+ Bright_Magenta)
            for char in Auto_Text_114:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)

            Auto_Text_115 = "Onion sites are used for a variety of purposes, but the common thread is privacy and anonymity, both for users and service providers. It is nearly impossible to trace the activity on onion sites, including the identities of people who use them."

            Auto_Text_116 = "Naturally, this makes the dark web a breeding ground for illegal activity. But onion sites can also serve nobler goals, like providing access to information and independent journalism in countries with government censorship. Activists, whistle blowers, and journalists also use the dark web to communicate securely with sources and news organizations."

            Auto_Text_117 = "[+] -> Is it illegal to visit onion sites?"
            Auto_Text_118 = "It’s not illegal to visit any of the onion sites listed above. But as the dark web does contain illegal activity, we can’t guarantee you won’t stumble across illicit material as you dig deeper into it, nor can anyone guarantee your activity will remain completely untraceable. This is why we say to explore at your own risk!"

            Auto_Text_119 = "What kind of content is on the dark web?"
            Auto_Text_120 = "As mentioned above, much of the content on the dark web is the same as you might find on the normal internet (news, message boards, web services) but made accessible on a more anonymous platform."

            Auto_Text_121 = "Some content, however, is only available on onion sites so as to evade detection by law enforcement: namely gore sites and other illegal media, and marketplaces selling illegal items such as drugs, weapons, and fake documents."

            Auto_Text_121 = "Needless to say, we don’t condone any content forbidden by law."

            Auto_Text_122 = "What can you buy on the dark web?"
            Auto_Text_123 = "You can buy almost anything on the dark web with Bitcoin and other cryptocurrencies, from secondhand furniture to illegal drugs, porn, exotic animals, and all manner of criminal services-for-hire."

            Auto_Text_124 = "But that doesn’t mean you should! As stated above, we don’t condone any activity—on the dark net or otherwise—that is forbidden by law."
            Auto_Text_125 = "Can you access the dark web with a VPN?"
            Auto_Text_126 = "Yes, you can connect to a VPN server before launching the Tor Browser to hide your IP address from any node in the Tor network, and to hide the fact that you are using Tor from your network operator."

            Auto_Text_127 = "This method is called Tor over VPN, and it’s a great way to increase your privacy over using Tor alone."

            

            Auto_Text_128 = "What are your favorite .onion sites? Are there any sites you wish had a .onion address? Share your thoughts in the comments below!"
















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
        
        #End Part

        elif Answer == "Memberships":
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                os.system(Refresh)
            clearConsole()
            #Membership Script
    
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
            print(Rest + Bright_Green + BG_Dark_Blue + Bright_Blue)
            for char in Endl:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)
            print(Rest +"")

            #Members With Their Individual Details
            print(Bright_Green +"The List Of CHH Organization Members With Their Details")

            #RekcahHC_I Details
            print(Bright_Magenta + Ms1 + Bright_Red +"). Membership:"+ Membership + Ms1)
            print("Nickname: GoldenThug RSS")
            print("Location: South Africa")
            print("Link: T.me/"+ Membership + Ms1)
            print(Bright_Green +"Skills List")
            print(Bright_Magenta + Ms1 + Bright_Red +"). Full Stock Developer")
            print(Bright_Magenta + Ms2 + Bright_Red +"). Digital Marketer")
            print(Bright_Magenta + Ms3 + Bright_Red +"). Ethical Hacker")
            print(Bright_Magenta + Ms4 + Bright_Red +"). DarkWeb User")
            print(Bright_Magenta + Ms5 + Bright_Red +"). Script kiddo")
            print(Bright_Magenta + Ms6 + Bright_Red +"). VPN Creator")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            #RekcahHC_II Deatils
            print(Bright_Magenta + Ms2 + Bright_Red +"). Membership:"+ Membership + Ms2)
            print("Nickname: Divine INFINITY")
            print("Location: South Africa")
            print("Link: T.me/"+ Membership + Ms2)
            print(Bright_Green +"Skills List")
            print(Bright_Magenta + Ms1 + Bright_Red +"). Hacking; Facebook // Instagram // Etc")
            print(Bright_Magenta + Ms2 + Bright_Red +"). Modding")
            print(Bright_Magenta + Ms3 + Bright_Red +"). Hacking; CCTV Cameras")
            print(Bright_Magenta + Ms4 + Bright_Red +"). Able To Add Windows 10 to Android")
            print(Bright_Magenta + Ms5 + Bright_Red +"). VPN Creator")
            print(Bright_Magenta + Ms6 + Bright_Red +"). VPN Modder")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            

            print(Bright_Magenta + Ms3 + Bright_Red +"). Membership:"+ Membership + Ms3)
            print("Location: North America")
            print(Bright_Magenta + Ms4 + Bright_Red +"). Membership:"+ Membership + Ms4)
            print("Location: Nigeria")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            #RekachHC_V
            print(Bright_Magenta + Ms5 + Bright_Red +"). Membership:"+ Membership + Ms5)
            print("Location: Ghana")
            print("Nickname: PJmax")
            print("Link: T.me/"+ Membership + Ms5)
            print("YouTuber: @DoriCodes")
            print(Bright_Green +"Skills List")
            print(Bright_Magenta + Ms1 + Bright_Red +"). Programming Languages; Python // C++ // HTML // CSS")
            print(Bright_Magenta + Ms2 + Bright_Red +"). Termux Hacker")
            print(Bright_Magenta + Ms3 + Bright_Red +"). A Little Experience In Kali Linux")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)


            #RekcahHC_VI
            print(Bright_Magenta + Ms6 + Bright_Red +"). Membership:"+ Membership + Ms6)
            print("Location: South Africa")
            print("Nickname: Deoderant Dee")
            print("Link: T.me/"+ Membership + Ms6)
            print(Bright_Green +"Skills List")
            print(Bright_Magenta + Ms1 + Bright_Red +"). Coding With Python")
            print(Bright_Magenta + Ms2 + Bright_Red +"). Using VPN")
            print(Bright_Magenta + Ms3 + Bright_Red +"). Website Developer")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            print(Bright_Magenta + Ms7 + Bright_Red +"). Membership:"+ Membership + Ms7)
            print("Location: Ghana")
            print(Bright_Magenta + Ms8 + Bright_Red +"). Membership:"+ Membership + Ms8)
            print("Location: India")
            print(Bright_Magenta + Ms9 + Bright_Red +"). Membership:"+ Membership + Ms9)
            print("Location: China")
            print(Bright_Magenta + Ms10 + Bright_Red +"). Membership:"+ Membership + Ms10)
            print("Location: Nigeria")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print("End Of The List...")

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

        #End Part

        elif Answer == "Apps":
            #Apps Script
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                os.system(Refresh)
            clearConsole()
            
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
            print(Rest +"")

            print(Bright_Red +"Cryptic Hats Hackers Organizations")
            print("Use This Apps To Change Members Phone, To")
            print("Keep Members Busy With Cool Games, To learn")
            print("Programming Offline And Online Plus So On!")
            print(Bright_Magenta +"Lists OF All Apps")

            #Recommanded Apps
            print(Bright_Blue + "[" + Bright_Red + "]" + Bright_Magenta + "->" + Bright_Yellow + "Recommanded Apps")
            
            print(Bright_Magenta + Ms1 + Bright_Green +"). Alison Courses")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Study IT and Get Certificate For Free.")
            print(Bright_Magenta + Ms2 + Bright_Green +"). Code Editor")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Code In Their Android Smart Phones.")
            print(Bright_Magenta + Ms3 + Bright_Green +"). F-Droid")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Install The Best Termux Version That Works.")
            print(Bright_Magenta + Ms4 + Bright_Green +"). GitHub")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Get Source Codes And Packages Installations Instructions.")
            print(Bright_Magenta + Ms5 + Bright_Green +"). HA Tunnel Plus")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Access DFN.hat Files And Access Free Internet.")
            print(Bright_Magenta + Ms6 + Bright_Green +"). ProtonMail")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Have An Encrypted Email Address.")
            print(Bright_Magenta + Ms7 + Bright_Green +"). ProtonVPN")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Change Their Country Location And IP-Address.")
            print(Bright_Magenta + Ms8 + Bright_Green +"). T-UI")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Change Their Android OS To Terminal OS.")
            print(Bright_Magenta + Ms9 + Bright_Green +"). Telegram")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Stay Updated And Be Able To Download The Org Files.")
            print(Bright_Magenta + Ms10 + Bright_Green +"). Termux")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Access Our BlackDocument And Upcoming Hacking Tools.")
            print(Bright_Magenta + Ms11 + Bright_Green +"). Termux T_C")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Get More Termux Tools Installation Instructions.")
            print(Bright_Magenta + Ms12 + Bright_Green +"). Udemy")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Study IT and Get Certificate For Free.")
            print(Bright_Magenta + Ms13 + Bright_Green +"). Yaaic")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Connect To The Organization Server.")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            #Learning Apps
            print(Bright_Blue + "[" + Bright_Red + "]" + Bright_Magenta + "->" + Bright_Yellow + "Learning Apps")
            print(Bright_Magenta + Ms1 + Bright_Green +"). Advanced Networking")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("About Networking And Uses Advanced Education.")
            print(Bright_Magenta + Ms2 + Bright_Green +"). Alison Courses")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("IT and Get Certificate For Free.")
            print(Bright_Magenta + Ms3 + Bright_Green +"). AWD - IDE For Web Dev")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("Web Developing And Is A Full Stock App.")
            print(Bright_Magenta + Ms4 + Bright_Green +"). CMD Command List")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("To USe Command Prompt Like A Pro.")
            print(Bright_Magenta + Ms5 + Bright_Green +"). Codepoint Learn PHP")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("PHP Web Developing.")
            print(Bright_Magenta + Ms6 + Bright_Green +"). HTML & CSS Basics")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("Basics About HTML And CSS Langauages.")
            print(Bright_Magenta + Ms7 + Bright_Green +"). HTML CSS PHP Frameworks")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("Full Stock In Web Developing.")
            print(Bright_Magenta + Ms8 + Bright_Green +"). Learn JAVAScript Offline")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("Javascript Language In A Simple Way.")
            print(Bright_Magenta + Ms9 + Bright_Green +"). Learn PHP Offline")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("PHP Programming Language In A Simple Way.")
            print(Bright_Magenta + Ms10 + Bright_Green +"). Linux Command Library")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("Linux Terminal And Have Also Advanced Commands.")
            print(Bright_Magenta + Ms11 + Bright_Green +"). Termux T_C")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Assist Memebers")
            print("To Get More Termux Tools Installation Instructions.")
            print(Bright_Magenta + Ms12 + Bright_Green +"). PyThon For Beginners-Offline Tutorial")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("Python Language In A Simple Way For Beginners.")
            print(Bright_Magenta + Ms13 + Bright_Green +"). Python X")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("Python With An Online App.")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

            #IT Games
            print(Bright_Blue + "[" + Bright_Red + "]" + Bright_Magenta + "->" + Bright_Yellow + "IT Games")
            print(Bright_Magenta + Ms1 + Bright_Green +"). HackBot")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Keep Memebers")
            print("Entertained All Times.")
            print(Bright_Magenta + Ms2 + Bright_Green +"). Hacker")
            print(Bright_Red + "Description; "+ Bright_Green + "This App keep Memebers")
            print("Entertained All Times.")
            print(Bright_Magenta + Ms3 + Bright_Green +"). Hacker Game")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Keep Memebers")
            print("Entertained All Times.")
            print(Bright_Magenta + Ms4 + Bright_Green +"). Hack Ex")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Keep Memebers")
            print("Entertained All Times.")
            print(Bright_Magenta + Ms5 + Bright_Green +"). Hacking Hero")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Keep Memebers")
            print("Entertained All Times.")
            print(Bright_Magenta + Ms6 + Bright_Green +"). I Hacker" + Bright_Red + " Recommanded")
            print(Bright_Red + "Description; "+ Bright_Green + "This App Teach Memebers")
            print("How To Crack Passwords From 'Basics' To 'GrandMaster' Level.")
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            print(Dark_Blue + BG_Dark_Green + Line + Rest)

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

        #End Part

        elif Answer == "Hacking Lessons":
            #Hacking Lessons Script
            print(Dark_Blue + BG_Dark_Green + Line + Rest)
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                os.system(Refresh)
            clearConsole()
            
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
            print(Rest +"")

            print(Bright_Green +"Cryptic Hats Hackers Organizations")
            print("Use This Script Also To Teach Our Members, About")
            print("IT Related Fundamentals.")
            print(Bright_Red + "Please Note; Everything You Will learn With Us")
            print("Whatsever You Plan To Do With The Knowledge, We Won't")
            print("Be Responsible For The Misuse Of This Information!")
            print(Bright_Magenta +"Hacking Lessons Start Now;")
            print(Bright_Green + "We have 78 Scripts In Total; About This Topic")
            print(Bright_Red +"Note; 'We Still Developing The Scripts'"+ Rest)

            #Hacking Lessions List
            print(Bright_Magenta + Ms1 + Bright_Green +"). Ethical Hacking - Overview" + Bright_Blue)
            print("-> " + Bright_Red + "[Set 1]")

            print(Bright_Magenta + Ms2 + Bright_Green +"). Typings Of Hacking" + Bright_Blue)
            print("-> " + Bright_Red + "[Set 2]")

            print(Bright_Magenta + Ms3 + Bright_Green +"). Advantages Of Ethical Hacking" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 3]")

            print(Bright_Magenta + Ms4 + Bright_Green +"). Hacker Types" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 4]")

            print(Bright_Magenta + Ms5 + Bright_Green +"). Famous Hackers" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 5]")

            print(Bright_Magenta + Ms6 + Bright_Green +"). Ethical Hacking - Terminologies" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 6]")

            print(Bright_Magenta + Ms7 + Bright_Green +"). Ethical Hacking - Tools" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 7]")

            print(Bright_Magenta + Ms8 + Bright_Green +"). Ethical Hacking - Skills" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 8]")

            print(Bright_Magenta + Ms9 + Bright_Green +"). Ethical Hacking - Process" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 9]")

            print(Bright_Magenta + Ms10 + Bright_Green +"). Ethical HAcking - Reconnaissance" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 10]")

            print(Bright_Magenta + Ms11 + Bright_Green +"). Ethical Hacking - Footprinting" + Bright_Blue) 
            print("-> " + Bright_Red + " [Set 11]")

            print(Bright_Magenta + Ms12 + Bright_Green +"). Ethical Hacking - Sniffing" + Bright_Blue)   
            print("-> " + Bright_Red + " [Set 12]")

            print(Bright_Magenta + Ms13 + Bright_Green +"). Types Of Sniffing" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 13]")

            print(Bright_Magenta + Ms14 + Bright_Green +"). Hardware Protocol Analyzers" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 14]")

            print(Bright_Magenta + Ms15 + Bright_Green +"). Lawful Interception" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 15]")

            print(Bright_Magenta + Ms16 + Bright_Green +"). Ehtcal Hacking - Sniffing Tools" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 16]")

            print(Bright_Magenta + Ms17 + Bright_Green +"). Ethical Hacking - ARP Poisoning" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 17]")

            print(Bright_Magenta + Ms18 + Bright_Green +"). What IS ARP Spoofing?" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 18]")

            print(Bright_Magenta + Ms19 + Bright_Green +"). What Is MITM?" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 19]")

            print(Bright_Magenta + Ms20 + Bright_Green +"). Ethical Hacking - DNS Poisoning" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 20]")

            print(Bright_Magenta + Ms21 + Bright_Green +"). Ethical Hacking - Exploitation" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 21]")

            print(Bright_Magenta + Ms22 + Bright_Green +"). Ethical Hacker - Enumeration" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 22]")

            print(Bright_Magenta + Ms23 + Bright_Green +"). Ethical hacking - Metaspoit" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 23]")

            print(Bright_Magenta + Ms24 + Bright_Green +"). Metasploit Payloads" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 24]")

            print(Bright_Magenta + Ms25 + Bright_Green +"). Ethical Hacking - Trojan Attacks" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 25]")

            print(Bright_Magenta + Ms26 + Bright_Green +"). Ethical Hacking - TCP/IP Hijackuing" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 26]")

            print(Bright_Magenta + Ms27 + Bright_Green +"). Ethical Hacking - Email Hijacking" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 27]")

            print(Bright_Magenta + Ms28 + Bright_Green +"). Ethical Hacking - Password HAcking" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 28]")

            print(Bright_Magenta + Ms29 + Bright_Green +"). Ethical Hacking - Wireless Hacking" + Bright_Blue)
            print("-> " + Bright_Red + " [Set 29]")

            Answer = int(input(Bright_Cyan + "Select 'Set' No; "))
            if Answer == 1:
                #Set 1 Details
                print(Bright_Magenta + Ms1 + Bright_Green +"). Ethical Hacking - Overview")


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
                    else:
                        print(Rest +""+ Bright_Red +"The End...")
                        print("")
                        for char in TO_msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)       
                else:
                    print("")
                    print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
                    for char in TO_msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.3)

            #End Part

            elif Answer == 2:
                print(Bright_Magenta + Ms2 + Bright_Green +"). Typings Of Hacking")

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
                    else:
                        print(Rest +""+ Bright_Red +"The End...")
                        print("")
                        for char in TO_msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)       
                else:
                    print("")
                    print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
                    for char in TO_msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.3)

            #End Part
            elif Answer == 3:
                print(Bright_Magenta + Ms3 + Bright_Green +"). Advantages Of Ethical Hacking")

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
                    else:
                        print(Rest +""+ Bright_Red +"The End...")
                        print("")
                        for char in TO_msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)       
                else:
                    print("")
                    print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
                    for char in TO_msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.3)

            #End Part

            elif Answer == 4:
                print(Bright_Magenta + Ms4 + Bright_Green +"). Hacker Types")

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
                    else:
                        print(Rest +""+ Bright_Red +"The End...")
                        print("")
                        for char in TO_msg:
                            sys.stdout.write(char)
                            sys.stdout.flush()
                            time.sleep(0.1)       
                else:
                    print("")
                    print(BG_Dark_Magenta + Bright_Yellow + Exit_msg + Rest + Bright_Red)
                    for char in TO_msg:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.3)

            #End Part    
            
            elif Answer == 5:
                print(Bright_Magenta + Ms5 + Bright_Green +"). Famous Hackers")
            
                #Logout Config
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
                
            #End Part

            else:
                print(Bright_Red + "") 
                Auto_Text_19 = "Please Use Only The Number Of A Set To Open A Set!"
                for char in Auto_Text_19:
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
        
        
        elif Answer == "More":
            
            def clearConsole():
                Refresh = 'clear'
                if os.name in ('nt', 'dos'): #If Machine is running on Windows, it will use cls
                    Refresh = 'cls'
                    os.system(Refresh)
            clearConsole() 

            #More Menu
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
                time.sleep(0.2)
            print(Rest + Bright_Green + BG_Dark_Blue)
            for char in Endl:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.0)
            print(Rest +"")

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

            #Logged in User Details
            User_Data = "-----Here is your Membership Details-----"
            print(BG_Bright_Cyan + Bright_Yellow)
            for char in User_Data:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.3)
            print(Rest +"")
            print(Bright_Red + "User iD: " + iD)
            print("Membership: "+ Membership + iD)
            print("Yaaic Password: "+ iD + Location[1] + Password[0] + Location[3] + iD[0] + Password[4] + Password[6])
            print("Telegram: "+ Bright_Magenta + "@" + Bright_Red + Telegram + iD)
            print("Location: "+ Location)
            print("Unique Code: "+ Secret + iD + "-" + Location[0] + Password[3] + Location[4] + iD[0] + Password[1] + Password[0])

            #Script Menu
            Auto_Text_4 = "[+] -> Menu"
            print(Bright_Magenta + "")
            for char in Auto_Text_4:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.5)
            print("")

            #Building Menu
            print(Bright_Cyan + BG_Dark_Yellow + Menu_TB)
            print(Bright_Cyan + BG_Dark_Yellow + More_Menu1)
            print(Bright_Cyan + BG_Dark_Yellow + More_Menu2)
            print(Bright_Cyan + BG_Dark_Yellow + More_Menu3)
            print(Bright_Cyan + BG_Dark_Yellow + More_Menu4)
            print(Bright_Cyan + BG_Dark_Yellow + Menu_BB + Rest)

            print(Bright_Magenta + "")
            for char in Menu_msg:
                sys.stdout.write(char)
                sys.stdout.flush()
                time.sleep(0.2)
            print("")

            More_MenuQ = input(Bright_Cyan +"Select: ")
            if More_MenuQ == "MyAccount":
                #Logged in User Details
                User_Data = "-------Here is your Account Details-------"
                print(BG_Bright_Cyan + Bright_Yellow)
                for char in User_Data:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3)
                print(Rest +"")
                print(Bright_Red + "User iD: " + iD)
                print("Membership: "+ Membership + iD)
                print("Telegram: "+ Bright_Magenta + "@" + Bright_Red + Telegram + iD)
                print("Location: "+ Location)
                print(""+ BG_Bright_Cyan + Bright_Yellow)
                Security_info = "-----------Account Secret Codes-----------"
                for char in Security_info:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.2)
                print(Rest)
                print("Yaaic Password: "+ iD + Location[1] + Password[0] + Location[3] + iD[0] + Password[4] + Password[6])
                print("DarkChat Code: "+ Secret_Chat + iD + "-" + Location[0] + Password[3] + Location[4] + iD[0] + Password[1] + Password[0])
                print("Unique Code: "+ Secret + iD + "-" + Location[0] + Password[3] + Location[4] + iD[0] + Password[1] + Password[0])

                #End Part..................................................
            
            elif More_MenuQ == "Org Rules":
                #Organization Rules
                Rules_List = "---Here Is The Organization Rules List---"
                print(BG_Bright_Cyan + Bright_Yellow)
                for char in Rules_List:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3)
                print(Rest +"" + Bright_Red)
                Rules_msg = "Organization's Rules;\n\
    I). Dont share this BlackDoc.\n\
    II). Dont copyright any Script!.\n\
    III). You must be an active member.\n\
    IV). You must respect other members.\n\
    V). If you are a beginner please study hard\n\
    everything you need is in BlackDocument.\n\
    \n\
    Note: If you break one of this rules.\n\
    you will lose your membership,\n\
    thats the last imported Rule."
                for char in Rules_msg:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3)
                print(Rest +"")

                #End Line Of Rules..............................................................        
            elif More_MenuQ == "About Us":
                #About The Org
                Org_Title = "---------About The Organization!---------"
                print(BG_Bright_Cyan + Bright_Yellow)
                for char in Org_Title:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3)
                #About The Org
                Org_Info = "About The Organization;\n\
    Cryptic Hats Hackers was created\n\
    At 25th of January 2021 as a new\n\
    Error Hackers Movement and Include\n\
    Developers, Traders, Marketers and\n\
    Digital Designers...\n\
    Since 2021 I 'GoldenThug' been looking\n\
    For committted members to form this\n\
    Community and now as DarkDoor Darkweb\n\
    Social Media of CHH.Org has been closed\n\
    Because of the Development was in an old\n\
    PHP Framework, Am developing a Backend\n\
    Also as the Frontend, this project\n\
    Might take me years to finalize so \n\
    That's were BlackDoc comes in... \n\
    To help the New members also the old\n\
    Mmembers to know how to connect to \n\
    The Irc Channels of the Org \n\
    with Yaaic App cause for now that'\n\
    Where the community is now!\n\
    \n\
    The purpose of the Organization;\n\
    The Organization started as the free\n\
    Darkweb in DNS World that you could \n\
    Access The Org BlackMarket with Udemy \n\
    Free Coupons for IT Lessons plus \n\
    Members could access DarkDoor Darkweb\n\
    Social Media with a one click...\n\
    \n\
    We also had lessons about Hacking and\n\
    More, BlackDoc is more cool cause to\n\
    Run it you only need Termux which means\n\
    Now Our members can study more on a go...\n\
    \n\
    Mission of The Org;\n\
    Our Org Mission is to help build a new\n\
    Error community of seekers about \n\
    IT Fundamentals like networking, coding,\n\
    Hacking, marketing designing also trading...\n\
    All Are Welcomed!!!"
                print(Rest + Bright_Red)
                for char in Org_Info:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)
                print("")
                print("" + Bright_Green +"See Our Rules Please...")
            elif More_MenuQ == "Members List":
                Members_List = "---Here Is The List Of All Org Members---"
                print(BG_Bright_Cyan + Bright_Yellow)
                for char in Members_List:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.3)
                print(Rest + "" + Bright_Green)
                #Member
                Print_Members = "[+] -> Members List Updates\n\
    Date: 24/02/2022\n\
    \n\
    I). Membership: RekcahHC_I\n\
    II). Membership: RekcahHC_II\n\
    III). Membership: RekcahHC_III (Pending)\n\
    IV). Membership: RekcahHC_IV (Pending)\n\
    V). Membership: RekcahHC_V\n\
    VI). Membership: RekcahHC_VI)\n\
    VII). Membership: RekcahHC_VII (Pending)\n\
    VIII). Membership: RekcahHC_VIII (Pending)\n\
    IX). Membership: RekcahHC_IX (Pending)\n\
    X). Membership: RekcahHC_X"
    #End Line Of Members
                for char in Print_Members:
                    sys.stdout.write(char)
                    sys.stdout.flush()
                    time.sleep(0.1)



        else:
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
            #End Part
    else:
        print(Bright_Red + Membership + iD + Bright_Green + " Passwords Didn't Match \n\
Please Make Sure They Match.")
        #The End Of The Script!
else:
    print(Bright_Red + Membership + iD + Bright_Green + " You Need To Input 8 or More \n\
Characters In Password...")