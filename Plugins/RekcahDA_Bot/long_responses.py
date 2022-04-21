import random
import os,sys,time 
Register = "To register in the Org,\n\
you must get a real membership \n\
and in order to do so you need \n\
to contact RekcahHC_I for\n\
Membership!\n\
I have no memory cause My God\n\
he said am still developing... "

#Yaa Config messages
Config_Yaaic = "Whats your Yaaic App Problem?"
Config_Yaaic0 = "Whats your Yaaic App Problem?"
Config_Yaaic1 = "Is it about the Installation?"
Config_Yaaic2 = "Whatever step you missed you\n\
you must read the whole steps \n\
again or Type; I cant register the yaaic app."
Config_Yaaic3 = "So you can't connect to Yaaic?"
Config_Yaaic4 = "Did you register Yaaic now?"
Config_Yaaic5 = "How To Register Yaaic;\n\
Your password must match!\n\
Your Port Must Be 6697\n\
Your Host Must Be irc.anonops.com\n\
Note: After you connect you must wait for 180sec\n\
before you can Register!\n\
Dont Leave The App!\n\
Wait.... For 180sec\n\
Then type this Commands;\n\
/msg NickServ REGISTER ******* info@chh.ogr\n\
\n\
Note: Those (****) Must Be Replaced By Your Password.\n\
You Must Use Your Secret Password From BlackDoc\n\
Unique Code Is Not Recommanded!\n\
\n\
To Join Channels Command;\n\
-> Org Channels"
Config_Yaaic6 = "Is easy to configure Yaaic,\n\
just open yaaic config at the menu"
Config_Yaaic7 = "Just follow the config steps\n\
right and dont messup!"
Config_Yaaic8 = "Port is 6697"
Config_Yaaic9 = "Host is irc.anonops.com"
Config_Yaaic10 = "This is a command to register\n\
NickServ; /msg NickServ REGISTER ********* \n\
info@chh.org\n\
Please Replace (***) with you password\n\
you enter in your Yaaic App."
Config_Yaaic11 = "Title Must Be; The Org\n\
or The Organization."
Config_Yaaic12 = "This is a command to Asign\n\
your password;\n\
/msg NickServ ASIGN *******"
Config_Yaaic13 = "To Download Yaaic here is the\n\
link: bit.ly/chhorg-yaaic-app"

#RANDOM
Coding_Tools = "In order for you to code you cam\n\
Download Code Editor for Android or Visual Studio\n\
for windows... Even Linux and Mac have them."
Coding_Apps = "There are many coding apps in Google\n\
PlayStore, for python, php, c++, C, C#, SQL, CSS\n\
and fo many more languages"
Open_Python = "You can open python script with\n\
Termux in Adroid, Linux, Mac and Windows Terminals\n\
to download Termux vist 'Apps'"
Which_Language = "In order for you to code, you need\n\
notepad++, nano or Visual Studio then star practice."
Use_Python = "For you to code python you need any\n\
coding software or app installed in your machine\n\
We Recommand Code Editor App or Visual Studio \n\
Software, then every file you make save it with \n\
.py so it can work and open as python then start\n\
using python rules."
Use_PHP = "For you to code php script you need wamp\n\
-server and a coding software installed in your\n\
machine We Recommand Visual Studio Software, \n\
then every file you make save it with \n\
.php so it can work and open as php\n\
then start using php rules."
Use_SQL = "For you to code sql or mysql \n\
script you need wampserver and a coding \n\
software installed in your machine We \n\
Recommand Visual Studio Software, \n\
then every file you make save it with \n\
.sql so it can work and open as sql\n\
then start using sql rules."
Use_CSS = "For you to code css you need\n\
html script as css style html and a\n\
coding software installed in your machine\n\
We Recommand Visual Studio Software, \n\
then every file you make save it with \n\
.css so it can work and open as css\n\
then start using css rules."
Use_HTML = "For you to code html you need\n\
a coding software installed in your machine\n\
We Recommand Visual Studio Software, \n\
then every file you make save it with \n\
.html so it can work and open as html\n\
then start using html rules."
Use_JavaScript = "Javascript it also support\n\
html so yo also need html to make it active.\n\
need a coding software installed in your\n\
machine We Recommand Visual Studio Software,\n\
then every file you make save it with \n\
.html so it can work and open as \n\
then start using html rules."
Use_Java = "Wait..."
Use_C = "Wait..."
Use_Sharp = "Wait..."
Use_CI = "Wait..."

