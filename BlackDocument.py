import os,sys,time
from Plugins.Configs.Settings import *

#Main Menu Pages
from Plugins.Configs.Pages.Darkweb_Links import Darkweb_Links
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
    print(BG_Bright_Cyan + Bright_Magenta)
    Security_info = "-----------Account Secret Codes-----------"
    for char in Security_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print(Rest + "" + Bright_Red)
    print("Yaaic & Element Password: "+ Identity + Location[1] + Password[0] + Location[3] + Identity[0] + Password[4] + Password[6])
    print("DarkChat Code: "+ Secret_Chat + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])
    print("Unique Code: "+ Secret + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])

#The Script Loop
while True:
    clearConsole()
    #Banner
    Login_Banner()
    #Login System & Instructions
    Login_System()
    Nickname = input(Bright_Cyan +"Nickname: ")
    if len(Nickname) > 1:
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
                            if Answer == "Updates":
                                #Updates Script
                                Updates_Page()
                                Logout_System()
                                break
                            #End Part

                            elif Answer == "VPN Files":
                                #VPN Files Script
                                VPN_Files()    
                                Logout_System()
                                break
                            #End Part

                            elif Answer == "Yaaic Config":
                                #Yaaic Config Script
                                Yaaic_Config()
                                break
                            #End Part

                            elif Answer == "Darkweb Links":
                                #DarkWeb Links Script
                                Darkweb_Links()
                                Logout_System()
                                break
                            #End Part

                            elif Answer == "Memberships":
                                #Membership Script
                                Membership()
                                Logout_System()
                                break
                            #End Part

                            elif Answer == "Apps":
                                #Apps Script
                                Apps()
                                Logout_System()
                                break
                            #End Part

                            elif Answer == "Hacking Lessons":
                                #Hacking Lessons Script
                                Hacking_Lessons()
                                continue
                            #End Part
                            elif Answer == "Chat":
                                #Chatting Script
                                Chat_App()
                                break
                            #End Part    
                            
                            elif Answer == "More":
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
                                if More_MenuQ == "MyAccount":
                                    #MyAccount Page
                                    clearConsole()
                                    NoLoad_Banner()
                                    Membership_Details()
                                    Logout_System()
                                    break
                                    #End Part..................................................
                                
                                elif More_MenuQ == "Org Rules":
                                    #Organization Rules
                                    clearConsole()
                                    NoLoad_Banner()
                                    Org_Rules()
                                    Logout_System()
                                    break

                                    #End Line Of Rules..............................................................        
                                elif More_MenuQ == "About Us":
                                    #About The Org
                                    clearConsole()
                                    NoLoad_Banner()
                                    About_Us()
                                    Logout_System()
                                    break

                                elif More_MenuQ == "Members List":
                                    #Members List Page
                                    clearConsole()
                                    NoLoad_Banner()
                                    Members_List()
                                    Logout_System()
                                    break

                                elif More_MenuQ == "Script Games":
                                    #Script Games Page
                                    clearConsole()
                                    NoLoad_Banner()
                                    Script_Games()
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
        Nickname_Error()
        continue
