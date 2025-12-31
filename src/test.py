import pathlib

cwd = pathlib.Path.cwd()
parent = cwd.parent
import_dir = parent/'env'/'Lib'

print("Current working directory: ", cwd)
print("Parent Directory: ", parent)
print("Import Directory: ", import_dir)