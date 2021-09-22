# music-playlist-shuffler
Small python script to rename your .mp3 files in order from 0 + randomly. Shuffle a folder of music this way! 

  # Before
    0.Lofi-pilot.mp3  25.firetrack.mp4    heavy_metal.mp4  really_lofi.mp4
    100.emp.mp4       2.Lofi-skyline.mp3  lit_single.mp4
    1.Lofi-3am.mp3    3.Lofi-2am.mp3      new_song.mp4

  # after
    0.firetrack.mp4     3.emp.mp4         6.heavy_metal.mp4  9.really_lofi.mp4
    1.Lofi-skyline.mp3  4.Lofi-pilot.mp3  7.Lofi-3am.mp3
    2.lit_single.mp4    5.new_song.mp4    8.Lofi-2am.mp3


# How to run 
1. Go to the directory that has "suffle.py"

2.in a command line type...

Linux/Mac
```console
python3 -c "from shuffle import shuffle_music;shuffle_music('<PATH-TO-PLAYLIST>')"
```

Windows
```console
python -c "from shuffle import shuffle_music;shuffle_music('<PATH-TO-PLAYLIST>')"
```

# Make a command (Linux)

1. Make a shell script shuffleplaylist.sh

2. Write the following...
```bash
#!/bin/sh

cd ~/Directory/for/shuffle-python-file

python3 -c "from shuffle import shuffle_music;shuffle_music('<PATH-TO-PLAYLIST>')"
```
3. create alias in terminal 
```console
alias shuffleplaylist="bash shuffleplaylist.sh"
```
