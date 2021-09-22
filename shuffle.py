import os
import random
import re

def shuffle_music(playlist_dir="/home/bbrodrick/Music/"):
    
    os.chdir(playlist_dir)
    files_left =[num for num in range(len(os.listdir(playlist_dir)))]

    print("total Files: ", len(files_left))
    
    for file in os.listdir(playlist_dir):
        number_choice = random.choice(files_left)
        if re.findall("\d\d?\d?\.",file):
            numberless_file_name = file[(len(re.findall("\d\d?\d?\.",file)[0]) -1):]
        else:
            numberless_file_name = "." + file
        new_file_name = str(number_choice) + str(numberless_file_name)
        os.rename(file,new_file_name)
        files_left.remove(number_choice)
        
    print("Done! New playlist Made!")
    print([filename for filename in sorted(os.listdir(playlist_dir))])

