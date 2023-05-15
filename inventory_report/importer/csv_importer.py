import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if 'csv' in path:
            with open(path, encoding="utf-8") as file:
                products_dict = csv.DictReader(file)
                products_list = [row for row in products_dict]
        else:
            raise ValueError('Invalid')

        return products_list
