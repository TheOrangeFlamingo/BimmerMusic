########  #### ##     ## ##     ## ######## ########     ########  #######   #######  ##        ######  
##     ##  ##  ###   ### ###   ### ##       ##     ##       ##    ##     ## ##     ## ##       ##    ## 
##     ##  ##  #### #### #### #### ##       ##     ##       ##    ##     ## ##     ## ##       ##       
########   ##  ## ### ## ## ### ## ######   ########        ##    ##     ## ##     ## ##        ######  
##     ##  ##  ##     ## ##     ## ##       ##   ##         ##    ##     ## ##     ## ##             ## 
##     ##  ##  ##     ## ##     ## ##       ##    ##        ##    ##     ## ##     ## ##       ##    ## 
########  #### ##     ## ##     ## ######## ##     ##       ##     #######   #######  ########  ######  

import os

#Create playlist in a BMW CCC compatible way
def main():
    print("Write drive route")
    driveLoc = input(">> ")
    print(driveLoc)

    subFolders = [f.name for f in os.scandir(driveLoc) if f.is_dir() and not f.name.startswith(".")]
    for detectedFolder in subFolders:
        print("Detected: " + detectedFolder)
        bimmerPlayListCreation(detectedFolder, driveLoc)


def bimmerPlayListCreation(dirKey, driveLoc):
    dir = driveLoc + "/" + dirKey
    songs = [f.name for f in os.scandir(dir) if f.is_file()]
    try:
        os.remove(dir + ".m3u")
    except:
        next

    playList = open(dir + ".m3u", "w")

    for song in songs:
        playList.write(dirKey + "\\" + song + "\r\n")

if __name__ == '__main__':
    main()