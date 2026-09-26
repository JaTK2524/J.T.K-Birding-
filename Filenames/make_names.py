import os
import shutil

downloads = "/home/jake/Downloads"
stamping_room = "."
names = [
"Tawny Frogmouth",
"Willie Wagtail",
"Blue-faced Honeyeater",
"Eastern Rosella",
"Galah",
"Sulphur-crested Cockatoo",
"Australian Pelican",
"Australian Wood Duck",
"Pacific Black Duck",
"Masked Lapwing",
"Australian Brush-turkey",
"Emu",
"Wedge-tailed Eagle",
"Northern Hawk-Owl",
"Australian Darter",
"Pied Currawong",
"Noisy Miner",
"Eastern Yellow Robin",
"Australian Golden Whistler",
"Australian King-Parrot",
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
