#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ffmpeg For Jupyter:
# conda install -c conda-forge ffmpeg

# ffmpeg for Windows:
# pip install ffmpeg

# pydub library:
# pip install pydub


# In[ ]:


# Personal batch audio script

import os, sys
from pydub import AudioSegment
from time import process_time

lst = [] # list of AudioSegments imported from songs
titles = [] # consider using dict instead?
lst_mod = [] # list of modified AudioSegements to be saved
dir_path = os.getcwd()

def export_fn(): 
    i = 0 # number of saved files
    x = input("Overwrite original files? (Y/N) \n")
    t0 = process_time() # record exporting time for performance measurement
    if x.upper() == "Y": # str.casefold()?
        print("saving...\n")
        for new in lst_mod:
            new.export(titles[i]+".mp3", format = "mp3", bitrate = "320k")
            print(titles[i] + " is overwritten.")
            i += 1
    elif x.upper() == "N":
        print("saving...\n")
        for new in lst_mod:
            # create a new directory if not found
            dir_new = os.path.join(dir_path, "TMU_export\\")
            if os.path.isdir(dir_new) == False:
                os.mkdir(dir_new)
            
            dir_new = dir_new + titles[i] + ".mp3"
            new.export(dir_new, format = "mp3", bitrate = "320k")
            print(titles[i] + " is saved to TMU_export.")
            i = i+1
    else:
        print("Stupid.")
        export_fn()
    print(str(i) + " files are saved in " + str((process_time()-t0)) + "s.")

def vol_increase(lst): # remove parameter if using global lst?
    print("+/- 3dB for a minimal hearable adjustment, 6dB for a moderate change in volume.")
    print("Note that any positive gain will result in distortion/quality loss.")
    dB = input("Type in the number of dB to change:\n")
    print("processing...\n")
    t0 = process_time() 
    i = 0
    for song in lst:
        duration = song.duration_seconds*1000
        new = song[:duration] + dB
        lst_mod.append(new)
        i += 1
    print(str(i) + " songs are processed in " + str((process_time()-t0)) + "s.\n")
    export_fn()
        
def quit_fn():
    x = input("\nType anything to exit.\n")
    quit()
    
def main():
    menu = 0
    t0 = process_time() # record exporting time for performance measurement
    print("Scanning files, this may take a minute...\n")
    # print(os.listdir(dir_path))
    # Finding all supported files in directory
    for file in os.listdir(dir_path): # any format supported by ffmpeg should work
        if file.endswith(".mp3"):
            # song = AudioSegment.from_file("/path/to/file.mp3", format="mp3")
            print(file)
            title = os.path.splitext(file)[0]
            song = AudioSegment.from_mp3(file)
            lst.append(song)
            titles.append(title)
        elif file.endswith(".wav"):
            print(file)
            title = os.path.splitext(file)[0]
            song = AudioSegment.from_wav(file)
            lst.append(song)
            titles.append(title)
        elif file.endswith(".ogg"):
            print(file)
            title = os.path.splitext(file)[0]
            song = AudioSegment.from_ogg(file)
            lst.append(song)
            titles.append(title)
        elif file.endswith(".mp4"):
            print(file)
            title = os.path.splitext(file)[0]
            song = AudioSegment.from_file(file,"mp4")
            lst.append(song)
            titles.append(title)
        elif file.endswith(".aac"):
            print(file)
            title = os.path.splitext(file)[0]
            song = AudioSegment.from_file(file,"aac")
            lst.append(song)
            titles.append(title)

    if len(lst) == 0:
        print("\nNo supported file (mp3, wav, ogg, mp4, aac) found. \n")
        quit_fn()
    else:
        print("\n" + str(len(lst)) + " files scanned in " + str((process_time()-t0)) + "s.\n")
        menu = 1 ### implement ###
        
    if menu == 1:
        vol_increase(lst)
    quit_fn()

main()
print("Now this is a bug.\n")
quit_fn()

