import os
 
count = 0
 
files = os.listdir(".")
for file in files:
    if file.lower().endswith(".jpg"):
              count += 1
print("JPG Images: ", count)   
ze_count = 0
os.mkdir("TestFolder")
photos = os.listdir("TestFolder")
for photo in photos:
    if photo.lower().endswith(".jpg"):
       ze_count += 1
print("JPG Images: ", ze_count)
print(file)