#Log Commands
#Memberships
Print_Memberships = "[+] -> Memberships [Full Detals] Updates\n\
Date: 24/02/2022\n\
\n\
I). Membership: RekcahHC_I\n\
    \n\
    Skills List\n\
    I). Full Stock Developer\n\
    II). Digital Marketer\n\
    III). Ethical Hacker\n\
    IV). DarkWeb User\n\
    V). Script kiddo\n\
    VI). VPN Creator\n\
\n\
II). Membership: RekcahHC_II\n\
     \n\
     Skills List\n\
     I). Hacking; Facebook // Instagram // Etc\n\
     II). Modding\n\
     III). Hacking; CCTV Cameras\n\
     IV). Able To Add Windows 10 to Android\n\
     V). VPN Creator\n\
     VI). VPN Moddern\n\
    \n\
III). Membership: RekcahHC_III (Pending)\n\
\n\
IV). Membership: RekcahHC_IV (Pending)\n\
    \n\
V). Membership: RekcahHC_V\n\
    \n\
    Skills List\n\
    I). Programming Languages; Python // C++ // HTML // CSS\n\
    II). Termux Hacker\n\
    III). A Little Experience In Kali Linux\n\
\n\
VI). Membership: RekcahHC_VI)\n\
    \n\
    Skills List\n\
    I). Coding With Python\n\
    II). Using VPN\n\
    IV). Website Developer\n\
\n\
VII). Membership: RekcahHC_VII (Pending)\n\
\n\
VIII). Membership: RekcahHC_VIII (Pending)\n\
\n\
IX). Membership: RekcahHC_IX (Pending)\n\
\n\
X). Membership: RekcahHC_X"
#End Line Of Memberships

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

#Rules
Rules = "Organization's Rules;\n\
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
#End Line Of Rules        


#Updates
Updates = "Date: 22/02 - 01/03/2022 Updates\n\
\n\
[+] -> FIXED Errors\n\
       I). Fixed Menu Borders\n\
       II.) Fixed Exiting And Chat.py Options\n\
\n\
[+] -> New Features\n\
       I). We added new menu items\n\
       II). We added script animation\n\
       III). We added new security for exits\n\
             you can use N to stay, Y to quit\n\
             or chat to chat with me.\n\
       IV). We added a Bot\n\
       V). We added Commands\n\
       VI). We added Org Rules at More. in Menu\n\
       VII). We added Loading Progress\n\
\n\
[+] -> Errors\n\
       I). Chat Option in Menu for Termux/Linux\n\
       Is not working!!!\n\
       \n\
       Note: In Termux we run TermuxRun.sh after\n\
       Installations.\n\
       II). Other Items in Menu they are unavailable\n\
       III). The script is still under Developing"
#End OF Line

#Versions And Levels Commmands
BlackDoc_Version = "BlackDoc Version: V0.0.04"
Bot_Version = "Bot Version: V0.0.02"
Response_Level = "Response Level: 1.02"
Security_Level = "Security Level: 1.04"
Versions_And_Levels = "Versions And Levels Updates\n\
Date: 22/02 - 01/02/2022\n\
\n\
BlackDoc Version: V0.0.04\n\
Bot Version: V0.0.02\n\
Response Level: 1.02\n\
Security Level: 1.04\n\
\n\
Note: The Script Is Still Developing"
#ENd Of List

#User Membership
My_Membership = "For more details about your\n\
membership please view Memberships in Menu!\n\
or Command; -> Memberships"
#End of Line

#Commands List
Commands_List = "Commands List;\n\
-> Help = To Show This List\n\
-> Port = Yaaic App Port\n\
-> Host = Yaaic App Host\n\
-> Title = Yaaic App Title\n\
-> Memberships = Memberships Updates\n\
-> Members = List of Members\n\
-> Updates = The Lastest Script Updates\n\
-> Rules = The Org Rules\n\
-> Org Info = Information About CHH.Org\n\
-> Org Channels = The Organization irc channels\n\
-> DarkDoor Channel = The Org DarkDoor Channel\n\
-> CHHOrg Channel = The Organization Main Channel"
#end of Line

#Channels Commands
Org_Channels = "The Organization IRC Channels\n\
I). #DarkDoor Channel\n\
II). #CHHOrg Channel"
DarkDoor_Channel = "#DarkDoor Channel;\n\
Yaaic Command: /msg join #darkdoor"
CHHOrg_Channel = "#CHHOrg Channel;\n\
Yaaic Command: /msg join #chhorg"

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

#Commands List
Help = "Commands List;\n\
-> Help = To Show This List\n\
-> Port = Yaaic App Port\n\
-> Host = Yaaic App Host\n\
-> Title = Yaaic App Title\n\
-> Memberships = Memberships Updates\n\
-> Members = List of Members\n\
-> Updates = The Lastest Script Updates\n\
-> Rules = The Org Rules\n\
-> Org Info = Information About CHH.Org\n\
-> Org Channels = The Organization irc channels\n\
-> DarkDoor Channel = The Org DarkDoor Channel\n\
-> CHHOrg Channel = The Organization Main Channel"
#end of Line

def unknown():
    response = ['Could you please re-phrase that?' ,
                "Sorry am DABot, member...",
                "Try to talk about it with\n\
                Rekcahhc_I, my God",
                "I cant think of nothing to \n\
                help you!",
                "Connect to the Org server",
                "What does that mean?"
                "What?"
                "Why, would you say that?"][random.randrange(4)]
    return response