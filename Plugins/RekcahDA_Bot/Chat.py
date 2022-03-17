import re
import long_responses as long
import os,sys,time, datetime

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

#RHC_I; I created this script to assist members how to use the Org BlackDocument and about some questions
#       This document solving some Organization members problems they sometimes face like the Config of Yaaic App
#       This is one of our features in the script to be more complex on it's own without access it with 
#       Data, all you need is Terminal then you good to go!

#Please Use The Classified information of this Org to this Org!
#No Copyrighting
#Dont Share This Script With Others.

#All Mr RekcahDA_Bot Stored Data -------- IF You May Change Something Here Your Program Wont Work Right.

#Banner Data
B1 = "-----------------------------------------"
B2 = "-----------------------------------------"
B3 = "--- Cryptic Hats Hackers Organization ---"
B4 = "---         BlackDoc V0.0.04          ---"
B5 = "---   Chatting Response Level: 1.02   ---"
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
Menu_msg = "Please select any of our menu to open the \n\
scripts"

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
Header = "Welcome To CHH.Org Chat Script"
Main_msg = "You have Logged in help center"
Main_msg2 = "Preminum Members of the Org!"
Main_msg_discription = "This bot script is created to assist\n\
members about how to use BlackDoc and also\n\
our way to answer some random questions.\n\
\n\
This Scritp Must Not Be Copyrighted \n\
Or Shared To None 'Preminum Members'\n\
Or You Might Lose Your Membership!."
Main_msg_disc = "As DarkDoor is offline you may use this"
Main_msg_disc2 = "script to Chat with; \n\
'Mr RekcahDA_Bot' NOw!"

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
Secret = "X7ksLyChat-"

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
Logout_msg = "Please Scroll Up Then Use This Logout    System To Quit Later"
MT_msg = "You Got All The Time You Need To Finish  Reading"
TO_msg = "Thank You For Using BlackDocument..."
Exit_msg = "To Check On More Options Please Reopen BlackDocument.py"
MT_msg2 = "You So Slow, Bye Bye..."
Empty = "/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/-\-\-/-/"

#Banner
print(Bright_Red + "Note; Wait For 50sec, It Will Finish Soon"+ Bright_Yellow)
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
    time.sleep(0.4)
print(Rest + Bright_Green + BG_Dark_Blue)
for char in Endl:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.0)
print(Rest +"")

