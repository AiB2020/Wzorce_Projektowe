"A sample document to be used in the Prototype example"
import copy  
from interface_prototype import IProtoType


class Document(IProtoType):
    "A Concrete Class"

    def __init__(self, name, l):
        self.name = name
        self.list = l

    def clone(self, mode):
        " This clone method uses different copy techniques "
        if mode == 1:
           
            doc_list = self.list
        if mode == 2:
           
            doc_list = self.list.copy()
        if mode == 3:
           
            doc_list = copy.deepcopy(self.list)

        return type(self)(
            self.name,  
            doc_list  
        )

    def __str__(self):
        " Overriding the default __str__ method for our object."
        return f"{id(self)}\tname={self.name}\tlist={self.list}"
