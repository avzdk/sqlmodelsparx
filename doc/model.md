## Model

```mermaid

classDiagram

Object --* Package
Object --> Xref
Attribute --* Object
AttributeTag --* Attribute
Object --> Object
Diagram --* Package
Diagramlink --> Diagram
Connector --> Object : Target
Connector --> Object : Source
ConnectorTag --* Connector
Diagramlink --> Connector
ObjectProperties --* Object

class Object {
    object_id
    name
    object_type
    note
    stereotype
    abstract
}

class ObjectProperties{
    propertyID
    object_id
    property
    value
    notes
}


```



See : https://github.com/avzdk/sparx/tree/main/Documentation