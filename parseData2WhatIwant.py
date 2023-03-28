from parseXML2EXCEL import *

class parseData2WhatIwant(parseXML2EXCEL):
    def __init__(self, xml_file, excel_file):
        super().__init__(xml_file, excel_file)

    def parse(self):
        for i, child in enumerate(self.root):
            for j, subchild in enumerate(child):
                if subchild.tag == 'name':
                    self.ws.cell(row=i + 1, column=j + 1).value = subchild.text
        self.wb.save(self.excel_file)


if __name__ == "__main__":
    xml_file = "data.xml"
    excel_file = "data.xlsx"
    parseData2WhatIwant = parseData2WhatIwant(xml_file, excel_file)
    parseData2WhatIwant.parse()