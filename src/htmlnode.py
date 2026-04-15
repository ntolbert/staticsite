


class HTMLNode:
    def __init__(self,tag = None,value= None,children= None,props= None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self. props = props
    def to_html(self):
        raise NotImplementedError("Child classes will override this method to render themselves as HTML")
    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html
    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None) -> None:
        super().__init__(tag=tag,children=children,props =props)
        self.tag = tag
        self.children = children
    def to_html(self):
        if self.tag is None:
            raise ValueError("all parentNodes must have a tag(s)")
        if self.children is None:
            raise ValueError("all parentNodes must have a child(ren)")
        html_child = "" 
        for child in self.children:
            html_child += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{html_child}</{self.tag}>"
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
class LeafNode(HTMLNode):
    def __init__(self, tag, value,props = None) -> None:
        super().__init__(tag=tag,value=value,props=props)
        self.tag = tag
        self.value = value
    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have value.")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    
    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

