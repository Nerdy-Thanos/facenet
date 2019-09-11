import os
os.getcwd()
collection = "datasets/vignesh0/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("datasets/vignesh0/" + filename, "datasets/vignesh0/" + str(i) + ".jpg")