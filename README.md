# bvzcomparefiles

A python library to compare two files to each other using an md5 checksum.

This library has no dependencies outside the standard python 3.X. It was developed under python 3.10 but may work with 
previous versions of python 3.

### Installation

Download the library and make sure it exists somewhere on your PYTHONPATH.

### Usage


Import the module
```
from bvzcomparefiles import comparefiles
```

Run the compare() function, passing in the full path to the two files you want to compare. If you want to provide
pre-computed checksums for one or both of the files, that can be done using the file_a_checksum and file_b_checksum
parameters. In that case, those would be used instead of re-computing the md5 checksum for the file in question. If
left unset, or set to None, then new checksums will be calculated for each file.

The result of the compare function will either be the checksum that both files share, or False if they are not identical
files.
```
result = comparefiles.compare(file_a_p="/file/path/a",
                              file_b_p="/file/path/b",
                              file_a_checksum=None,
                              file_b_checksum=None)
```

See the included sample.py file for a fuller example on how to use this library.
