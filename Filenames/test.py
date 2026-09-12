import os
import shutil 

os.mkdir("J.T.K Birding/TestFolder")

count = 0

other_count = 0

for root, folders, files in os.walk("."):
    for file in files:
        if file.lower().endswith(".txt"):
           print(os.path.join(root,file))
           count += 1
        else:
             other_count += 1
             
print("Txt files: ", count)
print("Other files ", other_count)
