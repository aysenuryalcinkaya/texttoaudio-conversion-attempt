import xml.etree.ElementTree as ET

def metin_to_xml(metin_dosyasi, xml_dosyasi):
    with open(metin_dosyasi, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    root = ET.Element('root')

    for line in lines:
        line = line.strip()
        if line:
            element = ET.SubElement(root, 'line')
            element.text = line

    tree = ET.ElementTree(root)
    tree.write(xml_dosyasi, encoding='utf-8', xml_declaration=True)

# Örnek kullanım
metin_dosyasi = 'aa.txt'
xml_dosyasi = 'metin.xml'
metin_to_xml(metin_dosyasi, xml_dosyasi)
