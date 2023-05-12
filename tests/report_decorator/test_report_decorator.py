from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

RED, GREEN, BLUE = ("\033[31m", "\033[32m", '\033[36m')

mock_products_list = [
    {
        "id": 1,
        "nome_do_produto": "Product_01",
        "nome_da_empresa": "Company_01",
        "data_de_fabricacao": "10/06/1996",
        "data_de_validade": "10/06/2023",
        "numero_de_serie": "1234",
        "instrucoes_de_armazenamento": "Conservar em local seco"
    },
    {
        "id": 2,
        "nome_do_produto": "Product_02",
        "nome_da_empresa": "Company_02",
        "data_de_fabricacao": "10/06/1995",
        "data_de_validade": "10/06/2022",
        "numero_de_serie": "1234",
        "instrucoes_de_armazenamento": "Conservar em local molhado"
    }
]


def test_decorar_relatorio():
    test_simple_colored_report = ColoredReport(SimpleReport)
    test_complete_colored_report = ColoredReport(CompleteReport)

    assert {BLUE} in test_simple_colored_report.generate(
        mock_products_list
    )
    assert {GREEN} in test_simple_colored_report.generate(
        mock_products_list
    )
    assert {RED} in test_simple_colored_report.generate(
        mock_products_list
    )

    assert {BLUE} in test_complete_colored_report.generate(
        mock_products_list
    )
    assert {GREEN} in test_complete_colored_report.generate(
        mock_products_list
    )
    assert {RED} in test_complete_colored_report.generate(
        mock_products_list
    )
