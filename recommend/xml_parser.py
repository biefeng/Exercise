from xml.dom.minidom import parse as parse

document = parse("D:\\program\\apache-tomcat-8.5.38\\conf\\server.xml")


def handle_node(node):
    print("nodeName: " + node.nodeName)

    attributes = node.attributes
    if attributes is not None:
        for index in range(len(attributes)):
            attr = attributes.item(index)
            if attr is not None:
                print("attrName: ", end="")
                print(attr.name)
                print("attrValue: ", end="")
                print(attr.value)
    print("nodeValue: ", end="")
    print(node.nodeValue)
    print("---------------------")


def iterate_nodes(root):
    if root is None:
        return
    handle_node(root)
    if root.hasChildNodes():
        nodes = root.childNodes
        for node in nodes:
            handle_node(node)
            if node.hasChildNodes():
                iterate_nodes(node)


iterate_nodes(document.documentElement)
