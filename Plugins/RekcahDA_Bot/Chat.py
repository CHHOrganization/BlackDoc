import re
import long_responses as long
import os,sys,time, datetime
from Settings import *

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
    Login_Banner()
    print(Bright_Yellow +"Login Security")
    print(Bright_Red + Membership + Identity + Bright_Green + Login_Main_msg)
    Moretime_Load()
    clearConsole()

def CPassword_Error():
    clearConsole()
    Login_Banner()
    print(Bright_Yellow +"Login Security")
    print(Bright_Red + Membership + Identity + Bright_Green + CPassword_Error_msg)
    Moretime_Load()
    clearConsole()

def Nickname_Error():
    clearConsole()
    Login_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Nickname.")
    Moretime_Load()
    clearConsole()

def iD_Error():
    clearConsole()
    Login_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Org iD.")
    Moretime_Load()
    clearConsole()

def Location_Error():
    clearConsole()
    Login_Banner()
    print(Bright_Red + "Empty Input Error;" + Bright_Green + "\n\
Please make sure you enter your Location.")
    Moretime_Load()
    clearConsole()

def Menu_Error():
    clearConsole()
    Login_Banner()
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
    Security_info = "-----------Account Secret Codes----------"
    for char in Security_info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.2)
    print(Rest + "" + Bright_Red)
    print("Yaaic & Element Password: "+ Identity + Location[1] + Password[0] + Location[3] + Identity[0] + Password[4] + Password[6])
    print("DarkChat Code: "+ Secret_Chat + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])
    print("Unique Code: "+ Secret + Identity + "-" + Location[0] + Password[3] + Location[4] + Identity[0] + Password[1] + Password[0])

while True:
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

                            #Welcoming Index Texts
                            #Banner
                            Main_Banner()
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
                            Membership_Details()
                            #current time
                            User_Data = "-------------BlackDoc Chat---------------"
                            print(BG_Bright_Cyan + Bright_Magenta)
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
                                print(Bright_Magenta + 'RekcahDA_Bot: ' + Bright_Green + get_response(input(Bright_Cyan + Membership + Identity + ': '+ Bright_Green)))
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
            