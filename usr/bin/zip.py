 
import os
   
import zipfile


def main(argc: int, argv: list):
    """ ZIP FILE TEST """
    fn = zipfile.ZipFile("test.zip", 'w')
    fn.write("./usr/bin/cat.py")
    fn.close()