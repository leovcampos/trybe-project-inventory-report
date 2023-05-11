from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        '1',
        'Product',
        'Company',
        '10/06/2023',
        '10/06/2024',
        '1234',
        'em estado congelado')

    assert str(product) == """O produto Product fabricado em 10/06/2023 por
    Company com validade até 10/06/2024
    precisa ser armazenado em estado congelado."""
