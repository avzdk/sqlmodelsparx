import os
from sparxmodel import Sparxmodel, Object, Attribute, Package
from sqlmodel import select
from dotenv import load_dotenv

if __name__ == '__main__':
    load_dotenv()
    DATABASE_URL=os.environ.get('DATABASE_URL')

    model = Sparxmodel(DATABASE_URL)

 
    q = select(Attribute)
    items = model.exec(q).all()

    for item in items:
        print(item.object_id, item.name, item.object.name)