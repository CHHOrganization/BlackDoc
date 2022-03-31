import os, time, sys
from Plugins.Configs.Settings import *

def BlackDOc_Info():
    BlackDoc_Info = "----Organization BlackDoc Script Info----"
    print(BG_Bright_Cyan + Bright_Magenta)
    for char in BlackDoc_Info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    #About The Org
    BlackDocument_Info = "Terminal BlackDocument Info;\n\
About BlackDoc (Python Script)\n\
We developed terminal python script\n\
for many reasons.\n\
Which is to quick assist our members with\n\
some random questions and instructions like\n\
How to config any irc client to point to our\n\
IRC Host and Port so you can join the online\n\
community.\n\
\n\
We use this script to keep our memebers\n\
Upto date at all time on a go with\n\
a computer or smart phone you can\n\
clone this package from Github.\n\
\n\
All the information in this script\n\
is classified to wrong hands and\n\
sharing or misuse of this script\n\
is highly not recommanded.\n\
\n\
We as the Organization Directors\n\
not responsble for any crimes\n\
might be committed by our fellow\n\
Member, as Our Mission about this script\n\
is positive which is to teach\n\
IT Fundamentals for free with terminal.\n\
\n\
We have many features in this Package\n\
ChatZone uses commands with -> ???(replace ???\n\
with any command to open info about it) for\n\
E.g -> Help, will show you all Commands List."
    print(Rest + Bright_Green)
    for char in BlackDocument_Info:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
    print("")
    print("" + Bright_Red +"For The Chat Script Info\n\
Check out 'Chat Info'")