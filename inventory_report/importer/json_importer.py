import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if 'json' in path:
            with open(path, encoding="utf-8") as file:
                content = file.read()
                products_list = json.loads(content)
        else:
            raise ValueError('Arquivo inválido')

        return products_list
