#!/usr/bin/env python3

import os

# Recursively copy target directory and all of it's subdirectories/files to a destination directory.
def copydir(destination_path, target_path):
    if (type(destination_path) is not str):
        raise TypeError("The given file path " + str(destination_path) + " isn't a string!")

    if (type(target_path) is not str):
        raise TypeError("The given file path " + str(target_path) + " isn't a string!")

    if (path_exists(destination_path) == False):
        raise FileNotFoundError("The given file path " + str(destination_path) + " doesn't exist!")

    if (path_exists(target_path) == False):
        raise FileNotFoundError("The given file path " + str(target_path) + " doesn't exist!")

    if (isdir(destination_path) == False):
        raise ValueError("The given file path " + str(destination_path) + " isn't a directory!")

    if (isdir(target_path) == False):
        raise ValueError("The given file path " + str(target_path) + " isn't a directory!")

    dirpaths = list([target_path])
    filepaths = list([])
    working_dir = wdir()
    
    for root, dirs, files in os.walk(target_path, topdown=False):
        for path in dirs:
            dirpaths.append(str(os.path.join(root, path)))
        for path in files:
            filepaths.append(str(os.path.join(root, path)))

    dirpaths.sort(); filepaths.sort()
    
    chdir(destination_path)

    for dirpath in dirpaths:
        mkdir(dirpath)

    chdir(working_dir)

    for filepath in filepaths:
        copyfile("b", destination_path, filepath)

# Copy single/multiple text/binary based files to destination directory.
# The mode argument must be either strings: "t" (text) or "b" (binary).
# The destination_path and *filepaths arguments must be strings.
def copyfile(mode, destination_path, *filepaths):
    working_directory = wdir()

    if (type(destination_path) is not str):
        raise TypeError("The given file path " + str(destination_path) + " isn't a string!")

    if (type(mode) is not str):
        raise TypeError("The given mode " + str(mode) + " isn't a string!")

    if (path_exists(destination_path) == False):
        raise FileNotFoundError("The given file path " + str(destination_path) + " doesn't exist!")

    if (isdir(destination_path) == False):
        raise ValueError("The given file path " + str(destination_path) + " isn't a directory!")

    if (mode != "t" and mode != "b"):
        raise ValueError("The mode is of the incorrect value! It must either strings: 't' (text) or 'b' (binary)")

    for filepath in filepaths:
        if (filepath != str(filepath)):
            raise TypeError("The given file path " + str(filepath) + " isn't a string!")

        if (path_exists(filepath) == False):
            raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

        if (isfile(filepath) == False):
            raise ValueError("The given file path " + str(filepath) + " isn't a file!")

        print("Copying:", filepath, "to", destination_path)    
        lines = mklist(mode, filepath)
        chdir(destination_path)
        mkfile(mode, filepath)
        writelines(mode, filepath, lines)
        chdir(working_directory)
        print("Copy Success:", filepath, "copied to", destination_path)

# Read and print lines in single/multiple text/binary based files.
# The mode argument must be either strings: "t" (text) or "b" (binary).
# The *filepaths arguments must be strings. 
def rpfile(mode, *filepaths):
    for filepath in filepaths:         
        if (filepath != str(filepath)):
            raise TypeError("The given file path " + str(filepath) + " isn't a string!")

        if (type(mode) is not str):
            raise TypeError("The given mode " + str(mode) + " isn't a string!")

        if (path_exists(filepath) == False):
            raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

        if (isfile(filepath) == False):
            raise ValueError("The given file path " + str(filepath) + " isn't a file!")

        if (mode != "t" and mode != "b"):
            raise ValueError("The mode is of the incorrect value! It must either strings: 't' (text) or 'b' (binary)")

        print(" ------------------------------", "\n", "Reading/Printing:", filepath, "\n", "------------------------------")

        with open(filepath, "r" + mode) as new_file:
            for line in new_file:
                print(line, end="")
            
            new_file.close()
            print()

# Delete single/multiple files.
# The *filepaths arguments must be strings.
def rmfile(*filepaths):
    for filepath in filepaths:
        if (filepath != str(filepath)):
            raise TypeError("The given file path " + str(filepath) + " isn't a string!")

        if (path_exists(filepath) == False):
            raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

        if (isfile(filepath) == False):
            raise ValueError("The given file path " + str(filepath) + " isn't a file!")

        print("Deleting:", filepath)
        os.remove(filepath)
        print("Deletion Success:", filepath, "Deleted!")

