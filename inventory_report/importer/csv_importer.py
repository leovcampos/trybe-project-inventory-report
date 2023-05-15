from inventory_report.importer.importer import Importer
import csv


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, file_name):
        file_list = []
        if file_name.endswith(".csv"):
            with open(file_name) as csv_file:
                file_reader = csv.DictReader(
                    csv_file, delimiter=",", quotechar='"')
                for role in file_reader:
                    file_list.append(role)
                return file_list
        else:
            raise ValueError('Arquivo inválido')
