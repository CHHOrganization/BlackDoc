import os,sys,time
from Settings import *

#EVilNinja Data
Level_1_Names = ["Kerry", "Jackey", "Mary", "Blackey", "Melisa", "Susan"]
Level_1_Surnames = ["White", "Rockafeller", "Chinano", "Kingsley", "Martinez", "White"]
Level_1_DOBs = ["1980-12-26", "1966-03-09", "1972-06-23", "1994-08-08", "1982-11-10", "1961-06-16" ]
EL_Passwords = ["26White12", "6603Jackey", "197206Mary", "Kingsley08", "1982Martinez", "Susan1961"]

Level_2_Names = ["Kerry", "Jackey", "Mary", "Blackey", ""]
Level_2_Surnames = ["White", "Rockafeller", "Chinano", "Kingsley"]
Level_2_DOBs = ["1980-12-26", "1966-03-09", "1972-06-23", "1994-08-08" ]
NL_Passwords = ["26White12", "6603Jackey", "197206Mary", "Kingsley08"]

Level_3_Names = ["Kerry", "Jackey", "Mary", "Blackey", ""]
Level_3_Surnames = ["White", "Rockafeller", "Chinano", "Kingsley"]
Level_3_DOBs = ["1980-12-26", "1966-03-09", "1972-06-23", "1994-08-08" ]
HL_Passwords = ["26White12", "6603Jackey", "197206Mary", "Kingsley08"]

#Victims data dashborad hader
def Victims_DDB():
    Victims_Data = "-------Here Is The Victims Details-------"
    print(BG_Bright_Cyan + Bright_Yellow)
    for char in Victims_Data:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(Rest +"")

#Victims data for Easy Levels
def Victims_Data_ELS1():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms1 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[0])
    print("Surname: "+ Level_1_Surnames[0])
    print("Date of Birth: "+ Level_1_DOBs[0])

def Victims_Data_ELS2():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms2 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[1])
    print("Surname: "+ Level_1_Surnames[1])
    print("Date of Birth: "+ Level_1_DOBs[1])

def Victims_Data_ELS3():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms3 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[2])
    print("Surname: "+ Level_1_Surnames[2])
    print("Date of Birth: "+ Level_1_DOBs[2])

def Victims_Data_ELS4():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms4 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[3])
    print("Surname: "+ Level_1_Surnames[3])
    print("Date of Birth: "+ Level_1_DOBs[3])

def Victims_Data_ELS5():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms5 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[4])
    print("Surname: "+ Level_1_Surnames[4])
    print("Date of Birth: "+ Level_1_DOBs[4])

def Victims_Data_ELS6():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms6 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[5])
    print("Surname: "+ Level_1_Surnames[5])
    print("Date of Birth: "+ Level_1_DOBs[5])

def Victims_Data_ELS7():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms7 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[6])
    print("Surname: "+ Level_1_Surnames[6])
    print("Date of Birth: "+ Level_1_DOBs[6])

def Victims_Data_ELS8():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms8 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[7])
    print("Surname: "+ Level_1_Surnames[7])
    print("Date of Birth: "+ Level_1_DOBs[7])

def Victims_Data_ELS9():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms9 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[8])
    print("Surname: "+ Level_1_Surnames[8])
    print("Date of Birth: "+ Level_1_DOBs[8])

def Victims_Data_ELS10():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms10 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[9])
    print("Surname: "+ Level_1_Surnames[9])
    print("Date of Birth: "+ Level_1_DOBs[9])

def Victims_Data_ELS11():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms11 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[10])
    print("Surname: "+ Level_1_Surnames[10])
    print("Date of Birth: "+ Level_1_DOBs[10])

def Victims_Data_ELS12():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms12 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[11])
    print("Surname: "+ Level_1_Surnames[11])
    print("Date of Birth: "+ Level_1_DOBs[11])

def Victims_Data_ELS13():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms13 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[12])
    print("Surname: "+ Level_1_Surnames[12])
    print("Date of Birth: "+ Level_1_DOBs[12])

def Victims_Data_ELS14():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms14 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[13])
    print("Surname: "+ Level_1_Surnames[13])
    print("Date of Birth: "+ Level_1_DOBs[13])

