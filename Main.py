########  #### ##     ## ##     ## ######## ########     ########  #######   #######  ##        ######  
##     ##  ##  ###   ### ###   ### ##       ##     ##       ##    ##     ## ##     ## ##       ##    ## 
##     ##  ##  #### #### #### #### ##       ##     ##       ##    ##     ## ##     ## ##       ##       
########   ##  ## ### ## ## ### ## ######   ########        ##    ##     ## ##     ## ##        ######  
##     ##  ##  ##     ## ##     ## ##       ##   ##         ##    ##     ## ##     ## ##             ## 
##     ##  ##  ##     ## ##     ## ##       ##    ##        ##    ##     ## ##     ## ##       ##    ## 
########  #### ##     ## ##     ## ######## ##     ##       ##     #######   #######  ########  ######  

import os
import subprocess
import glob

def main():
    #Temporal stuff. Just for today.

    songs = {}

    exitDirCreation = False

    while (not exitDirCreation):
        print("Select dir name")
        print("Write end to finish")
        dirName = input(">> ")
    
        if (dirName == 'end'):
            exitDirCreation = True
        else:
            songs[dirName] = []
            exit = False
            print("Add spotify lists and songs")
            print("Write end to finish")
            while (not exit):
                song = input(">> ")
                if (song == 'end'):
                    exit = True
                else:
                    songs[dirName].append(song)
    
    for dirKey in songs.keys():
        try:
            os.mkdir("output/" + dirKey)
        except:
            next

    for song in songs[dirKey]:
        os.system("cd 'output/" + dirKey +  "' && ../../libs/spotdl-4.2.4-linux " + song)
    
    bimmerPlayListCreation(dirKey)


def bimmerPlayListCreation(dirKey):
    dir = "output/" + dirKey
    songs = glob.glob(dir + "/*.mp3")

    playList = open("output/" + dirKey + ".m3u", "w")

    for song in songs:
        playList.write(song.replace("/", "\\").replace("output\\", "") + "\r\n")

if __name__ == '__main__':
    main()