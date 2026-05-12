#Script by VIPUL
#dependencies => should be in the same folder as latest yt-dlp python file or should have yt-dlp latest installed on your system. 
#             => python3 required

import subprocess


def dlplaylist():
     url=input("enter url from youtube to download mp3(playlist) => ")
#use replace to change the download path there is some kind of bug
     path='"~/Music"'

     command = 'python3 yt-dlp -x --audio-format mp3 --audio-quality 0 --embed-metadata --add-metadata --parse-metadata "playlist_index:%(track_number)s" --embed-thumbnail -o "%(title)s.%(ext)s" -P "/home/mechanisium/Music" '+url 
# Run the command on the terminal
     result = subprocess.run(command, shell=True, text=True, capture_output=True)

# Print the output and errors (if any)
     print("Output:")
     print(result.stdout)

     print("Errors:")
     print(result.stderr)


while(True):
    dlplaylist()
    wanttocontinue=input("do you want to continue [y]yes or [Q]quit? =>")
    if(wanttocontinue == "Y") or (wanttocontinue == "y"):
        dlplaylist()
    else:
        break
