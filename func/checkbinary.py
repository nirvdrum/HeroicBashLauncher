#TO USE LEGENDARY OR GOGDL
#   For AppImage, check if alternavtive binary (Legendary) is added.
#   If not, check folder under /tmp/ that includes path to the binaries.

import os, json, sys, traceback
import configpath

def getbinary(gametype):

    try:

        #Path to heroic's configuration json file
        #heroicconfigpath = os.path.expanduser("~") + "/.config/heroic/config.json"

        #Convert config json to dict
        with open(configpath.heroicconfigpath, encoding='utf-8') as p:
            heroicconfig = json.load(p)

        #Checking
        if os.path.exists("/opt/Heroic/resources/app.asar.unpacked/build/bin/linux") == True:

            if gametype != "epic":
                binary = "/opt/Heroic/resources/app.asar.unpacked/build/bin/linux/gogdl "
            else:
                binary = "/opt/Heroic/resources/app.asar.unpacked/build/bin/linux/legendary "
        elif heroicconfig["defaultSettings"]["altLegendaryBin"] != "" and gametype == "epic":

            binary = heroicconfig["defaultSettings"]["altLegendaryBin"] + " "
        elif heroicconfig["defaultSettings"]["altGogdlBin"] != "" and gametype != "epic":

            binary = heroicconfig["defaultSettings"]["altGogdlBin"] + " "
        elif os.path.exists("/var/lib/flatpak/app/com.heroicgameslauncher.hgl") or os.path.exists("/app/bin/heroic"):#System or Flatpak-env path

            if gametype != "epic":
                binary = "/app/bin/heroic/resources/app.asar.unpacked/build/bin/linux/gogdl "
            else:
                binary = "/app/bin/heroic/resources/app.asar.unpacked/build/bin/linux/legendary "
        else:#AppImage

            if gametype != "epic":
                binary = os.getcwd() + "/binaries/gogdl "
            else:
                binary = os.getcwd() + "/binaries/legendary "
            

        return binary
    except Exception:

        print(traceback.format_exc())
        os.system('zenity --error --title="Failed" --text="Looks like you are using Heroic via AppImage\n\nMake sure to keep Heroic running and try again" --width=300')
        sys.exit()