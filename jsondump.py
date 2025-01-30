import os
import sparxmodel
from sqlmodel import select
from dotenv import load_dotenv
from typing import List
from pprint import pprint as print
import json



def dump(items):
    model=[]
    for item in items:
        objDict=item.model_dump()
        for prop in item.properties:
            propDict=prop.model_dump()
            objDict[propDict['property']]=propDict['value']            
        
        attrList=[]
        for attr in item.attributes:
            attrDict=attr.model_dump()
            for tag in attr.tags:
                tagDict=tag.model_dump()
                attrDict[tagDict['property']]=tagDict['value']
            attrList.append(attrDict)
        objDict['attributes']=attrList

        diagramList=[]
        for diagramobj in item.diagramobjects:
            diagram= diagramobj.diagram.model_dump()
            diagramList.append(diagram)
        model.append(objDict)
    return model


def ObjectsInPackageRecursive(package : sparxmodel.Package) -> List[sparxmodel.Object]:
    """Recursively get all objects in a package not including the packages itself"""

    objects: List[sparxmodel.Object] =[]
    for subpackage in package.children:
        subobj=ObjectsInPackageRecursive(subpackage)
        objects=objects+subobj
    for obj in package.objects:
        if obj.object_type != 'Package':
            objects.append(obj)
    return objects

if __name__ == '__main__':
    load_dotenv()
    DATABASE_URL=os.environ.get('DATABASE_URL') # ex. mysql+pymysql://user:password@server.com/mydatabase?charset=utf8mb4

    model = sparxmodel.Sparxmodel(DATABASE_URL)
 
    q = select(sparxmodel.Package).where(sparxmodel.Package.name == 'SIS DEV5')
    package = model.exec(q).first()
    objects = ObjectsInPackageRecursive(package)
    print(f"Found {len(objects)} objects in package {package.name}")
    d=dump(objects)
    #with open('output.json', 'w') as f: json.dump(d, f, indent=4)

