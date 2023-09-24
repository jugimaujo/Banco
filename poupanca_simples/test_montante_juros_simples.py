from montante_juros_simples import juros_simples, montante


# Testes da função juros_simples:

def test_1_juros_simples():
    assert juros_simples(1000, 2.5, 10) == 250


def test_2_juros_simples():
    assert juros_simples(1000, 0.025, 10, porcentagem=False) == 250


# Testes da função montante:

def test_1_montante():
    assert montante(1000, 250) == 1250


def test_2_montante():
    assert montante(2000, 500) == 2500