def Victims_Data_ELS15():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms15 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[14])
    print("Surname: "+ Level_1_Surnames[14])
    print("Date of Birth: "+ Level_1_DOBs[14])

def Victims_Data_ELS16():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms16 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[15])
    print("Surname: "+ Level_1_Surnames[15])
    print("Date of Birth: "+ Level_1_DOBs[15])

def Victims_Data_ELS17():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms17 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[16])
    print("Surname: "+ Level_1_Surnames[16])
    print("Date of Birth: "+ Level_1_DOBs[16])

def Victims_Data_ELS18():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms18 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[17])
    print("Surname: "+ Level_1_Surnames[17])
    print("Date of Birth: "+ Level_1_DOBs[17])

def Victims_Data_ELS19():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms19 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[18])
    print("Surname: "+ Level_1_Surnames[18])
    print("Date of Birth: "+ Level_1_DOBs[18])

def Victims_Data_ELS20():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms20 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[19])
    print("Surname: "+ Level_1_Surnames[19])
    print("Date of Birth: "+ Level_1_DOBs[19])

def Victims_Data_ELS21():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms21 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[20])
    print("Surname: "+ Level_1_Surnames[20])
    print("Date of Birth: "+ Level_1_DOBs[20])

def Victims_Data_ELS22():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms22 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[21])
    print("Surname: "+ Level_1_Surnames[21])
    print("Date of Birth: "+ Level_1_DOBs[21])

def Victims_Data_ELS23():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms23 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[22])
    print("Surname: "+ Level_1_Surnames[22])
    print("Date of Birth: "+ Level_1_DOBs[22])

def Victims_Data_ELS24():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms24 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[23])
    print("Surname: "+ Level_1_Surnames[23])
    print("Date of Birth: "+ Level_1_DOBs[23])

def Victims_Data_ELS25():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms25 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[24])
    print("Surname: "+ Level_1_Surnames[24])
    print("Date of Birth: "+ Level_1_DOBs[24])

def Victims_Data_ELS26():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms26 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[25])
    print("Surname: "+ Level_1_Surnames[25])
    print("Date of Birth: "+ Level_1_DOBs[25])

def Victims_Data_ELS27():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms27 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[26])
    print("Surname: "+ Level_1_Surnames[26])
    print("Date of Birth: "+ Level_1_DOBs[26])

def Victims_Data_ELS28():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms28 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[27])
    print("Surname: "+ Level_1_Surnames[27])
    print("Date of Birth: "+ Level_1_DOBs[27])

def Victims_Data_ELS29():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms29 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[28])
    print("Surname: "+ Level_1_Surnames[28])
    print("Date of Birth: "+ Level_1_DOBs[28])

def Victims_Data_ELS30():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms30 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[29])
    print("Surname: "+ Level_1_Surnames[29])
    print("Date of Birth: "+ Level_1_DOBs[29])

def Victims_Data_ELS31():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms31 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[30])
    print("Surname: "+ Level_1_Surnames[30])
    print("Date of Birth: "+ Level_1_DOBs[30])

def Victims_Data_ELS32():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms32 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[31])
    print("Surname: "+ Level_1_Surnames[31])
    print("Date of Birth: "+ Level_1_DOBs[31])

def Victims_Data_ELS33():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms33 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[32])
    print("Surname: "+ Level_1_Surnames[32])
    print("Date of Birth: "+ Level_1_DOBs[32])

def Victims_Data_ELS34():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms34 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[33])
    print("Surname: "+ Level_1_Surnames[33])
    print("Date of Birth: "+ Level_1_DOBs[33])

def Victims_Data_ELS35():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms35 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[34])
    print("Surname: "+ Level_1_Surnames[34])
    print("Date of Birth: "+ Level_1_DOBs[34])


#Victims data for Normal Levels
def Victims_Data_NLS1():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms1 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[0])
    print("Surname: "+ Level_2_Surnames[0])
    print("Date of Birth: "+ Level_2_DOBs[0])

def Victims_Data_NLS2():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms2 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[1])
    print("Surname: "+ Level_2_Surnames[1])
    print("Date of Birth: "+ Level_2_DOBs[1])

def Victims_Data_NLS3():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms3 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[2])
    print("Surname: "+ Level_2_Surnames[2])
    print("Date of Birth: "+ Level_2_DOBs[2])

