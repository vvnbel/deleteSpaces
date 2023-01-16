import os


def make_unique_name(new_name_without_spaces):
    filename, extension = os.path.splitext(new_name_without_spaces)
    counter = 1
    while os.path.exists(new_name_without_spaces):
        new_name_without_spaces = filename + "_" + str(counter) + extension
        counter += 1
    return os.rename(folder, new_name_without_spaces)


os.chdir('D:\\test')

for folder in os.listdir():
    if os.path.isdir(folder) and '  ' in folder:
        new_name_without_spaces = ' '.join(folder.split())
        make_unique_name(new_name_without_spaces)