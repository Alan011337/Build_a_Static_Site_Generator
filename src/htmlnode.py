class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        output = ""
        if not self.props:
            return output
        for key, value in self.props.items():
            output = output + " " + key + "=" + '"' + value + '"'
        return output

    def __repr__(self):
        return f"tag = {self.tag}\nvalue = {self.value}\nchildren = {self.children} \nprops = {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value is None:
            raise ValueError
        if not self.tag:
            return self.value
        else:
            output = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
            return output
        
    def __repr__(self):
        return f"tag = {self.tag}\nvalue = {self.value} \nprops = {self.props}"
    
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError
        if not self.children:
            raise ValueError
        else:
            output = ""
            for child in self.children:
                output += child.to_html()
            output = f"<{self.tag}{self.props_to_html()}>{output}</{self.tag}>"
            return output