import os
list_files=os.listdir("C:\\Users\\achan\\Downloads\\prank")
print(list_files)
os.chdir("C:\\Users\\achan\\Downloads\\prank")
for file in list_files:
    old_name=file
    print(old_name)

    new_name=old_name.lstrip("0123456789")
    print(new_name)
    os.rename(old_name,new_name)
    print(new_name)