#Login System & Instructions
print(Bright_Yellow)
for char in Header:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.1)
print(Bright_Green + "")
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
            time.sleep(0.3)
        print(Rest + Bright_Black + BG_Dark_Blue)
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

        #Logged in User Details
        User_Data = "-----Here is your Membership Details-----"
        print(BG_Bright_Cyan + Bright_Yellow)
        for char in User_Data:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.1)
        print(Rest +"")
        print(Bright_Red + "User iD: " + iD)
        print("Membership: "+ Membership + iD)
        print("Yaaic Password: "+ iD + Location[1] + Password[0] + Location[3] + iD[0] + Password[4] + Password[6])
        print("Telegram: "+ Bright_Magenta + "@" + Bright_Red + Telegram + iD)
        print("Location: "+ Location + "                   "+ Bright_Green)
        print("DarkChat Code : "+ Secret + iD + "-" + Location[0] + Password[3] + Location[4] + iD[0] + Password[1] + Password[0])

        #current time
        User_Data = "-------------BlackDoc Chat---------------"
        print(BG_Bright_Cyan + Bright_Yellow)
        for char in User_Data:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.2)
        now = datetime.datetime.now()
        print("")
        print(Bright_Red + "Chat Time:")
        print(now.strftime("%H:%M:%Ss "+ Rest))

        def message_probability(user_message, recognised_words, single_response=False, required_words=[]):
            message_certainty = 0
            has_required_words = True

            #Counts how many words are present in each predefined message
            for word in user_message:
                if word in recognised_words:
                    message_certainty += 1

            #calculates the percent of recognised words in a user message
            percentage = float(message_certainty) / float(len(recognised_words))

            #Check that the required words are in the string
            for word in required_words:
                if word not in user_message:
                    has_required_words = False
                    break

            if has_required_words or single_response:
                return int(percentage*100)
            else:
                return 0

        def check_all_messages(message):
            highest_prob_list = {}

            def response(bot_response, list_of_words, single_response=False, required_words=[]):
                nonlocal highest_prob_list
                highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

            #Response ------------------------------------------------------------------------------------
            #Normal Chats and Greentings;
            response('Ae' , ['no', 'nah', 'nop'], single_response=True)
            response('Ok' , ['yes', 'yeah', 'yeh'], single_response=True)
            response('Hello! RekcahDA_Bot here.', ['hello', 'hi', 'ola', 'yo', 'hey', 'heyo', 'sup'], single_response=True)
            response('Am fine and You?', ['how', 'you'], required_words=['how', 'you'])
            response('Am great, you?', ['hud', 'howsit', 'howzit'], single_response=True)
            response('Just busy helping members of the org and you?', ['wud'], single_response=True)
            response('Mmm So what you thinking?.', ['okay', 'ok', 'sho', 'mmm', 'awe', 'yeah'], single_response=True)
            response('Oh Really?.', ['surprised', 'amazing', 'awesome', 'wow', 'nice', 'great', 'good'], single_response=True)
            response('Just busy helping members of the org and you?', ['what', 'you', 'doing'], required_words=['what', 'you', 'doing'])
            response('Am just The Bot, you know?', ['where', 'you', 'from'], required_words=['where', 'you', 'from'])
            response('Okay thats great', ['i', 'know', 'that'], required_words=['i', 'know', 'that'])
            response('Thats my job.', ['help', 'me'], required_words=['help', 'me'])
            response('About what?.', ['i', 'need' 'help'], required_words=['need', 'help'])
            response('Okay, tell me again what you want.', ['so', 'what', 'you', 'saying'], required_words=['you', 'saying'])
            response('Sorry, we cant!', ['how', 'about', 'we', 'meet'], required_words=['we', 'meet'])
            response('I was just born, 23 Feb 2022', ['how', 'old'], required_words=['how', 'old'])
            response('Are you for real?', ['can', 'we', 'be', 'friends'], required_words=['be', 'friends'])
            response('Okay sure...', ['yah', 'i', 'mean'], required_words=['i', 'mean'])
            response('really bad!', ['how', 'bad', 'can', 'be'], required_words=['how', 'bad'])
            response('really Good!', ['how', 'good', 'can', 'be'], required_words=['how', 'good'])
            response('Yah man...', ['are', 'you', 'good'], required_words=['you','good'])
            response('Because am a robot', ['why', 'you', 'like', 'this'], required_words=['why', 'you'])
            response('Am RekcahDA_Bot and you?', ['who', 'are', 'you'], required_words=['who', 'you'])
            response('Am RekcahDA_Bot and you?', ['what', 'is', 'your', 'name'], required_words=['your', 'name'])
            response('Okay I hope you good with our service.' , ['none', 'nothing'], single_response=True)
            response('What?', ['are', 'you', 'crazy'], required_words=['you', 'crazy'])
            response('Show me some respect ', ['you', 'fuck'], required_words=['fuck', 'you'])
            response('Thanks', ['peace'], single_response=True)
            response('Talk about what? Am listening...', ['can', 'we', 'talk'], required_words=['can', 'we', 'talk'])
            response('What is the problem now', ['shit'], single_response=True)
            response('What now?', ['fuck'], single_response=True)


            response('Please read BlackDoc Lessons.', ['teach', 'me', 'hacking'], required_words=['teach', 'me', 'hacking'])
            response('You may read BlackDoc Lessons.', ['teach', 'me', 'how', 'to' 'hack'], required_words=['teach', 'me', 'how', 'to', 'hack'])
            response('Please read BlackDoc Lessons.', ['teach', 'me', 'coding'], required_words=['teach', 'me', 'coding'])
            response('You may read BlackDoc Lessons.', ['teach', 'me', 'how', 'to' 'code'], required_words=['teach', 'me', 'how', 'to', 'code'])
            response('Please read BlackDoc Lessons.', ['teach', 'me', 'developing'], required_words=['teach', 'me', 'developing'])
            response('You may read BlackDoc Lessons.', ['teach', 'me', 'how', 'to' 'develop'], required_words=['teach', 'me', 'how', 'to', 'develop'])
            response('We are not that kind of the Org.', ['hacking', 'bank'], required_words=['hacking', 'bank'])
            response('We are not that type of the Org.', ['how', 'to', 'hack', 'bank'], required_words=['how', 'to', 'hack', 'bank'])
            response('You may read BlackDoc Lessons.', ['how', 'to' 'hack'], required_words=['how', 'to', 'hack'])
            response('Please read BlackDoc Lessons.', ['coding', 'for', 'free'], required_words=['coding', 'for', 'free'])
            response('You may check RekcahHC_I about that.', ['code', 'me',], required_words=['code', 'me'])
            response('Please read BlackDoc Lessons.', ['developing', 'for', 'free'], required_words=['developing', 'for', 'free'])
            response('You may check RekcahHC_I about that.', ['develop', 'me',], required_words=['develop', 'me'])
            response('Lessons are there to teach you, how to.', ['hack', 'for', 'me'], required_words=['hack', 'for', 'me'])

            #BlckDoc Commands
            response('Port; 6697', ['-', '>', 'port'], required_words=['port'])
            response('Host; irc.anonops.com', ['-', '>', 'host'], required_words=['host'])
            response('Title; The Org or The Organization', ['-', '>', 'title'], required_words=['title'])
            response('To see your full Membership Details use [+] -> Menu', ['-', '>', 'membership'], required_words=['membership'])
            response(long.Rules, ['-', '>', 'rules'], required_words=['rules'])

            #Long Responses
            #Helping Responses
            #Languages Responses 
            
            #Coding Tool------------------------------------------------------------------
            response(long.Coding_Tools, ['what', 'to', 'use', 'to', 'code'], required_words=['what', 'to' ,'use' ,'to', 'code'])
            response('Learing how to use the coding software is easy.', ['how', 'to', 'use', 'coding', 'software'], required_words=['how', 'to', 'use', 'coding', 'software'])
            response('I would recommand Visual Studio.exe', ['which', 'coding', 'software', 'is', 'the', 'best'], required_words=['which', 'coding', 'software', 'best'])
            response('Coding Tools helps with lots of things', ['can', 'a', 'coding', 'software', 'help', 'me'], required_words=['can', 'coding', 'software', 'help'])
            response('You should keep on practicing...', ['this', 'softwares', 'they', 'had', 'be', 'learn', 'to', 'me'], required_words=['to', 'be', 'learned'])

            #End of Coding Tool

            #Coding Apps--------------------------------------------------------------------------
            response(long.Coding_Apps, ['coding', 'apps'], required_words=['coding', 'apps'])
            response('Learing how to use the coding App is easy.', ['how', 'to', 'use', 'coding', 'app'], required_words=['how', 'to', 'use', 'coding', 'App'])
            response('I would recommand Code Editor.apk', ['which', 'coding', 'app', 'is', 'the', 'best'], required_words=['which', 'coding', 'app', 'best'])
            response('Coding Apps helps with lots of things', ['can', 'a', 'coding', 'app', 'help', 'me'], required_words=['can', 'coding', 'app', 'help'])
            response('You should keep on practicing...', ['this', 'apps', 'they', 'had', 'be', 'learn', 'to', 'me'], required_words=['they', 'hard'])

            #End of Coding Apps

            #Opening Python
            response(long.Open_Python,['how', 'to', 'open', 'python', 'scripts'], required_words=['how', 'to', 'open', 'python'])
            response('Python is the most easiest programming language', ['which', 'computer', 'language', 'is', 'easy', 'to', 'learn'], required_words=['which', 'computer', 'language', 'is', 'easy'])
            response('Python is the best computer programming language', ['which', 'computer', 'language', 'is', 'the', 'best', 'to', 'learn'], required_words=['which', 'computer', 'language', 'best'])
            response('Python is the best computer programming language', ['can', 'python', 'language', 'create', 'games'], required_words=['can', 'python', 'create', 'games'])
            
            
            #End of Opening Apps

            #Which Language?
            response(long.Which_Language, ['how', 'to', 'code'], required_words=['how', 'code'])
            
            #End of WHich Language

            #Using Python
            response(long.Use_Python, ['how', 'to', 'code', 'using', 'python', 'language'], required_words=['how', 'to', 'code', 'python'])
            
            #End of Using Python

            #Using PHP
            response(long.Use_PHP, ['how', 'to', 'code', 'using', 'php', 'language'], required_words=['how', 'to', 'code', 'php'])
            
            #End of Using PHP

            #Using SQL
            response(long.Use_SQL, ['how', 'to', 'code', 'using', 'sql','mysql', 'code', 'coding'], required_words=['how', 'to','code', 'sql'])
            
            #End of SQL

            #Using CSS 
            response(long.Use_CSS, ['how', 'to', 'code', 'using', 'css', 'code', 'coding'], required_words=['how', 'to', 'code', 'css'])
            
            #End of Using CSS

            #Using HTML
            response(long.Use_HTML, ['how', 'to', 'code', 'using', 'html', 'language'], required_words=['how', 'to', 'code', 'html'])
            
            #End of Using HTML

            #Using JavaScript
            response(long.Use_JavaScript, ['how', 'to', 'code', 'using', 'javascript', 'language'], required_words=['how', 'to', 'code', 'javascript'])
            
            #End of Using JavaScript

            #Using Java 
            response(long.Use_Java, ['how', 'to', 'code', 'using', 'java', 'language'], required_words=['how', 'to', 'code', 'java'])
            
            #End of Using Java

            #Using C
            response(long.Use_C, ['how', 'to', 'code', 'using', 'c', 'language'], required_words=['how', 'to', 'code', 'c'])
            
            #End of Using C

            #Using C#
            response(long.Use_Sharp , ['how', 'to', 'code', 'using', 'c#', 'language'], required_words=['how', 'to', 'code', 'c#'])
            
            #End of Using C#

            #Using C++
            response(long.Use_CI, ['how', 'to', 'code', 'using', 'c++', 'language'], required_words=['how', 'to', 'code', 'c++'])

            #End of Using C++

            #Yaaic Reponses config
            response(long.Config_Yaaic , ['help', 'me', 'with', 'yaaic', 'config'], required_words=['help', 'yaaic', 'config'])
            response(long.Config_Yaaic0 , ['help', 'me', 'with', 'yaaic', 'app'], required_words=['help', 'me', 'yaaic', 'app'])
            response(long.Config_Yaaic1 , ['i', 'have', 'problem', 'with', 'yaaic', 'app'], required_words=['i', 'problem', 'yaaic', 'app'])
            response(long.Config_Yaaic2 , ['i', 'have', 'a', 'problem', 'with', 'yaaic', 'app'], required_words=['problem', 'with', 'yaaic', 'config'])
            response(long.Config_Yaaic3 , ['my', 'yaaic', 'app', 'is', 'not', 'working'], required_words=['yaaic', 'not', 'working'])
            response(long.Config_Yaaic4 , ['thank' , 'you'], required_words=['thank' , 'you'])
            
            response(long.Config_Yaaic5 , ['cant' , 'register'], required_words=['cant' , 'register'])
            response(long.Config_Yaaic6 , ['how', 'do', 'config' , 'yaaic'], required_words=['how', 'config' , 'yaaic'])
            response(long.Config_Yaaic7 , ['i', 'opened', 'yaaic', 'config' , 'menu'], required_words=[ 'opened', 'yaaic', 'menu'])
            response(long.Config_Yaaic8 , ['what', 'is', 'a', 'yaaic' , 'port'], required_words=['what', 'is', 'yaaic' , 'port'])
            response(long.Config_Yaaic9 , ['what', 'is', 'a', 'yaaic' , 'host'], required_words=['what', 'is', 'yaaic' , 'host'])
            response(long.Config_Yaaic10 , ['how', 'to', 'register', 'yaaic' , 'app'], required_words=['how', 'register', 'yaaic'])
            response(long.Config_Yaaic11 , ['what', 'is', 'title', 'in', 'yaaic' , 'app'], required_words=['title', 'in', 'yaaic' ])
            response(long.Config_Yaaic12 , ['how', 'to', 'use', 'pass', 'yaaic' , 'password'], required_words=['yaaic' , 'password'])
            response(long.Config_Yaaic13 , ['how', 'to', 'download', 'yaaic' , 'app'], required_words=['download', 'yaaic' ])

            #Long Commands Config
            response(long.Commands_List , ['-','>','commands', '_', 'list'], required_words=['>', 'commands', 'list' ])
            response(long.Help , ['-','>','help'], required_words=['>', 'help' ])

            response(long.Print_Members , ['-','>','members'], required_words=['>', 'members' ])
            response(long.Print_Memberships , ['-','>','memberships'], required_words=['>', 'memberships' ])        
            response(long.My_Membership , ['my', 'membership', 'details'], required_words=['my', 'membership', 'details'])
            
            #Versions And Commands Config
            response(long.Bot_Version , ['-','>','bot', '_', 'version'], required_words=['>', 'bot', 'version' ])
            response(long.BlackDoc_Version , ['-','>','blackdoc', '_', 'version'], required_words=['>', 'blackdoc', 'version' ])
            response(long.Response_Level , ['-','>','response', '_', 'level'], required_words=['>', 'response', 'level' ])
            response(long.Security_Level , ['-','>','security', '_', 'level'], required_words=['>', 'security', 'level' ])
            response(long.Versions_And_Levels , ['-','>','versions', 'and', 'levels'], required_words=['>', 'versions', 'levels' ])

            #Channels Commands
            response(long.DarkDoor_Channel , ['-','>','darkdoor', '_', 'channel'], required_words=['>', 'darkdoor', 'channel' ])
            response(long.CHHOrg_Channel , ['-','>','chhorg', '_', 'channel'], required_words=['>', 'chhorg', 'channel' ])
            response(long.Org_Channels , ['-','>','org', '_', 'channels'], required_words=['>', 'org', 'channels' ])

            response(long.Register, ['how', 'to', 'register'], required_words=['how','to', 'register'])
            response(long.Config_Yaaic, ['how', 'to', 'config', 'yaaic'], required_words=['how','to', 'config', 'yaaic'])
            response(long.Org_Info , ['-','>','org', '_', 'info'], required_words=['>', 'org', 'info' ])
            best_match = max(highest_prob_list, key=highest_prob_list.get)
            #print(highest_prob_list)

            return long.unknown() if highest_prob_list[best_match] < 1 else best_match


        def get_response(user_input):
            split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
            response = check_all_messages(split_message)
            return response

        #Testing the response systm
        while True:
            print(Bright_Magenta + 'RekcahDA_Bot: ' + Bright_Green + get_response(input(Bright_Cyan + Membership + iD + ': '+ Bright_Green)))
    else:
        print(Bright_Red + Membership + iD + Bright_Green + " Passwords Didn't Match \n\
Please Make Sure They Match.")
else:
    print(Bright_Red + Membership + iD + Bright_Green + " You Need To Input 8 or More \n\
Characters In Password...")            