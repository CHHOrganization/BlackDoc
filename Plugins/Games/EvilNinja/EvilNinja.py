import os,sys,time
from Settings import *
from Functions import *
import Functions as Config

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


#EVilNinja Data
Level_1_Names = ["Kerry", "Jackey", "Mary", "Blackey", "Melisa", "Susan"]
Level_1_Surnames = ["White", "Rockafeller", "Chinano", "Kingsley", "Martinez", "White"]
Level_1_DOBs = ["1980-12-26", "1966-03-09", "1972-06-23", "1994-08-08", "1982-11-10", "1961-06-16" ]
EL_Passwords = ["26White12", "6603Jackey", "197206Mary", "Kingsley08", "1982Martinez", "Susan1961"]

#Game Data
Trying_Again = 0
Live = 3

Index_Banner()

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
            else:
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
