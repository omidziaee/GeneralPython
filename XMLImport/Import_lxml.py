from lxml import etree
import os
# Class common attributs
CIM_SCHEMA_NAME = "{http://iec.ch/TC57/2013/CIM-schema-cim16#}"

class SchemaExtract(object):
    # constructor
    def __init__(self, xmlFile):
        self.root = etree.parse(xmlFile)
        
    def findAll(self, nodePath):
        return self.root.findall(nodePath.replace("cim:", CIM_SCHEMA_NAME))
    
    def find(self, nodePath):
        return self.root.find(nodePath.replace("cim:", CIM_SCHEMA_NAME)) 
    
    def names_of(self, nodes):
        pass
    
    
    
    
    
if __name__ == '__main__':
    os.chdir()
     with open('') as xmlFile:
         schemaExtract = SchemaExtract
         