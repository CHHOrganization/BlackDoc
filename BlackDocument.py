import os,sys,time
from Plugins.Configs.Settings import *

#Main Menu Pages
from Plugins.Configs.Pages.Darkweb_Links import *
from Plugins.Configs.Pages.Updates import *
from Plugins.Configs.Pages.VPN_Files import *
from Plugins.Configs.Pages.Yaaic_Config import *
from Plugins.Configs.Pages.Darkweb_Links import *
from Plugins.Configs.Pages.Memberships import *
from Plugins.Configs.Pages.Apps import *
from Plugins.Configs.Pages.Hacking_Lessons import *
from Plugins.Configs.Pages.Chat_App import *

#More Menu Pages
from Plugins.Configs.Pages.More_Menu_Pages.Org_Rules import *
from Plugins.Configs.Pages.More_Menu_Pages.About_Us import *
from Plugins.Configs.Pages.More_Menu_Pages.Members_List import *
from Plugins.Configs.Pages.More_Menu_Pages.Script_Games import *
from Plugins.Configs.Pages.More_Menu_Pages.Org_History import *
from Plugins.Configs.Pages.More_Menu_Pages.Chat_Info import *
from Plugins.Configs.Pages.More_Menu_Pages.BlackDoc_Info import *

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

#Membership Data Storage
Nickname = ""
Identity = ""
Membership = "RekcahHC_"
Location = ""
Telegram = "T.me/RekcahHC_"
Secret = "BDU"
Secret_Chat = "X7ksLyChat-"
Password = ""
Paying_Member = ""

#Main Page Functions
def Password_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Yellow +"Login Security")
    print(Bright_Red + Membership + Identity + Bright_Green + Login_Main_msg)
    Moretime_Load()
    clearConsole()

def CPassword_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Yellow +"Login Security")
    print(Bright_Red + Membership + Identity + Bright_Green + CPassword_Error_msg)
    Moretime_Load()
    clearConsole()

def Nickname_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Nickname.")
    Moretime_Load()
    clearConsole()

def Nickname_Error2():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Nickname.")
    Moretime_Load()
    clearConsole()

def iD_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Org iD.")
    Moretime_Load()
    clearConsole()

def Location_Error():
    clearConsole()
    NoLoad_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Location.")
    Moretime_Load()
    clearConsole()

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

def Firewall_Error():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you Answer That Question.\n\
" + Bright_Red + "If you are not a preminum member\n\
Register to get all answers to access\n\
The Locked Version\n\
"+ BG_Bright_Cyan + Bright_Magenta + "")
    Firewall_info = "--------How To Register To CHH.Org-------"
    for char in Firewall_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")
    print(Rest + Bright_Red + "Register With Us Today\n\
To Register you must contact us\n\
At Facebook or Telegram seraching\n\
'Cryptic Hats Hackers' then inbox us.\n\
We will then register you in CHH Org as a\n\
Preminum Member;" + Bright_Cyan + "\n\
Note; You cant register in this Version!")
    Moretime_Load()
    clearConsole()

def Access_Denied():
    clearConsole()
    NoLoad_Banner2()
    print(Bright_Red + "Wrong Input Error;" + Bright_Green + "\n\
Please make sure you Answer That Question\n\
Right and other Questions as well.\n\
" + Bright_Red + "If you are not a preminum member\n\
Register to get all answers to access\n\
The Locked Version\n\
\n\
" + BG_Bright_Cyan + Bright_Magenta)
    Firewall_info = "--------How To Register To CHH.Org-------"
    for char in Firewall_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print("")
    print(Rest + Bright_Red + "Register With Us Today\n\
To Register you must contact us\n\
At Facebook or Telegram seraching\n\
'Cryptic Hats Hackers' then inbox us.\n\
We will then register you in CHH Org as a\n\
Preminum Member;" + Bright_Cyan + "\n\
Note; You cant register in this Version!")
    Moretime_Load()

def Membership_Details():
    #Logged in User Details
    User_Data = "-----Here is your Membership Details-----"
    print(BG_Bright_Cyan + Bright_Magenta)
    for char in User_Data:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(Rest +"")
    print(Bright_Red + "User iD: " + Identity)
    print("Membership: "+ Membership + Identity)
    print(Bright_Red + "Nickname: " + Nickname)
    print("Location: "+ Location)
    print("Proton Email: " + Membership + Identity + Bright_Magenta + "@" + Bright_Red + "protonmail.com")
    print("Telegram: "+ Bright_Magenta + "@" + Bright_Red + Telegram + Identity)
    print("Invited By: "+  Bright_Red + Invited_By)
    print("Registered Date: "+  Bright_Red + Registered_Date)
    print(Bright_Red + "Paying Member: " + Paying_Member)
    Security_info = "-----------Account Secret Codes----------"
    print(Rest + BG_Bright_Cyan + Bright_Magenta)
    for char in Security_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print(Rest + "" + Bright_Red)
    print("Yaaic & Element Password: "+ Identity + Location[1] + Password[0] + Location[3] + Identity[0] + Password[4] + Password[6])
    print("DarkChat Code: "+ Secret_Chat + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])
    print("Unique Code: "+ Secret + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])
    

