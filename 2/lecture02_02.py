import xml.etree.ElementTree as ET

def lecture02_02() -> None:
    root = ET.Element('book')
    article = ET.SubElement(root, 'article')
    article.attrib = {'title': '卒業論文'}
    chapters= []
    
    for i in range(6):
        chapter = ET.SubElement(article, 'chapter')
        chapter.attrib['id'] = str(i)
        match i:
            case 0:
                chapter.attrib['name'] = str('はじめに')
                chapter.attrib['pages'] = str(2)
            case 1:
                chapter.attrib['name'] = str("基礎理論")
                chapter.attrib['pages'] = str(8)
            case 2:
                chapter.attrib['name'] = str("実験方法")
                chapter.attrib['pages'] = str(6)
            case 3:
                chapter.attrib['name'] = str("結果と考察")
                chapter.attrib['pages'] = str(2)
            case 4:
                chapter.attrib['name'] = str("まとめ")
                chapter.attrib['pages'] = str(1)
            case 5:
                chapter.attrib['name'] = str("参考文献")
                chapter.attrib['pages'] = str(2)
        chapters.append(chapter)

    novel = ET.SubElement(root,'novel')
    for i in range(5):
        chapter = ET.SubElement(novel, 'chapter')
        chapter.attrib['id'] = str(i)
        match i:
            case 0:
                chapter.attrib['name'] = str('1日の始まり')
                chapter.attrib['pages'] = str(2)
            case 1:
                chapter.attrib['name'] = str('朝食')
                chapter.attrib['pages'] = str(8)
            case 2:
                chapter.attrib['name'] = str('仕事')
                chapter.attrib['pages'] = str(6)
            case 3:
                chapter.attrib['name'] = str('帰宅後')
                chapter.attrib['pages'] = str(2)
            case 4:
                chapter.attrib['name'] = str('新しい朝')
                chapter.attrib['pages'] = str(1)

    with open('lecture02_02_data.xml', 'wb') as f:
        import xml.dom.minidom as md
        f.write(md.parseString(ET.tostring(root, encoding='utf-8', xml_declaration=True)).toprettyxml(indent='  ',encoding="utf-8"))


if __name__ == '__main__':
    lecture02_02()