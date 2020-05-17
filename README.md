# ***filewrap***

    A Python module for file/archive manipulation & management.
    Built-in modules used: os, tarfile, gzip, zipfile, zlib

    Make sure to have the latest version of Python 3 installed although this should work with previous versions. 
    Pip and git also need to be installed for module installation with command line.  

    To install/update the module with pip enter command in terminal:
        pip install git+https://github.com/CodeConfidant/filewrap-os.git#egg=filewrap-os

    To uninstall the module with pip enter command in terminal:
        pip uninstall filewrap

<table width="100%">
	<tr>
		<th align="left">
            Method
        </th>
		<th align="left">
            Description
        </th>
	</tr>
    <tr>
		<td>
            <code>copydir(destination_path, target_path)</code>
        </td>
		<td>
            Copy target directory and all of it's subdirectories/files to a destination directory.
        </td>
	</tr>
    <tr>
		<td>
            <code>copyfile(destination_path, *filepaths)</code>
        </td>
		<td>
            Copy single/multiple files to destination directory. <br/>
            The destination_path and *filepaths arguments must be strings.
        </td>
	</tr>
	<tr>
		<td>
            <code>rpfile(mode, *filepaths)</code>
        </td>
		<td>
            Read and print lines in single/multiple text/binary based files. <br/>
            The mode argument must be either strings: "t" (text) or "b" (binary). <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rmfile(*filepaths)</code>
        </td>
		<td>
            Delete single/multiple files. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>mkfile(mode, *filepaths)</code>
        </td>
		<td>
            Make single/multiple text/binary based files. <br/>
            The mode argument must be either strings: "t" (text) or "b" (binary). <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rmdir(*filepaths)</code>
        </td>
		<td>
            Delete single/multiple directories. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rmall(dirpath)</code>
        </td>
		<td>
            Delete single directory along with it's subdirectories and files. <br/>
            Use this with caution, as you could delete your entire file system if you're not careful.
        </td>
	</tr>
    <tr>
		<td>
            <code>mkdir(*filepaths)</code>
        </td>
		<td>
            Make single/multiple directories. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>rpdir(*filepaths)</code>
        </td>
		<td>
            Output to terminal the file/subdirectory names of single/multiple argument filepaths. <br/>
            Use no arguments for working directory only. <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>lsdir(*filepaths)</code>
        </td>
		<td>
            Return a list with file/subdirectory names of the single/multiple argument filepaths. <br/>
            If there are no arguments used in *filepaths, a list of the contents within the working directory is returned. <br/>
            If there is only one argument used in *filepaths, a list of the contents of only that filepath directory is returned. <br/>
            Using the method with two or more arguments in *filepaths will return a list of lists with each list containing the file/subdirectory names of that filepath argument.
        </td>
	</tr>
    <tr>
		<td>
            <code>chdir(filepath)</code>
        </td>
		<td>
            Change current working directory. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>wdir()</code>
        </td>
		<td>
            Return string of the path of the current working directory.
        </td>
	</tr>
    <tr>
		<td>
            <code>pwdir()</code>
        </td>
		<td>
            Print working directory to terminal.
        </td>
	</tr>
    <tr>
		<td>
            <code>mklist(mode, *filepaths)</code>
        </td>
		<td>
            Return a list from lines in single/multiple text/binary based files. <br/>
            The mode argument must be either strings: "t" (text) or "b" (binary). <br/>
            The *filepaths arguments must be strings.
        </td>
	</tr>
    <tr>
		<td>
            <code>writelines(mode, filepath, *lines)</code>
        </td>
		<td>
            Write singular strings or lists of elements in sequence to lines in a text/binary based file. <br/>
            The mode argument must be either strings: "t" (text) or "b" (binary). <br/>
            The filepath argument must be a string. <br/>
            The lines in the file are overwritten by the lines argument values.
        </td>
	</tr>
    <tr>
		<td>
            <code>appendlines(mode, filepath, *lines)</code>
        </td>
		<td>
            Append singular strings or lists of elements in sequence to lines at the end of a text/binary based file. <br/> 
            The mode argument must be either strings: "t" (text) or "b" (binary). <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>attrfile(mode, filepath)</code>
        </td>
		<td>
            Return information about a file as dictionary. <br/>
            The mode argument value can be one of the following strings: "rt", "at", "wt", "rb", "ab", "wb" <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>path_exists(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if a single file path exists. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>isfile(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a file. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>isdir(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a directory. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>istar(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a tar archive. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>iszip(filepath)</code>
        </td>
		<td>
            Return boolean value (True or False) to check if filepath argument is a zip archive. <br/>
            The filepath argument must be a string.
        </td>
	</tr>
    <tr>
		<td>
            <code>ren(current_filepath, desired_filepath)</code>
        </td>
		<td>
            Rename single/multiple files or directories. <br/>
            current_filepath represents the file path's name being changed. <br/>
            desired_filepath represents the file path's new intended name. <br/>
            current_filepath and desired_filepath can either be:
            <ul>
                <li>Two strings</li>
                <li>Two lists of equal length consisting of strings</li>
            </ul>
        </td>
	</tr>
    <tr>
		<td>
            <code>tar_wrap(filepath)</code>
        </td>
		<td>
            Create a tar archive with gzip compression & .gz extension.
        </td>
	</tr>
    <tr>
		<td>
            <code>tar_extract(filepath)</code>
        </td>
		<td>
            Extract a tar gzip archive contents to working directory.
        </td>
	</tr>
     <tr>
		<td>
            <code>zip_wrap(filepath)</code>
        </td>
		<td>
            Create a zip archive with DEFLATE compression.
        </td>
	</tr>
    <tr>
		<td>
            <code>zip_extract(filepath)</code>
        </td>
		<td>
            Extract a zip archive contents to working directory.
        </td>
	</tr>
</table>

[Back to Top](#filewrap)

---
