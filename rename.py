import os
files=os.listdir("./")
for file in files:
    if file[-4:]!="docx":
        continue
    os.rename(file,file.replace("docx","md"))