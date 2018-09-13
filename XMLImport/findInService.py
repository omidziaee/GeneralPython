from __future__ import print_function
import xml.etree.cElementTree as ET
import sys, os, json



class ActiveElemFinder:
    def __init__(self, tagInFile, searchActiveElem):
        self.inFile1 = tagInFile;
        self.inFile2 = searchActiveElem
        try:
            print("Reading \"{}\" into memory." .format(self.inFile1), end=' ')
            with open(self.inFile1) as f:
                self.rawTagFile = f.read()
            print("\nDone with reading the file \"{}\"".format(self.inFile1))
        except IOError:
            print("\nFile \"%s\" can not be found." %(self.inFile1))
            
                
                
if __name__ == "__main__":
    mainPath = "C:\\Users\\USOMZIA\\Desktop\\XML_Project"
    tagInFile = mainPath + "\\NB_CGMES_20171205_1130_EQ.xml"
    searchActiveElem = mainPath + "\\NB_CGMES_20171205_1130_SSH.xml"
    ActiveLine = ActiveElemFinder(tagInFile, searchActiveElem)

        
        