# Make single/multiple text/binary based files.
# The mode argument must be either strings: "t" (text) or "b" (binary).
# The *filepaths arguments must be strings.
def mkfile(mode, *filepaths):
    for filepath in filepaths:
        if (filepath != str(filepath)):
            raise TypeError("The given file path " + str(filepath) + " isn't a string!")
            
        if (type(mode) is not str):
            raise TypeError("The given mode " + str(mode) + " isn't a string!")

        if (path_exists(filepath) == True):
            raise FileExistsError("The given file path " + str(filepath) + " already exists!")

        if (mode != "t" and mode != "b"):
            raise ValueError("The mode is of the incorrect value! It must either strings: 't' (text) or 'b' (binary)")
        
        print("Creating:", filepath)
        new_file = open(filepath, "x" + mode); new_file.close()
        print("Creation Success:", filepath, "Created!")

# Delete single/multiple empty directories.
# The *filepaths arguments must be strings.
def rmdir(*filepaths):
    for filepath in filepaths:
        if (filepath != str(filepath)):
            raise TypeError("The given file path " + str(filepath) + " isn't a string!")

        if (path_exists(filepath) == False):
            raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

        if (isdir(filepath) == False):
            raise ValueError("The given file path " + str(filepath) + " isn't a directory!")
            
        print("Deleting:", filepath)
        os.rmdir(filepath)
        print("Deletion Success:", filepath, "Deleted!")

# Delete single directory along with it's subdirectories and files.
# Use this with caution, as you could delete your entire file system if you're not careful. 
def rmall(dirpath):
    if (type(dirpath) is not str):
        raise TypeError("The given file path " + str(dirpath) + " isn't a string!")

    if (path_exists(dirpath) == False):
        raise FileNotFoundError("The given file path " + str(dirpath) + " doesn't exist!")

    if (isdir(dirpath) == False):
        raise ValueError("The given file path " + str(dirpath) + " isn't a directory!")

    dirpaths = list([])
    filepaths = list([])
    
    for root, dirs, files in os.walk(dirpath, topdown=True):
        for path in dirs:
            dirpaths.append(str(os.path.join(root, path)))
        for path in files:
            filepaths.append(str(os.path.join(root, path)))

    dirpaths.reverse(); filepaths.sort()

    for file in filepaths:
        rmfile(file)

    try:
        for file in dirpaths:
            rmdir(file)
    finally:
        rmdir(dirpath)
 
# Make single/multiple directories.
# The *filepaths arguments must be strings.
def mkdir(*filepaths):
    for filepath in filepaths:
        if (filepath != str(filepath)):
            raise TypeError("The given file path " + str(filepath) + " isn't a string!")

        if (path_exists(filepath) == True):
            raise FileExistsError("The given file path " + str(filepath) + " already exists!")
            
        print("Creating:", filepath)
        os.mkdir(filepath)
        print("Creation Success:", filepath, "Created!")

# Output to terminal the filenames/subdirectories in single/multiple directories. 
# Use no arguments for working directory only.
# The *filepaths arguments must be strings. 
def lsdir(*filepaths):
    if (len(filepaths) == 0):
        directory = os.listdir() 
        print(" -------------------", "\n", "Directory - Working", "\n", "-------------------")

        for file in directory:
            print("-", file)
        
    else: 
        for filepath in filepaths:
            if (filepath != str(filepath)):
                raise TypeError("The given file path " + str(filepath) + " isn't a string!")

            if (path_exists(filepath) == False):
                raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

            if (isdir(filepath) == False):
                raise ValueError("The given file path " + str(filepath) + " isn't a directory!")
                
            directory = os.listdir(filepath)
            print(" -------------------", "\n", "Directory - ", filepath.strip("../"), "\n", "-------------------")

            for file in directory:
                print("-", file)

# Change current working directory.
# The filepath argument must be a string. 
def chdir(filepath):
    if (filepath != str(filepath)):
        raise TypeError("The given file path " + str(filepath) + " isn't a string!")

    if (path_exists(filepath) == False and filepath != ".."):
        raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

    if (isdir(filepath) == False and filepath != ".."):
        raise ValueError("The given file path " + str(filepath) + " isn't a directory!")

    os.chdir(filepath)

# Return string of the path of the current working directory. 
def wdir():
    return os.getcwd()

# Print working directory to terminal. 
def pwdir():
    print("-", wdir())