def Victims_Data_NLS4():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms4 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[3])
    print("Surname: "+ Level_2_Surnames[3])
    print("Date of Birth: "+ Level_2_DOBs[3])

def Victims_Data_NLS5():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms5 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[4])
    print("Surname: "+ Level_2_Surnames[4])
    print("Date of Birth: "+ Level_2_DOBs[4])

def Victims_Data_NLS6():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms6 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[5])
    print("Surname: "+ Level_2_Surnames[5])
    print("Date of Birth: "+ Level_2_DOBs[5])

def Victims_Data_NLS7():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms7 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[6])
    print("Surname: "+ Level_2_Surnames[6])
    print("Date of Birth: "+ Level_2_DOBs[6])

def Victims_Data_NLS8():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms8 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[7])
    print("Surname: "+ Level_2_Surnames[7])
    print("Date of Birth: "+ Level_2_DOBs[7])

def Victims_Data_NLS9():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms9 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[8])
    print("Surname: "+ Level_2_Surnames[8])
    print("Date of Birth: "+ Level_2_DOBs[8])

def Victims_Data_NLS10():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms10 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[9])
    print("Surname: "+ Level_2_Surnames[9])
    print("Date of Birth: "+ Level_2_DOBs[9])

def Victims_Data_NLS11():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms11 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[10])
    print("Surname: "+ Level_2_Surnames[10])
    print("Date of Birth: "+ Level_2_DOBs[10])

def Victims_Data_NLS12():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms12 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[11])
    print("Surname: "+ Level_2_Surnames[11])
    print("Date of Birth: "+ Level_2_DOBs[11])

def Victims_Data_NLS13():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms13 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[12])
    print("Surname: "+ Level_2_Surnames[12])
    print("Date of Birth: "+ Level_2_DOBs[12])

def Victims_Data_NLS14():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms14 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[13])
    print("Surname: "+ Level_2_Surnames[13])
    print("Date of Birth: "+ Level_2_DOBs[13])

def Victims_Data_NLS15():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms15 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[14])
    print("Surname: "+ Level_2_Surnames[14])
    print("Date of Birth: "+ Level_2_DOBs[14])

def Victims_Data_NLS16():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms16 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[15])
    print("Surname: "+ Level_2_Surnames[15])
    print("Date of Birth: "+ Level_2_DOBs[15])

def Victims_Data_NLS17():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms17 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[16])
    print("Surname: "+ Level_2_Surnames[16])
    print("Date of Birth: "+ Level_2_DOBs[16])

def Victims_Data_NLS18():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms18 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[17])
    print("Surname: "+ Level_2_Surnames[17])
    print("Date of Birth: "+ Level_2_DOBs[17])

def Victims_Data_NLS19():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms19 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[18])
    print("Surname: "+ Level_2_Surnames[18])
    print("Date of Birth: "+ Level_2_DOBs[18])

def Victims_Data_NLS20():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms20 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[19])
    print("Surname: "+ Level_2_Surnames[19])
    print("Date of Birth: "+ Level_2_DOBs[19])

def Victims_Data_NLS21():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms21 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[20])
    print("Surname: "+ Level_2_Surnames[20])
    print("Date of Birth: "+ Level_2_DOBs[20])

def Victims_Data_NLS22():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms22 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[21])
    print("Surname: "+ Level_2_Surnames[21])
    print("Date of Birth: "+ Level_2_DOBs[21])

def Victims_Data_NLS23():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms23 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[22])
    print("Surname: "+ Level_2_Surnames[22])
    print("Date of Birth: "+ Level_2_DOBs[22])

def Victims_Data_NLS24():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms24 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[23])
    print("Surname: "+ Level_2_Surnames[23])
    print("Date of Birth: "+ Level_2_DOBs[23])

def Victims_Data_NLS25():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms25 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[24])
    print("Surname: "+ Level_2_Surnames[24])
    print("Date of Birth: "+ Level_2_DOBs[24])

def Victims_Data_NLS26():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms26 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[25])
    print("Surname: "+ Level_2_Surnames[25])
    print("Date of Birth: "+ Level_2_DOBs[25])

def Victims_Data_NLS27():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms27 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[26])
    print("Surname: "+ Level_2_Surnames[26])
    print("Date of Birth: "+ Level_2_DOBs[26])

