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
        print(f"OBJ: {objDict}")
        model.append(objDict)
    return model

if __name__ == '__main__':
    load_dotenv()
    DATABASE_URL=os.environ.get('DATABASE_URL')

    model = sparxmodel.Sparxmodel(DATABASE_URL)
 
    q = select(sparxmodel.Object).where(sparxmodel.Object.name == 'FagelementansvarligEnhed')  
    items :List[sparxmodel.Object] = model.exec(q).all()
    d=dump(items)
    with open('output.json', 'w') as f:
        json.dump(d, f, indent=4)

