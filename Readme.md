A simple script tool to help in migrating php files to html files for a django template.
Useful when using third-party html template for your designs.
This script will mostly be used by the backend guys.

Features
1. Changes all php extension to html
2. Changes all php include tag to django's include tag
3. Clean up php semi-colon in every scripts

How to use
python transpose.py /home/path/to/base/folder/of/php/files fromExtension toExtension