import os

downloads_folder = "/home/jake/Downloads/"

images = os.listdir(downloads_folder)

for image in images:
    path = downloads_folder + image
    time = os.path.getmtime(downloads_folder + image)

    print(path, time)

print("Done, Jake")
