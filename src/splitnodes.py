from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for node in old_nodes:
        new = node.split(delimiter)
        for count in range(len(new)):
            if count % 2 == 0:
                new[count].text_type = text_type
    return new

def split_nodes_image(old_nodes):
    text_node_list = []
    image = False
    remainder = old_nodes[0]
    index = remainder.find("[")
    while len(remainder) > 0:
        if remainder[0] == "!":
            image = True
        else:
            image = False

        if image:
            text = remainder[2:remainder.find("]")]
            url = remainder[remainder.find("(")+1:remainder.find(")")]
            text_node_list.append(text, TextType.IMAGE, url)
            index = remainder.find(")")+1
            remainder = remainder[index:]
            if remainder.find("[") == -1:
                text_node_list.append(remainder, TextType.TEXT)
                remainder = ""
        else:
            text_node_list.append(remainder[:index-1], TextType.TEXT)
            index = remainder.find("[")-1
            
        
            

def split_nodes_link(old_nodes):
    pass