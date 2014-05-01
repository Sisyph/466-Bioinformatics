import os
import fnmatch

def getFiles(pattern):
        files = []
        for root, dirnames, filenames in os.walk('data'):
                for filename in fnmatch.filter(filenames, pattern):
                      files.append(os.path.join(root, filename))
        return files
