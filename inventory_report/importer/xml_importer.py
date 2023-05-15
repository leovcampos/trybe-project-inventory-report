import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if 'xml' in path:
            with open(path, encoding="utf-8") as file:
                products = xmltodict.parse(file.read())
                products_list = products['dataset']['record']
        else:
            raise ValueError('Arquivo inválido')

        return products_list
