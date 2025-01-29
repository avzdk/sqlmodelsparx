from sqlmodel import Session, Field, Relationship, SQLModel, create_engine, select




class Sparxmodel():
    def __init__(self, url):
        self.engine = create_engine(echo=True, url=url) 
        self.session = Session(self.engine) 

    def exec(self, query):
        return self.session.exec(query)

class Object(SQLModel, table=True):
    __tablename__ = 't_object'
    object_id: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    name: str 
    attributes: list["Attribute"] = Relationship(back_populates="object")

class Attribute(SQLModel, table=True):
    __tablename__ = 't_attribute'
    id: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    name: str
    object_id: int = Field(foreign_key="t_object.object_id")
    object: "Object" = Relationship(back_populates="attributes")

class Package(SQLModel, table=True):
    __tablename__ = 't_package'
    Package_ID: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    name: str

if __name__ == '__main__':
    None