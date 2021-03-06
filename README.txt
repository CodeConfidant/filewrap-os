filewrap

A Python package for file/archive manipulation & management.

Make sure to have the latest version of Python 3 installed although this should work with previous versions. 

To install the package with pip enter command in terminal:
    pip install filewrap

To uninstall the package with pip enter command in terminal:
    pip uninstall filewrap

Built-in modules used: os, tarfile, gzip, zipfile, zlib

copydir(destination_path, target_path): 	Copy target directory and all of it's subdirectories/files to a destination directory.

copyfile(destination_path, *filepaths): 	Copy single/multiple files to destination directory.
                                            The destination_path and *filepaths arguments must be strings.

read(filepath):                         Read the binary from a file and return.
                                        The filepath argument must be a string.                

write(filepath, data):                  Write bytes object to a file.
                                        The filepath argument must be a string.
                                        The data argument must be a bytes object.

rpfile(mode, *filepaths): 	            Read and print lines in single/multiple text/binary based files.
                                        The mode argument must be either strings: "t" (text) or "b" (binary).
                                        The *filepaths arguments must be strings.

rmfile(*filepaths): 	                Delete single/multiple files.
                                        The *filepaths arguments must be strings.

mkfile(mode, *filepaths): 	            Make single/multiple text/binary based files.
                                        The mode argument must be either strings: "t" (text) or "b" (binary).
                                        The *filepaths arguments must be strings.

rmdir(*filepaths):                   	Delete single/multiple directories.
                                        The *filepaths arguments must be strings.

rmall(dirpath): 	                    Delete single directory along with it's subdirectories and files.
                                        Use this with caution, as you could delete your entire file system if you're not careful.

mkdir(*filepaths): 	                    Make single/multiple directories.
                                        The *filepaths arguments must be strings.

rpdir(*filepaths):	                    Output to terminal the file/subdirectory names of single/multiple argument filepaths. 
                                        Use no arguments for working directory only. 
                                        The *filepaths arguments must be strings.

lsdir(*filepaths):	                    Return a list with file/subdirectory names of the single/multiple argument filepaths. 
                                        If there are no arguments used in *filepaths, a list of the contents within the working directory is returned. 
                                        If there is only one argument used in *filepaths, a list of the contents of only that filepath directory is returned. 
                                        Using the method with two or more arguments in *filepaths will return a list of lists with each list containing the file/subdirectory names of that filepath argument.

chdir(filepath): 	                    Change current working directory.
                                        The filepath argument must be a string.

wdir(): 	                            Return string of the path of the current working directory.

pwdir(): 	                            Print working directory to terminal.

mklist(*filepaths): 	                Return a list from lines in single/multiple text based files.
                                        The *filepaths arguments must be strings.

writelines(filepath, *lines): 	        Write singular strings or lists of strings in sequence to lines in a text based file.
                                        The filepath argument must be a string.
                                        The lines in the file are overwritten by the lines argument values.

appendlines(filepath, *lines): 	        Append singular strings or lists of strings in sequence to lines at the end of a text based file.
                                        The filepath argument must be a string.

path_exists(filepath): 	                Return boolean value (True or False) to check if a single file path exists.
                                        The filepath argument must be a string.

isfile(filepath): 	                    Return boolean value (True or False) to check if filepath argument is a file.
                                        The filepath argument must be a string.

isdir(filepath): 	                    Return boolean value (True or False) to check if filepath argument is a directory.
                                        The filepath argument must be a string.

istar(filepath): 	                    Return boolean value (True or False) to check if filepath argument is a tar archive.
                                        The filepath argument must be a string.

iszip(filepath): 	                    Return boolean value (True or False) to check if filepath argument is a zip archive.
                                        The filepath argument must be a string. 

ren(current_filepath, desired_filepath): Rename single/multiple files or directories.
                                         current_filepath represents the file path's name being changed.
                                         desired_filepath represents the file path's new intended name.
                                         current_filepath and desired_filepath can either be:
                                            Two strings
                                            Two lists of equal length consisting of strings

tar_wrap(filepath): 	                Create a tar archive with gzip compression & .gz extension.

tar_extract(filepath): 	                Extract a tar gzip archive contents to working directory.

zip_wrap(filepath): 	                Create a zip archive with DEFLATE compression.

zip_extract(filepath): 	                Extract a zip archive contents to working directory.

filecount(filepath):                    Count and return the number of files within a directory.

dircount(filepath):                     Count and return the number of directories within a directory.