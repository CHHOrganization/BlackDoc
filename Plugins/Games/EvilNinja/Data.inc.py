

    
            
                Answer = input(BG_Bright_Green + Bright_Blue + "Next Stage? <(Y|N)>" + Rest + Bright_Green + " ")
                if Answer == "Y":
                    Victims_Data = "-------Here Is The Victims Details-------"
                    print(BG_Bright_Cyan + Bright_Yellow)
                    for char in Victims_Data:
                        sys.stdout.write(char)
                        sys.stdout.flush()
                        time.sleep(0.3)
                    print(Rest +"")




                    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms3 + Bright_Red +" [Password Has 8 Char...]"+ Rest)
                    print(Bright_Green + "Name: "+ Level_1_Names[2])
                    print("Surname: "+ Level_1_Surnames[2])
                    print("Date of Birth: "+ Level_1_DOBs[2])
                    
                        Answer = input(BG_Bright_Green + Bright_Blue + "Next Stage? <(Y|N)>" + Rest + Bright_Green + " ")
                        if Answer == "Y":
                            Victims_Data = "-------Here Is The Victims Details-------"
                            print(BG_Bright_Cyan + Bright_Yellow)
                            for char in Victims_Data:
                                sys.stdout.write(char)
                                sys.stdout.flush()
                                time.sleep(0.3)
                            print(Rest +"")





                            print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms4 + Bright_Red +" [Password Has 10 Char...]"+ Rest)
                            print("Name: "+ Level_1_Names[3])
                            print("Surname: "+ Level_1_Surnames[3])
                            print("Date of Birth: "+ Level_1_DOBs[3])
                            Stage4 = input(Bright_Cyan + "Password: ")
                            if Stage4 == EL_Passwords[3]:
                                print(BG_Dark_Magenta + Bright_Yellow)
                                Stage4_msg = "            Congradulations              \n\
                You Won                  "
                                for char in Stage4_msg:
                                    sys.stdout.write(char)
                                    sys.stdout.flush()
                                    time.sleep(0.1)
                                print(Rest)
                                print(BG_Dark_Blue + "        " + Bright_Green + Stage4 + " Is Correct!           "+ Rest)
                                print("\n\
                                ")
                                Answer = input(BG_Bright_Green + Bright_Blue + "Next Stage? <(Y|N)>" + Rest + Bright_Green + " ")
                                if Answer == "Y":
                                    print("Stage 5 Locked")


#Hard Level..................................................................................................................................................................................................................
elif Answer == "Normal Level":
    Normal_Level_msg = "EvilNinja Level: Normal\n\
Note: You Only Got 2 Chances\n\
To Get This Password Right!"
    print(Bright_Red)
    for char in Easy_Level_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)

#Hard Level..................................................................................................................................................................................................................
elif Answer == "Hard Level":
    Easy_Level_msg = "EvilNinja Level: Easy\n\
Note: You Only Got 1 Chance\n\
To Get This Password Right!"
    print(Bright_Red)
    for char in Easy_Level_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)