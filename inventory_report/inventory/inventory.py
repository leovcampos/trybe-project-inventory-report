from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

import json
import csv
import xmltodict


class Inventory:
    @staticmethod
    def JsonImporter(path):
        path_type = path.split(".")[-1]
        if path_type != "json":
            raise ValueError("Invalid")
        with open(path, encoding="utf8") as file:
            return json.load(file)

    @staticmethod    
    def CsvImporter(path):
        path_type = path.split(".")[-1]
        if path_type != "csv":
            raise ValueError("Invalid")
        with open(path, newline="", encoding="utf8") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
        
    @staticmethod
    def XmlImporter(path):
        path_type = path.split(".")[-1]
        if path_type != "xml":
            raise ValueError("Invalid")
        with open(path, encoding="utf-8") as file:
            return xmltodict.parse(file.read())["dataset"]["record"]

    @staticmethod
    def read(path):
        path_especific = path.split(".")[-1]
        if path_especific == "csv":
            return Inventory.CsvImporter(path)
        elif path_especific == "json":
            return Inventory.JsonImporter(path)
        elif path_especific == "xml":
            return Inventory.XmlImporter(path)

    @staticmethod
    def import_data(path, type):
        result = Inventory.read(path)
        if type == "simples":
            return SimpleReport.generate(result)
        elif type == "completo":
            return CompleteReport.generate(result)
