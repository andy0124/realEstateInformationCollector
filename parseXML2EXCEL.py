import xml.etree.ElementTree as ET
from openpyxl import Workbook


class parseXML2EXCEL:
    def __init__(self, xml_file, excel_file):
        self.xml_file = xml_file
        self.excel_file = excel_file
        self.tree = ET.parse(self.xml_file)
        self.root = self.tree.getroot()
        self.wb = Workbook()
        self.ws = self.wb.active

    def parse(self):
        for i, child in enumerate(self.root):
            for j, subchild in enumerate(child):
                self.ws.cell(row=i + 1, column=j + 1).value = subchild.text
        self.wb.save(self.excel_file)