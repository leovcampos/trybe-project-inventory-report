from datetime import date, datetime
from collections import Counter


class SimpleReport:
    def generate(list):
        update_day = date.today()
        date_validity = []

        oldest_fabrication_date = min(item["data_de_fabricacao"] for item in list)

        validity_date = [item["data_de_validade"] for item in list]
        list_validity_date = [
            datetime.strptime(item, "%Y-%m-%d").date() for item in validity_date
        ]

        for item in list_validity_date:
            if item >= update_day:
                date_validity.append(item)

        companies = Counter([item["nome_da_empresa"] for item in list])

        return (
            f"Data de fabricação mais antiga: {oldest_fabrication_date}\n"
            f"Data de validade mais próxima: {min(date_validity)}\n"
            f"Empresa com mais produtos: {companies.most_common(1)[0][0]}"
        )
