import os
import shutil

downloads = "/home/jake/Downloads"
stamping_room = "."
names = [
"Superb Fairywren",
"Laughing Kookaburra",
"Australian Magpie",
"Rainbow Lorikeet",
"Southern Cassowary",
"Italian Sparrow",
"European Stonechat",
"European Bee-eater",
"White Stork",
"European Serin",
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
