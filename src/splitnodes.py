

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    for node in old_nodes:
        new = node.split(delimiter)
        for count in range(len(new)):
            if count % 2 == 0:
                new[count].text_type = text_type
    return new
            