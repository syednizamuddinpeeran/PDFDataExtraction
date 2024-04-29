from typing import List, Self

class bbox:
    def __init__(self,x,y,h,w) -> None:
        self.x =x
        self.y=y
        self.h=h
        self.w=w
    def __str__(self) -> str:
        return "{" + f"x:{self.x},y:{self.y},h:{self.w},h:{self.w}" + "}"
    @property
    def x(self)->int: return self._x
    @x.setter
    def x(self, value:int):
        self._x = value
    @property
    def y(self)->int: return self._y
    @x.setter
    def y(self, value:int):
        self._y = value
    
    @property
    def h(self)->int: return self._h
    @h.setter
    def h(self, value:int):
        self._h = value
    
    @property
    def w(self)->int: return self._w
    @h.setter
    def w(self, value:int):
        self._w = value

class element:
    def __init__(self,bbox:bbox) -> None:
        self._bbox = bbox
    @property
    def bbox(self)->bbox: return self._bbox

    @bbox.setter
    def value(self, value:bbox):
        self._bbox = value
class text(element):
    def __init__(self, bbox:bbox,value:str) -> Self:
        super().__init__(bbox)
        self._value = value
    def __init__(self, value:str) -> None:
        super().__init__(None)
        self._value = value
    @property
    def value(self)->str: 
        return self._value
    @value.setter
    def value(self, value:str):
        self._value = value
    def __str__(self) -> str:
        return f"Bound Box: {self.bbox}" + "\n" + f"Text :{self.value}" 
class image(element):
    def __init__(self, bbox: bbox,value:bytes) -> None:
        super().__init__(bbox)
        self._value = value
    def __init__(self,value:bytes) -> None:
        super().__init__(None)
        self._value = value
    @property
    def value(self)->bytes: return self._value
    @value.setter
    def value(self, value:bytes):
        self._value = value
class page:
    def __init__(self) -> Self:
        self._elements = []
        self._text = ""
    @property
    def elements(self)->List[element]: 
        return self._elements
    @elements.setter
    def elements(self, value:List[element]):
        self._elements = value
    @property
    def text(self)->str:
        if self._text == "":
            _text = "" 
            for ele in self.elements:
                if type(ele) is text:    
                    _text += ele.value
            self._text = _text
            return _text
        else :
            return self._text 
    @text.setter
    def text(self, value:str):
        self._text = value
class pdf:
    def __init__(self,filePath) -> Self:
        self._pages = []
        self._filePath =filePath

    @property
    def filePath(self)->str: 
        return self._filePath
    
    @filePath.setter
    def filePath(self, value:str):
        self._filePath = value

    @property
    def pages(self)->List[page]: 
        return self._pages
    @pages.setter
    def pages(self, value:List[page]):
        self._pages = value