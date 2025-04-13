from .config import ENTRADA_PADRAO, CHROMEDRIVER_PATH
from .web_scraper import coleta_dados_produtos
from .desktop_automation import cadastra_produto

def main():
  # Coleta os dados dos produtos
  df = coleta_dados_produtos(ENTRADA_PADRAO, CHROMEDRIVER_PATH)

  # Cadastra os produtos no sistema Fakturama
  cadastra_produto(df)

if __name__ == "__main__":
  main()