#Unlocked Version
while True:
    clearConsole()
    Login_Banner()
    Index_Welcome_msg2()
    Answer = input(Bright_Red + "Are you registered? <(Y/N)> " + Bright_Green)
    if Answer == Binary_Firewall[0]:
        print(Bright_Red + "Please Contact Us;\n\
At https://facebook.com/chhorg or try\n\
At Https://t.me/cryptichatshackers Now...\n\
Know Register and get the Organization\n\
Password...\n\
    \n\
You Can't Register here in this version!")
        Logout_System()
        break
    elif Answer == Binary_Firewall[1]:
        print("If you are a member of the Org\n\
Please Enter The Firewall Security\n\
Details;")
        Nickname = input(Bright_Cyan + "Nickname: " + Bright_Green)
        if len(Nickname) >= 1:
            clearConsole()
            Firewall_Banner()
            print(Bright_Red + "Thank You " + Nickname + "\n\
For Coming To Study With Us!\n\
\n\
" + Bright_Green + "Please Pass Throgh To Login!")
            Login = input(Bright_Yellow + "Security Tasks;\n\
"+ Bright_Magenta + Ms1 + Bright_Red + "). When Did The Organization Start?\n\
"+ Bright_Magenta + Ms2 + Bright_Red + "). Who is the Founder Of The Org?\n\
"+ Bright_Magenta + Ms3 + Bright_Red + "). What is the Membership of The\n\
Person In The Previous Question?\n\
"+ Bright_Magenta + Ms4 + Bright_Red + "). What is the BlackDocument\n\
Secret Password for Preminum Members?\n\
"+ Bright_Magenta + Ms5 + Bright_Red + "). Who Invited You?\n\
"+ Bright_Magenta + Ms6 + Bright_Red + "). When Did you Register?\n\
"+ Bright_Magenta + Ms7 + Bright_Red + "). Are You In The Paying Members List?\n\
" + Bright_Cyan + Ms1 + "). " + Rest  + "Q1 Answer;\n\
" + Bright_Red)
            if len(Login) <=5:
                Firewall_Error()
                Logout_System()
                break
            else:
                if Login != Firewall[0]:
                    Access_Denied()
                    Logout_System()
                    break
                else:
                    Login = input(Bright_Cyan + Ms2 + "). " + Rest + "Q2 Answer;\n\
"+ Bright_Red)
                    if len(Login) <=5:
                        Firewall_Error()
                        Logout_System()
                        break
                    else:
                        if Login != Firewall[1]:
                            Access_Denied()
                            Logout_System()
                            break
                        else:
                            Login = input(Bright_Cyan + Ms3 + "). " + Rest + "Q3 Answer;\n\
"+ Bright_Red)
                            if len(Login) <=5:
                                Firewall_Error()
                                Logout_System()
                                break
                            else:
                                if Login != Firewall[2]:
                                    Access_Denied()
                                    Logout_System()
                                    break
                                else:
                                    Login = input(Bright_Cyan + Ms4 + "). " + Rest + "Q4 Answer;\n\
"+ Bright_Red)
                                    if len(Login) <=5:
                                        Firewall_Error()
                                        Logout_System()
                                        break
                                    else:
                                        if Login != Firewall[3]:
                                            Access_Denied()
                                            Logout_System()
                                            break
                                        else:
                                            Invited_By = input(Bright_Cyan + Ms5 + "). " + Rest +  "Q5 Answer;\n\
"+ Bright_Red)
                                            if len(Invited_By) <=5:
                                                Firewall_Error()
                                                Logout_System()
                                                break
                                            else:
                                                Registered_Date = input(Bright_Cyan + Ms6 + "). " + Rest +  "Q6 Answer;\n\
"+ Bright_Red)
                                                if len(Registered_Date) <=5:
                                                    Firewall_Error()
                                                    Logout_System()
                                                    break
                                                else:
                                                    Paying_Member = input(Bright_Cyan + Ms7 + "). " + Rest +  "Q7 Answer; <(Y/N)>\n\
"+ Bright_Red)
                                                    if len(Paying_Member) <=0:
                                                        Firewall_Error()
                                                        Logout_System()
                                                        break
                                                    else:
                                                        if Paying_Member == "Y":
                                                            Paying_Member = "Yes"
                                                        elif Paying_Member == "N":
                                                            Paying_Member = "No"

                                                        #The Script Loop
                                                        while True:
                                                            clearConsole()
                                                            #Banner
                                                            Login_Banner()
                                                            #Login System & Instructions
                                                            Login_System()
                                                            Identity = input(Bright_Cyan +"iD: ")
                                                            if len(Identity) > 0:
                                                                Password = input("Password: ")
                                                                if len(Password) >= 8:    
                                                                    Cpassword = input("Confirm Password: ")
                                                                    if len(Cpassword) >= 8:
                                                                        if Password == Cpassword:
                                                                            Location = input("Location: ")
                                                                            if len(Location) > 1:
                                                                                print(Dark_Blue + BG_Dark_Green + Line + Rest)
                                                                                print(Dark_Blue + BG_Dark_Green + Line + Rest)

                                                                                clearConsole() 
                                                                                Index_Banner()
                                                                                Index_Welcome_msg()
                                                                                Membership_Details()
                                                                                Main_Menu()
                                                                                Answer = input(Bright_Cyan +"Select: ")
                                                                                if Answer == DemonFireWall[0]:
                                                                                    #Updates Script
                                                                                    Updates_Page()
                                                                                    Logout_System()
                                                                                    break
                                                                                #End Part

                                                                                elif Answer == DemonFireWall[1]:
                                                                                    #VPN Files Script
                                                                                    VPN_Files()    
                                                                                    Logout_System()
                                                                                    break
                                                                                #End Part

                                                                                elif Answer == DemonFireWall[2]:
                                                                                    #Yaaic Config Script
                                                                                    Yaaic_Config()
                                                                                    break
                                                                                #End Part

                                                                                elif Answer == DemonFireWall[3]:
                                                                                    #DarkWeb Links Script
                                                                                    Darkweb_Links()
                                                                                    Logout_System()
                                                                                    break
                                                                                #End Part

                                                                                elif Answer == DemonFireWall[4]:
                                                                                    #Membership Script
                                                                                    Memberships()
                                                                                    Logout_System()
                                                                                    break
                                                                                #End Part

                                                                                elif Answer == DemonFireWall[5]:
                                                                                    #Apps Script
                                                                                    Apps()
                                                                                    Logout_System()
                                                                                    break
                                                                                #End Part

                                                                                elif Answer == DemonFireWall[6]:
                                                                                    #Hacking Lessons Script
                                                                                    Hacking_Lessons()
                                                                                    continue
                                                                                #End Part
                                                                                elif Answer == DemonFireWall[7]:
                                                                                    #Chatting Script
                                                                                    Chat_App()
                                                                                    break
                                                                                #End Part    
                                                                                
                                                                                elif Answer == DemonFireWall[8]:
                                                                                    #More Menu
                                                                                    clearConsole() 
                                                                                    #Banner
                                                                                    NoLoad_Banner()
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
                                                                                    Membership_Details()
                                                                                    More_Menu()
                                                                                    More_MenuQ = input(Bright_Cyan +"Select: ")
                                                                                    if More_MenuQ == DemonFireWall[9]:
                                                                                        #MyAccount Page
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        Membership_Details()
                                                                                        Logout_System()
                                                                                        break
                                                                                        #End Part..................................................
                                                                                    
                                                                                    elif More_MenuQ == DemonFireWall[10]:
                                                                                        #Organization Rules
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        Org_Rules()
                                                                                        Logout_System()
                                                                                        break

                                                                                        #End Line Of Rules..............................................................        
                                                                                    elif More_MenuQ == DemonFireWall[11]:
                                                                                        #About The Org
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        About_Us()
                                                                                        Logout_System()
                                                                                        break

                                                                                    elif More_MenuQ == DemonFireWall[12]:
                                                                                        #Members List Page
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        Members_List()
                                                                                        Logout_System()
                                                                                        break

                                                                                    elif More_MenuQ == DemonFireWall[13]:
                                                                                        #Script Games Page
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        Script_Games()
                                                                                        Logout_System()
                                                                                        break
                                                                                    
                                                                                    elif More_MenuQ == DemonFireWall[14]:
                                                                                        #Script Games Page
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        Org_History()
                                                                                        Logout_System()
                                                                                        break

                                                                                    elif More_MenuQ == DemonFireWall[15]:
                                                                                        #Script Games Page
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        Chat_Info()
                                                                                        Logout_System()
                                                                                        break

                                                                                    elif More_MenuQ == DemonFireWall[16]:
                                                                                        #Script Games Page
                                                                                        clearConsole()
                                                                                        NoLoad_Banner()
                                                                                        
                                                                                        Logout_System()
                                                                                        break
                                                                                    else:
                                                                                        Menu_Error()
                                                                                        continue
                                                                                else:
                                                                                    Menu_Error()
                                                                                    continue
                                                                            else:
                                                                                Location_Error()
                                                                                continue
                                                                        else:
                                                                            CPassword_Error()
                                                                            continue
                                                                            #The End Of The Script!
                                                                    else:
                                                                        CPassword_Error()
                                                                        continue
                                                                else:
                                                                    Password_Error()
                                                                    continue
                                                            else:
                                                                iD_Error()
                                                                continue
                                                           
        else:
            Nickname_Error2()
            continue