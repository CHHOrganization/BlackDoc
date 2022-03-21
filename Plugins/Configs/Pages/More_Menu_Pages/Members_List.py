import os, time, sys
from Plugins.Configs.Settings import *

def Members_List():
    Members_List = "---Here Is The List Of All Org Members---"
    print(BG_Bright_Cyan + Bright_Yellow)
    for char in Members_List:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(Rest + "" + Bright_Green)
    #Member
    Print_Members = "[+] -> Members List Updates\n\
Date: 24/02/2022\n\
\n\
I). Membership: RekcahHC_I\n\
II). Membership: RekcahHC_II\n\
III). Membership: RekcahHC_III (Pending)\n\
IV). Membership: RekcahHC_IV\n\
V). Membership: RekcahHC_V\n\
VI). Membership: RekcahHC_VI)\n\
VII). Membership: RekcahHC_VII (Pending)\n\
VIII). Membership: RekcahHC_VIII\n\
IX). Membership: RekcahHC_IX (Pending)\n\
X). Membership: RekcahHC_X\n\
XI). Membership: RekcahHC_XI"
    #End Line Of Members
    for char in Print_Members:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.1)
