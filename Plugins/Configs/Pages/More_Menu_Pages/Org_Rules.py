import os, time, sys
from Plugins.Configs.Settings import *

def Org_Rules():
    Rules_List = "---Here Is The Organization Rules List---"
    print(BG_Bright_Cyan + Bright_Yellow)
    for char in Rules_List:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(Rest +"" + Bright_Red)
    Rules_msg = "Organization's Rules;\n\
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
    for char in Rules_msg:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.3)
    print(Rest +"")