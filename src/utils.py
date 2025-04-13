# Utilitário para tratar os preços

def trata_preco(preco):
  """
  Recebe o preço como string, remove o símbolo e converte para float.
  Exemplo: 'R$ 1.234,56' -> 1234.56
  """
  preco = preco.replace("R$", "").replace(".", "").replace(",", ".")
  return float(preco.strip())
