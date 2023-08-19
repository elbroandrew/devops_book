import os
import pathlib

rc_name = ".examplerc"
var_name = "EXAMPLE_RC_DIR"
var_path = os.path.join(os.getcwd(), rc_name)
config_path = os.path.expandvars(var_path)  # не надо, наверно, т.к. нет глобальных переменных в пути?
print(config_path)
print(os.environ.items())

# print rc file current dir
rc_file_dir = os.path.abspath(__name__) # will get full path and __name__ at the end
parent_path = os.path.dirname(rc_file_dir)  # will get full path w/o __name__ (only current dir the file resides)
current_path = os.path.join(parent_path, rc_name)
print("cur path", current_path)



os.environ[var_name] = parent_path  # just add parent dir for tutorial below

# using paths as pathlib objects (useful for current OS, because paths may differ on Win, Mac, Linux)
example_dir = os.environ[var_name]  # gets path from environ
posix_path = ""
if example_dir:
    dir_path = pathlib.Path(example_dir)  # pathlib object
    config_path = dir_path / rc_name  # we can combine slashes with parent dir and strings
    print(dir_path)
    print(config_path)
    if config_path.exists():
        posix_path = config_path.as_posix()  # returns as string
print(posix_path)

# check dir of a file
file_path = pathlib.Path(__file__).resolve()  # returns full path with this python script name
print(file_path)
parent_path = file_path.parent
print(parent_path)  # full path of the directory itself


