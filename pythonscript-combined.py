#Script by VIPUL
#dependencies => should be in the same folder as latest yt-dlp python file or should have yt-dlp latest installed on your system. 
#             => python3 required

import subprocess

def dlsingle():
     url=input("enter url from youtube to download mp3(single) => ")
#use replace to change the download path there is some kind of bug
     path='"/home/mechanisium/Music"'

     command = 'python3 yt-dlp -x --audio-format mp3 --audio-quality 0 --embed-metadata --add-metadata --parse-metadata "playlist_index:%(track_number)s" --embed-thumbnail -o "%(title)s.%(ext)s" -P "/home/mechanisium/Music" --no-playlist '+url  
# Run the command on the terminal
     result = subprocess.run(command, shell=True, text=True, capture_output=True)

# Print the output and errors (if any)
     print("Output:")
     print(result.stdout)

     print("Errors:")
     print(result.stderr)


def dlplaylist():
     url=input("enter url from youtube to download mp3(playlist) => ")
#use replace to change the download path there is some kind of bug
     path='"/home/mechanisium/Music"'

     command = 'python3 yt-dlp -x --audio-format mp3 --audio-quality 0 --embed-metadata --add-metadata --parse-metadata "playlist_index:%(track_number)s" --embed-thumbnail -o "%(title)s.%(ext)s" -P "/home/mechanisium/Music" '+url 
# Run the command on the terminal
     result = subprocess.run(command, shell=True, text=True, capture_output=True)

# Print the output and errors (if any)
     print("Output:")
     print(result.stdout)

     print("Errors:")
     print(result.stderr)



print("hey nerd!")

ch=input("Enter=> [S]single file [P]playlist ")


if(ch == "S") or (ch == "s"):   
    dlsingle()

elif(ch == "P") or (ch == "p"):
    dlplaylist()


    


while(True):
       
    wanttocontinue=input("do you want to continue [S]single or [P]playlist(may take some time)  or [Q]quit? =>")

    if(wanttocontinue == "S") or (wanttocontinue == "s"):
        dlsingle()
    if(wanttocontinue == "P") or (wanttocontinue == "p"):
        dlplaylist()
    else:
        break



