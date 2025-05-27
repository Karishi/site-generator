class HTMLNode():
    def __init__(self, tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def toHTML(self):
        raise NotImplementedError()
    
    def props_to_HTML(self):
        if not self.props:
            return ""
        output = ""
        for key in self.props:
            output += f' {key}="{self.props[key]}"'
        return output
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"