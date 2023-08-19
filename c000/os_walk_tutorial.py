import os

print(os.listdir())

g = os.walk("./")  # walks through each dir and returns generator

print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("-----------------")
for cur_dir, sub_dirs, files in g:
    print(f"Processing {cur_dir}")
    print("Sub-dirs %s" % sub_dirs)
    print("Files %s" % files)