def Victims_Data_NLS28():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms28 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[27])
    print("Surname: "+ Level_2_Surnames[27])
    print("Date of Birth: "+ Level_2_DOBs[27])

def Victims_Data_NLS29():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms29 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[28])
    print("Surname: "+ Level_2_Surnames[28])
    print("Date of Birth: "+ Level_2_DOBs[28])

def Victims_Data_NLS30():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms30 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[29])
    print("Surname: "+ Level_2_Surnames[29])
    print("Date of Birth: "+ Level_2_DOBs[29])

def Victims_Data_NLS31():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms31 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[30])
    print("Surname: "+ Level_2_Surnames[30])
    print("Date of Birth: "+ Level_2_DOBs[30])

def Victims_Data_NLS32():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms32 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[31])
    print("Surname: "+ Level_2_Surnames[31])
    print("Date of Birth: "+ Level_2_DOBs[31])

def Victims_Data_NLS33():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms33 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[32])
    print("Surname: "+ Level_2_Surnames[32])
    print("Date of Birth: "+ Level_2_DOBs[32])

def Victims_Data_NLS34():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms34 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[33])
    print("Surname: "+ Level_2_Surnames[33])
    print("Date of Birth: "+ Level_2_DOBs[33])

def Victims_Data_NLS35():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms35 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[34])
    print("Surname: "+ Level_2_Surnames[34])
    print("Date of Birth: "+ Level_2_DOBs[34])

#Victims data for Hard Levels
def Victims_Data_HLS1():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms1 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[0])
    print("Surname: "+ Level_2_Surnames[0])
    print("Date of Birth: "+ Level_2_DOBs[0])

def Victims_Data_HLS2():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms2 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[1])
    print("Surname: "+ Level_2_Surnames[1])
    print("Date of Birth: "+ Level_2_DOBs[1])

def Victims_Data_HLS3():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms3 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[2])
    print("Surname: "+ Level_2_Surnames[2])
    print("Date of Birth: "+ Level_2_DOBs[2])

def Victims_Data_HLS4():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms4 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_2_Names[3])
    print("Surname: "+ Level_2_Surnames[3])
    print("Date of Birth: "+ Level_2_DOBs[3])

def Victims_Data_HLS5():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms5 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[4])
    print("Surname: "+ Level_2_Surnames[4])
    print("Date of Birth: "+ Level_2_DOBs[4])

def Victims_Data_HLS6():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms6 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[5])
    print("Surname: "+ Level_2_Surnames[5])
    print("Date of Birth: "+ Level_2_DOBs[5])

def Victims_Data_HLS7():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms7 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[6])
    print("Surname: "+ Level_2_Surnames[6])
    print("Date of Birth: "+ Level_2_DOBs[6])

def Victims_Data_HLS8():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms8 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[7])
    print("Surname: "+ Level_2_Surnames[7])
    print("Date of Birth: "+ Level_2_DOBs[7])

def Victims_Data_HLS9():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms9 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[8])
    print("Surname: "+ Level_2_Surnames[8])
    print("Date of Birth: "+ Level_2_DOBs[8])

def Victims_Data_HLS10():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms10 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[9])
    print("Surname: "+ Level_2_Surnames[9])
    print("Date of Birth: "+ Level_2_DOBs[9])

def Victims_Data_HLS11():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms11 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[10])
    print("Surname: "+ Level_2_Surnames[10])
    print("Date of Birth: "+ Level_2_DOBs[10])

def Victims_Data_HLS12():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms12 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[11])
    print("Surname: "+ Level_2_Surnames[11])
    print("Date of Birth: "+ Level_2_DOBs[11])

def Victims_Data_HLS13():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms13 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[12])
    print("Surname: "+ Level_2_Surnames[12])
    print("Date of Birth: "+ Level_2_DOBs[12])

def Victims_Data_HLS14():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms14 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[13])
    print("Surname: "+ Level_2_Surnames[13])
    print("Date of Birth: "+ Level_2_DOBs[13])

def Victims_Data_HLS15():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms15 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[14])
    print("Surname: "+ Level_2_Surnames[14])
    print("Date of Birth: "+ Level_2_DOBs[14])

