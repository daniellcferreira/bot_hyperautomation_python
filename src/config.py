import os

# Entrada padrão usada para coleta
ENTRADA_PADRAO = "Você poderia gerar no formato json com o nome 'produtos' contendo nome, descrição e preço?"

# Caminho absoluto do chromedriver
CHROMEDRIVER_PATH = os.path.abspath(
  os.path.join(os.path.dirname(__file__), "..", "drivers", "chromedriver.exe")
)