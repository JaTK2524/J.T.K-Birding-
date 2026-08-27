import os
import shutil

downloads = "/home/jake/Downloads"
stamping_room = "."
names = [
"Crimson Sunbird",
"Golden-Fronted Leafbird",
"Black Bulbul",
"Grey-Breasted Prinia",
"Ashy Prinia",
"Plain Prinia",
"Indian Bush Lark",
"Oriental Skylark",
"Common Hawk-Cuckoo",
"Pied Cuckoo",
"Greater Flamingo",
"Indian Courser",
"Long-Tailed Shrike",
"Bay-Backed Shrike",
"Small Minivet",
"White-Browed Wagtail",
"Red-Naped Ibis",
"White-Bellied Sea-Eagle",
"Lesser Adjutant",
"Malabar Pied Hornbill",
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
