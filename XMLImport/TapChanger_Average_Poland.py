'''
Created on Jun 11, 2018

@author: USOMZIA
'''
import os, xml.etree.cElementTree as ET, json

currFolder = os.path.join('c:\Users','USOMZIA','Desktop','XML_Project','POLAND_CIM')
os.chdir(currFolder)
fileName = os.path.join('C:\\Users','USOMZIA','Desktop','XML_Project','POLAND_CIM','NB_CGMES_20171205_1130_EQ.xml')
tree = ET.parse(fileName)
root = tree.getroot()
print root.tag
for tabTapChanger in root.findall('{http://iec.ch/TC57/2013/CIM-schema-cim16#}RatioTapChangerTable'):
    name = tabTapChanger.find('{http://iec.ch/TC57/2013/CIM-schema-cim16#}IdentifiedObject.name')
    print 'omid', name.text
        
        


