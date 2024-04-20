from funções_montante_e_juros_simples import calcular_juros_simples, calcular_montante


# Testes da função calcularJurosSimples:

def test_1_calcular_juros_simples():
    assert calcular_juros_simples(1000, 2.5, 10) == 250


def test_2_calcular_juros_simples():
    assert calcular_juros_simples(1000, 0.025, 10, porcentagem=False) == 250


# Testes da função calcularMontante:

def test_1_calcular_montante():
    assert calcular_montante(1000, 250) == 1250


def test_2_calcular_montante():
    assert calcular_montante(2000, 500) == 2500
