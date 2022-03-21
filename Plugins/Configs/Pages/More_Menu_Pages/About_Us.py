import os, time, sys
from Plugins.Configs.Settings import *

def About_Us():
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
