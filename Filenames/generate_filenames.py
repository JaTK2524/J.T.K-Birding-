import os
download_folder = "/home/jake/Downloads"
folder = "."
birds = [
"Pied Bushchat",
"Black Redstart",
"Spotted Owlet",
"Black-Naped Oriole",
"Woolly-Necked Stork",
"Common Iora",
"Jungle Owlet",
"Black-Hooded Oriole",
"Brown Rock Chat",
"Blue-Tailed Bee-Eater",
]

birds = birds[::-1]

files = [
         f for f in os.listdir(download_folder)
         if f.lower().endswith(("jpg", "jpeg", "png"))
         ]
files.sort(
         key = lambda f: os.path.getctime(
         os.path.join(download_folder, f)
         )
    ) 
print("Files found:")
print(files)
        
for old_name, bird in zip(files,birds):
    new_name = bird.replace(" ", "") + "1.jpg"
            
    old_path = os.path.join(download_folder, old_name)
    new_path = os.path.join(folder, new_name)
            
    os.rename(old_path, new_path)
            
print("All Images Were Renamed Successfully!")
