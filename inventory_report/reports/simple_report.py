from datetime import date, datetime
from collections import Counter


class SimpleReport:
    def generate(list):
        update_day = date.today()
        date_validity = []

        fabrication_date = [item["data_de_fabricacao"] for item in list]
        f_fabrication_date = [
            datetime.strptime(item, "%Y-%m-%d") for item in fabrication_date
        ]

        validity_date = [item["data_de_validade"] for item in list]
        f_validity_date = [
            datetime.strptime(item, "%Y-%m-%d") for item in validity_date
        ]

        for item in f_validity_date:
            if f_validity_date >= update_day:
                date_validity.append(item)

        companies = Counter([item["nome_da_empresa"] for item in list])

        return f"""Data de fabricação mais antiga: {min(f_fabrication_date)}
                Data de validade mais próxima: {min(date_validity)}
                Empresa com mais produtos: {companies.most_common(1)[0]}"""
