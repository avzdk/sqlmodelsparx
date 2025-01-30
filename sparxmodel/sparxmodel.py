from sqlmodel import Session, Field, Relationship, SQLModel, create_engine, select


class Sparxmodel():
    def __init__(self, url):
        self.engine = create_engine(url=url) 
        self.session = Session(self.engine) 

    def exec(self, query):
        return self.session.exec(query)


class Object(SQLModel, table=True):
    __tablename__ = 't_object'
    object_id: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    name: str 
    object_type : str 
    Note : str
    Stereotype : str
    Abstract : bool
    attributes: list["Attribute"] = Relationship(back_populates="object")
    properties: list["ObjectProperty"] = Relationship(back_populates="object")
    ea_guid: str
    package_id: int = Field(foreign_key="t_package.package_id")
    package: "Package" = Relationship(back_populates="objects")
    diagramobjects: list["Diagramobject"] = Relationship(back_populates="object")

class Attribute(SQLModel, table=True):
    __tablename__ = 't_attribute'
    id: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    name: str
    object_id: int = Field(foreign_key="t_object.object_id")
    object: "Object" = Relationship(back_populates="attributes")
    tags: list["AttributeTag"] = Relationship(back_populates="attribute")
    stereotype: str
    LowerBound: str
    UpperBound: str
    Derived: bool
    ea_guid: str

class ObjectProperty(SQLModel, table=True):
    __tablename__ = 't_objectproperties'
    propertyID: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    object_id: int = Field(foreign_key="t_object.object_id")
    property: str
    value: str
    notes: str
    object: "Object" = Relationship(back_populates="properties")

class AttributeTag(SQLModel, table=True):
    __tablename__ = 't_attributetag'
    propertyID: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    elementID: int = Field(foreign_key="t_attribute.id")
    property: str
    value: str
    notes: str
    attribute: "Attribute" = Relationship(back_populates="tags")

class Package(SQLModel, table=True):
    __tablename__ = 't_package'
    package_id: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    objects: list["Object"] = Relationship(back_populates="package")
    name: str
    parent_id: int = Field(foreign_key="t_package.package_id")
    children: list["Package"] = Relationship()
    ea_guid: str
    diagrams: list["Diagram"] = Relationship(back_populates="package")

class Diagram(SQLModel, table=True):
    __tablename__ = 't_diagram'
    diagram_id : int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    name: str
    package_id: int = Field(foreign_key="t_package.package_id")
    package: "Package" = Relationship(back_populates="diagrams")
    diagramobjects: list["Diagramobject"] = Relationship(back_populates="diagram")
    ea_guid: str

class Diagramobject(SQLModel, table=True):
    __tablename__ = 't_diagramobjects'
    id: int | None = Field(default=None, primary_key=True)   #None = autoincrement in database
    diagram_id: int = Field(foreign_key="t_diagram.diagram_id")
    object_id: int = Field(foreign_key="t_object.object_id")
    diagram: "Diagram" = Relationship(back_populates="diagramobjects")
    object: "Object" = Relationship(back_populates="diagramobjects")

if __name__ == '__main__':
    None