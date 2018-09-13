import xml.etree.cElementTree as ET
import os, json
os.chdir('C:\\Users\\USOMZIA\\Desktop\\XML_Project\\ISEM_CIM')
fileName = os.path.join('C:\\Users','USOMZIA','Desktop','XML_Project','NB_CGMES_20171205_1130_EQ.xml')
tree = ET.parse(fileName)
root = tree.getroot()
print root.tag
print root.attrib

with open('temp1.txt', 'w') as f:
    for childFirst in root:
        f.write(childFirst.tag + '\n')
        f.write('\t')
        for childSecond in childFirst:
            f.write(childSecond.tag + '\n')
            f.write('\t\t')
            # to dump a dictionary into a text file you need to use this json library
            f.write(json.dumps(childSecond.attrib))
            f.write('\n')
        
with open('temp2.txt', 'w') as f:
    for child in root:
        if 'ACLineSegment' in child.attrib.values():
            f.write(json.dumps(child.attrib) + '\n')
            
with open('temp3.txt', 'w') as f:
    # the following is to search the entire root for ACLineSegment Node!
    for line in root.findall('{http://iec.ch/TC57/2013/CIM-schema-cim16#}ACLineSegment'):
        for child in line:
            print child.attrib
        testTemp = line.find('{http://iec.ch/TC57/2013/CIM-schema-cim16#}ACLineSegment.bch')
        f.write(testTemp.text)
        f.write('\n')

#omid = root.findall(".//xs:element[@source=[@substitutionGroup='rdf:RDFResource']")
'''
omid = root.findall("//cim:ConformLoad//cim:ConformLoad.LoadGroup[@rdf:resource='#c3b962e9-9389-4337-9582-ed0a2044edbe']")
for item in omid:
    print item
'''
    
        