# Return a list from lines in single/multiple text/binary based files.
# The mode argument must be either strings: "t" (text) or "b" (binary).
# The *filepaths arguments must be strings.
def mklist(mode, *filepaths):
    finalList = list([])
    tempList = list([])

    if (type(mode) is not str):
        raise TypeError("The given mode " + str(mode) + " isn't a string!")

    if (mode != "t" and mode != "b"):
        raise ValueError("The mode is of the incorrect value! It must either strings: 't' (text) or 'b' (binary)")
        
    for filepath in filepaths:
        if (filepath != str(filepath)):
            raise TypeError("The given file path " + str(filepath) + " isn't a string!")

        if (path_exists(filepath) == False):
            raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

        if (isfile(filepath) == False):
            raise ValueError("The given file path " + str(filepath) + " isn't a file!")    

        with open(filepath, "r" + mode) as new_file:
            tempList = new_file.readlines()
            new_file.close()

            for element in tempList:
                if (mode == "t"):
                    element = element.strip("\n")
                    finalList.append(element)
                elif (mode == "b"):
                    finalList.append(element)

    return finalList
 
# Write singular strings or lists of elements in sequence to lines in a text/binary based file.
# The mode argument must be either strings: "t" (text) or "b" (binary).
# The filepath argument must be a string. 
# The lines in the file are overwritten by the lines argument values.       
def writelines(mode, filepath, *lines):
    j = int(0)
    i = int(0)

    if (filepath != str(filepath)):
        raise TypeError("The given file path " + str(filepath) + " isn't a string!")

    if (type(mode) is not str):
        raise TypeError("The given mode " + str(mode) + " isn't a string!")

    if (path_exists(filepath) == False):
        raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

    if (isfile(filepath) == False):
        raise ValueError("The given file path " + str(filepath) + " isn't a file!")

    if (mode != "t" and mode != "b"):
        raise ValueError("The mode is of the incorrect value! It must either strings: 't' (text) or 'b' (binary)")

    print("Writing:", filepath)

    with open(filepath, "w" + mode) as new_file:
        for line in lines:      
            if (type(line) is not list and type(line) is not str):
                raise TypeError("The argument " + str(line) + " isn't a list or string!")
                
            if (mode == "t"):
                if (type(line) is str):
                    if (line == ""):
                        pass
                    elif (j == 0 and line != ""):
                        new_file.write(line)
                    else:
                        new_file.write("\n")
                        new_file.write(line)
                        
                    j += 1
                    
                if (type(line) is list):
                    if (len(line) == 0):
                        pass
                    elif (j == 0 and len(line) != 0):
                        while (i < len(line) - 1):
                            new_file.write(str(line[i]))
                            new_file.write("\n")
                            i += 1

                        new_file.write(str(line[i]))
                        i = int(0)
                    else:
                        new_file.write("\n")

                        while (i < len(line) - 1):
                            new_file.write(str(line[i]))
                            new_file.write("\n")
                            i += 1

                        new_file.write(str(line[i]))
                        i = int(0)

                    j += 1
                
            elif (mode == "b"):
                if (type(line) is str):
                    pass
                    
                if (type(line) is list):
                    if (len(line) == 0):
                        pass
                    else :
                        while (i < len(line)):
                            new_file.write(line[i])
                            i += 1

                        i = int(0)

        new_file.close()

    print("Write Success:", filepath, "written to!")

# Append singular strings or lists of elements in sequence to lines at the end of a text/binary based file. 
# The mode argument must be either strings: "t" (text) or "b" (binary).
# The filepath argument must be a string.
def appendlines(mode, filepath, *lines):
    i = int(0)

    if (filepath != str(filepath)):
        raise TypeError("The given file path " + str(filepath) + " isn't a string!")

    if (type(mode) is not str):
        raise TypeError("The given mode " + str(mode) + " isn't a string!")
         
    if (path_exists(filepath) == False):
        raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

    if (isfile(filepath) == False):
        raise ValueError("The given file path " + str(filepath) + " isn't a file!")

    if (mode != "t" and mode != "b"):
        raise ValueError("The mode is of the incorrect value! It must either strings: 't' (text) or 'b' (binary)")

    print("Appending:", filepath)

    with open(filepath, "a" + mode) as new_file:
        for line in lines:      
            if (type(line) is not list and type(line) is not str):
                raise TypeError("The argument " + str(line) + " isn't a list or string!")

            if (mode == "t"):
                if (type(line) is str):        
                    new_file.write("\n")
                    new_file.write(line)
                        
                if (type(line) is list):
                    if (len(line) == 0):
                        pass
                    else: 
                        new_file.write("\n")

                        while (i < len(line) - 1):
                            new_file.write (str(line[i]))
                            new_file.write("\n")
                            i += 1

                        new_file.write(str(line[i]))
                        i = int(0)             
            elif (mode == "b"):
                if (type(line) is str):   
                    pass
                 
                if (type(line) is list):
                    while (i < len(line)):
                        new_file.write(line[i])
                        i += 1

                    i = int(0)
                                 
        new_file.close()
            
    print("Append Success:", filepath, "appended to!")

