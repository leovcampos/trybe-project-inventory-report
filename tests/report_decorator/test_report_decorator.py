from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    products = [
        {
            "id": 1,
            "nome": "Product 1",
            "data_de_validade": "10/06/1996",
            "data_de_fabricacao": "10/06/1998",
            "nome_da_empresa": "Company 1",
        },
        {
            "id": 2,
            "nome": "Product 2",
            "data_de_validade": "10/06/2020",
            "data_de_fabricacao": "10/06/2023",
            "nome_da_empresa": "Company 2",
        },
        {
            "id": 3,
            "nome": "Product 3",
            "data_de_validade": "10/06/1999",
            "data_de_fabricacao": "10/06/2000",
            "nome_da_empresa": "Company 1",
        },
        {
            "id": 4,
            "nome": "Product 4",
            "data_de_validade": "10/06/1995",
            "data_de_fabricacao": "10/06/2001",
            "nome_da_empresa": "Company 2",
        },
    ]
    simple_colored_report = ColoredReport(SimpleReport)
    result_simple = simple_colored_report.generate(products)

    complete_colored_report = ColoredReport(CompleteReport)
    result_complete = complete_colored_report.generate(products)

    assert (
        "\033[32mData de fabricação mais antiga:\033[0m "
        "\033[36m2021-01-01\033[0m"
        in result_simple
    )
    assert (
        "\033[32mData de validade mais próxima:\033[0m "
        "\033[36m2023-06-14\033[0m"
        in result_simple
    )

    assert (
        "\033[32mEmpresa com mais produtos:\033[0m "
        "\033[31mEmpresa B\033[0m" in result_simple
    )

    assert (
        "\033[32mData de fabricação mais antiga:\033[0m "
        "\033[36m2021-01-01\033[0m"
        in result_complete
    )
    assert (
        "\033[32mData de validade mais próxima:\033[0m "
        "\033[36m2023-06-14\033[0m"
        in result_complete
    )

    assert (
        "\033[32mEmpresa com mais produtos:\033[0m "
        "\033[31mEmpresa B\033[0m" in result_complete
    )
