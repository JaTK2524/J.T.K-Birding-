import os
import shutil

downloads = "/home/jake/Downloads"
stamping_room = "."
names = [
"European Robin",
"European Goldfinch",
"Eurasian Jay",
"Great Spotted Woodpecker",
"Common Kestrel",
"Common Nightingale",
"Northern Lapwing",
"Eurasian Magpie",
"European Greenfinch",
"Common Chaffinch",
]

things = os.listdir(downloads)
things.sort(key = lambda thing: os.path.getmtime(downloads + "/" + thing))
    
for index, thing in enumerate(things):
    bird = names[index]
    new_name = bird.replace(" ", "") + "1.jpg"  
    
    old_path = downloads + "/" + thing
    new_path = stamping_room + "/" + new_name
    
    shutil.move(old_path, new_path)
print("Done")