def Victims_Data_HLS16():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms16 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[15])
    print("Surname: "+ Level_2_Surnames[15])
    print("Date of Birth: "+ Level_2_DOBs[15])

def Victims_Data_HLS17():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms17 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[16])
    print("Surname: "+ Level_2_Surnames[16])
    print("Date of Birth: "+ Level_2_DOBs[16])

def Victims_Data_HLS18():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms18 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[17])
    print("Surname: "+ Level_2_Surnames[17])
    print("Date of Birth: "+ Level_2_DOBs[17])

def Victims_Data_HLS19():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms19 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[18])
    print("Surname: "+ Level_2_Surnames[18])
    print("Date of Birth: "+ Level_2_DOBs[18])

def Victims_Data_HLS20():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms20 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[19])
    print("Surname: "+ Level_2_Surnames[19])
    print("Date of Birth: "+ Level_2_DOBs[19])

def Victims_Data_HLS21():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms21 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[20])
    print("Surname: "+ Level_2_Surnames[20])
    print("Date of Birth: "+ Level_2_DOBs[20])

def Victims_Data_HLS22():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms22 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[21])
    print("Surname: "+ Level_2_Surnames[21])
    print("Date of Birth: "+ Level_2_DOBs[21])

def Victims_Data_HLS23():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms23 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[22])
    print("Surname: "+ Level_2_Surnames[22])
    print("Date of Birth: "+ Level_2_DOBs[22])

def Victims_Data_HLS24():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms24 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[23])
    print("Surname: "+ Level_2_Surnames[23])
    print("Date of Birth: "+ Level_2_DOBs[23])

def Victims_Data_HLS25():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms25 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[24])
    print("Surname: "+ Level_2_Surnames[24])
    print("Date of Birth: "+ Level_2_DOBs[24])

def Victims_Data_HLS26():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms26 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[25])
    print("Surname: "+ Level_2_Surnames[25])
    print("Date of Birth: "+ Level_2_DOBs[25])

def Victims_Data_HLS27():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms27 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[26])
    print("Surname: "+ Level_2_Surnames[26])
    print("Date of Birth: "+ Level_2_DOBs[26])

def Victims_Data_HLS28():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms28 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[27])
    print("Surname: "+ Level_2_Surnames[27])
    print("Date of Birth: "+ Level_2_DOBs[27])

def Victims_Data_HLS29():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms29 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[28])
    print("Surname: "+ Level_2_Surnames[28])
    print("Date of Birth: "+ Level_2_DOBs[28])

def Victims_Data_HLS30():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms30 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[29])
    print("Surname: "+ Level_2_Surnames[29])
    print("Date of Birth: "+ Level_2_DOBs[29])

def Victims_Data_HLS31():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms31 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[30])
    print("Surname: "+ Level_2_Surnames[30])
    print("Date of Birth: "+ Level_2_DOBs[30])

def Victims_Data_HLS32():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms32 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[31])
    print("Surname: "+ Level_2_Surnames[31])
    print("Date of Birth: "+ Level_2_DOBs[31])

def Victims_Data_HLS33():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms33 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[32])
    print("Surname: "+ Level_2_Surnames[32])
    print("Date of Birth: "+ Level_2_DOBs[32])

def Victims_Data_HLS34():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms34 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[33])
    print("Surname: "+ Level_2_Surnames[33])
    print("Date of Birth: "+ Level_2_DOBs[33])

def Victims_Data_HLS35():
    print(BG_Bright_Blue + Bright_Red + "[+] ->" + Bright_Yellow + " Stage " + Ms35 + Bright_Red +" [Password Has 9 Char...]  "+ Rest)
    print(Bright_Green + "Name: "+ Level_1_Names[34])
    print("Surname: "+ Level_2_Surnames[34])
    print("Date of Birth: "+ Level_2_DOBs[34])

#Stage 1 In Easy Level
def ELStage1():
    Stage1 = input(Bright_Cyan + "Password: ")
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
        print("\n\
        ")

#Trying Again Config
def Try_Again():
    print(Bright_Red + "You Running out of lucks.")
    Trying_Again += 1
    if Trying_Again == 3:
        GameOver = "GameOver\n\
Try Better Next Time."
        print(BG_Bright_Cyan + Bright_Red + "")
        for char in GameOver:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
            break
    

        