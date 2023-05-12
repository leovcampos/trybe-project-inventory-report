from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

products = [
    {
        "id": 1,
        "nome_do_produto": "Product 1",
        "nome_da_empresa": "Company",
        "data_de_fabricacao": "2022-06-10",
        "data_de_validade": "2024-06-10",
        "numero_de_serie": "1234",
        "instrucoes_de_armazenamento": "Manusear com cuidado"
    },
    {
        "id": 2,
        "nome_do_produto": "Product 2",
        "nome_da_empresa": "Company",
        "data_de_fabricacao": "2021-06-10",
        "data_de_validade": "2024-06-10",
        "numero_de_serie": "1234",
        "instrucoes_de_armazenamento": "Manusear com cuidado"
    },
    {
        "id": 1,
        "nome_do_produto": "Product 3",
        "nome_da_empresa": "Company 1",
        "data_de_fabricacao": "2022-06-10",
        "data_de_validade": "2023-06-10",
        "numero_de_serie": "1234",
        "instrucoes_de_armazenamento": "Manusear com cuidado"
    },
    {
        "id": 1,
        "nome_do_produto": "Product 4",
        "nome_da_empresa": "Company 2",
        "data_de_fabricacao": "2023-06-10",
        "data_de_validade": "2023-06-10",
        "numero_de_serie": "1234",
        "instrucoes_de_armazenamento": "Manusear com cuidado"
    }
]

def test_decorar_relatorio():

    simple_colored_report = ColoredReport(SimpleReport)
    result_simple = simple_colored_report.generate(products)
    # result_simple = ColoredReport(SimpleReport)

    complete_colored_report = ColoredReport(CompleteReport)
    result_complete = complete_colored_report.generate(products)
    # result_complete = ColoredReport(CompleteReport)

    assert '\033[36m' in result_simple

    assert '\033[32m' in result_simple

    assert '\033[31m' in result_simple

    assert '\033[36m' in result_complete

    assert '\033[32m' in result_complete

    assert '\033[31m' in result_complete
