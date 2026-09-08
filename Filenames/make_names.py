import os
import shutil

downloads = "/home/jake/Downloads"
stamping_room = "."
names = [
"Black-winged Stilt",
"Eurasian Coot",
"Indian Spot-billed Duck",
"House Sparrow",
"Laughing Dove",
"Blue-eared Kingfisher",
"Little Grebe",
"Chestnut-bellied Sandgrouse",
"Oriental Turtle Dove",
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
