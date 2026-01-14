class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props 
        
    def __eq__(self, other):
        if (self.tag == other.tag) & (self.value == other.value) & (self.children == other.children) & (self.props == other.props):
            return True
        return False
        
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
        
    def to_html(self):
        raise NotImplementedError
        
    def props_to_html(self):
        # self.props is a set of key value pairs, convert them to a string of the form " key1=value1 key2=value2"
        ans = ""
        for key, value in self.props.items():
            ans += f" {key}=\"{value}\""
        return ans

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super(LeafNode, self).__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            return "" #raise ValueError
        if self.tag == None:
            return self.value
        if self.props == None:
            my_props = ""
        else:
            my_props = self.props_to_html()
        return f"<{self.tag}{my_props}>{self.value}</{self.tag}>" 

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super(ParentNode, self).__init__(tag, None, children, props)
        
    def to_html(self):
        if self.tag == None:
            return "" #raise ValueError("tag cannot be None")
        if self.children == None:
            return "" #raise ValueError("children cannot be None")
        middle = ""
        for child in self.children:
            middle += child.to_html()
        return f"<{self.tag}>{middle}</{self.tag}>"