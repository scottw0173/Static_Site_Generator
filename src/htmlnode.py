class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag= tag
        self.value= value
        self.children= children
        self.props= props
    

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        prop_string = ""
        if self.props == None:
            return prop_string
        for llave in self.props:
            prop_string += f' {llave}="{self.props[llave]}" '
        return prop_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("No value in self.value")
        elif not self.tag:
            return self.value
        elif self.props == None:
            string_start = f'<{self.tag}>'
            string_end = f'</{self.tag}>'
            html_string = string_start + self.value + string_end
            return html_string
        else:
            string_start = f'<{self.tag}'
            string_end = f'</{self.tag}>'
            props_string = ""
            for llave in self.props:
                props_string += f' {llave}="{self.props[llave]}" '
            total_string = string_start + props_string + self.value + string_end
            return total_string
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, {self.props})'
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)
    
    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing HTML tag")
        if self.children == None:
            raise ValueError("Missing kids")
        
        