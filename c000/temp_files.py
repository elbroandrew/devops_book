import tempfile, os

print(os.listdir())

with tempfile.TemporaryFile('w+') as temp:
    temp.write("I am a temporary file!")
    temp.seek(0)
    print(temp.read())

with tempfile.TemporaryDirectory() as temp_dir:
    print(temp_dir)
    print(os.path.exists(temp_dir))