# Return information about a file as dictionary. 
# The mode argument value can be one of the following strings: "rt", "at", "wt", "rb", "ab", "wb"
# The filepath argument must be a string. 
def attrfile(mode, filepath):
    if (filepath != str(filepath)):
        raise TypeError("The given file path " + str(filepath) + " isn't a string!")

    if (type(mode) is not str):
        raise TypeError("The given mode " + str(mode) + " isn't a string!")

    if (path_exists(filepath) == False):
        raise FileNotFoundError("The given file path " + str(filepath) + " doesn't exist!")

    if (isfile(filepath) == False):
        raise ValueError("The given file path " + str(filepath) + " isn't a file!")

    if (mode != "rt" and mode != "at" and mode != "wt" and mode != "rb" and mode != "ab" and mode != "wb"):
        raise ValueError("The mode argument must one of the following strings - 'rt', 'at', 'wt', 'rb', 'ab', 'wb' ")

    with open(filepath, mode) as new_file:
        fileAttributes = dict({ 
            "fileName": filepath,
            "fileNumber": new_file.fileno(),
            "fileMode": mode,
            "fileStreamInteractive": new_file.isatty(),
            "fileSeekability": new_file.seekable(),
            "fileReadability": new_file.readable(),
            "fileWritability": new_file.writable()
        })
        new_file.close()
        return fileAttributes

# Return boolean value (True or False) to check if a single file path exists.
# The filepath argument must be a string.
def path_exists(filepath):  
    if (filepath != str(filepath)):
        raise TypeError("The given file path " + str(filepath) + " isn't a string!")

    if (os.path.exists(filepath) == True):
        return True
    elif (os.path.exists(filepath) == False):
        return False

# Return boolean value (True or False) to check if filepath argument is a file.
# The filepath argument must be a string.
def isfile(filepath):
    if (filepath != str(filepath)):
        raise TypeError("The given file path " + str(filepath) + " isn't a string!")

    if (os.path.isfile(filepath) == True):
        return True
    elif (os.path.isfile(filepath) == False):
        return False

# Return boolean value (True or False) to check if filepath argument is a directory.
# The filepath argument must be a string.
def isdir(filepath):
    if (filepath != str(filepath)):
        raise TypeError("The given file path " + str(filepath) + " isn't a string!")

    if (os.path.isdir(filepath) == True):
        return True
    elif (os.path.isdir(filepath) == False):
        return False

'''
    Rename single/multiple files or directories.
    
    current_filepath represents the file path's name being changed.
    desired_filepath represents the file path's new intended name. 
    
    current_filepath and desired_filepath can either be:
        Two strings
        Two lists of equal length consisting of strings
'''
def ren(current_filepath, desired_filepath):
    i = int(0)

    if (type(current_filepath) is str and type(desired_filepath) is not str):
        raise TypeError("The first argument is a string, the second argument must be a string!")

    if (type(current_filepath) is list and type(desired_filepath) is not list):
        raise TypeError("The first argument is a list, the second argument must be a list!")
        
    if (type(current_filepath) is str and type(desired_filepath) is str):
        if (path_exists(current_filepath) == False):
            raise FileNotFoundError("The given file path " + str(current_filepath) + " doesn't exist!")

        print("Renaming:", current_filepath, "as", desired_filepath)
        os.rename(current_filepath, desired_filepath)
        print("Rename Success:", current_filepath, "renamed as", desired_filepath)

    if (type(current_filepath) is list and type(desired_filepath) is list):
        if (len(current_filepath) != len(desired_filepath)):
            raise ValueError("The length of the list current_filepath is not equal to the length of the list desired_filepath!")

        while(i < len(current_filepath) and i < len(desired_filepath)):
            if (type(current_filepath[i]) is not str):
                raise TypeError("The given file path " + str(current_filepath[i]) + " isn't a string!")

            if (type(desired_filepath[i]) is not str):
                raise TypeError("The given file path " + str(desired_filepath[i]) + " isn't a string!")

            if (path_exists(current_filepath[i]) == False):
                raise FileNotFoundError("The given file path " + str(current_filepath[i]) + " doesn't exist!")

            print("Renaming:", current_filepath[i], "as", desired_filepath[i])
            os.rename(current_filepath[i], desired_filepath[i])
            print("Rename Success:", current_filepath[i], "renamed as", desired_filepath[i])
            i += 1