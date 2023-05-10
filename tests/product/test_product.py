from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        1,
        'Produto',
        'Empresa',
        '10/06/2023',
        '10/06/2024',
        '1234',
        'Cuidado, frágil'
    )
    assert product.id == 1
    assert product.nome_do_produto == "Produto"
    assert product.nome_da_empresa == "Empresa"
    assert product.data_de_fabricacao == "10/06/2023"
    assert product.data_de_validade == "10/06/2024"
    assert product.numero_de_serie == '1234'
    assert product.instrucoes_de_armazenamento == "Cuidado, frágil"
