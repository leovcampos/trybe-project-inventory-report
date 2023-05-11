from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport:
    def generate(list):
        report = ""

        companies = Counter([item["nome_da_empresa"] for item in list])
        for company, times in companies.items():
            report += f"- {company}: {times}\n"

        return (
            f"{SimpleReport.generate(list)}\n"
            f"Produtos estocados por empresa:\n"
            f"{report}"
        )
