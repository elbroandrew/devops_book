# use os only if my script is not going to be crossplatform
# because for each platform there is specific mehods in 'os' module
# such as: Windows os.O_TEXT, GNU/Linux os.CLOEXEC
import os
import time

print(os.stat("text"))
p = os.stat("text")
print(oct(p.st_mode)[-3:])  # 644
os.chmod('text', 0o777)  # using chmod
p = os.stat("text")
print(oct(p.st_mode)[-3:])  # 777

# os.path.expandvars && os.path.expanduser
print(os.path.expanduser("~/.ssh"))  # подставит  '/home/andrew/.ssh' вместо тильды или ~user
print(os.path.expanduser("~"))
print(os.environ)
print(os.path.expandvars("$HOME/.ssh"))  # короче берет из окружения переменную и подставляет ее путь в виде $HOME или ${HOME}

# get last access time and size
children = os.listdir()
for child in children:
    child_path = os.path.join(os.getcwd(), child)
    #print(child_path)
    if os.path.isfile(child_path):
        last_access_time = os.path.getatime(child_path)
        size = os.path.getsize(child_path)
        print("Path: %s, last time accessed: %s; size: %s;" % (child, time.ctime(last_access_time), size))
