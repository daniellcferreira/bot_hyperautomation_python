from botcity.web import WebBot, Browser, By
import pandas as pd
from .utils import trata_preco

def coleta_dados_produtos(entrada, driver_path):
  """
  Usa o BotCity Web para coletar os dados de produtos de um site de IA.
  Retorna um DataFrame com nome, descrição e preço.
  """
  bot = WebBot()
  bot.headless = False
  bot.browser = Browser.CHROME
  bot.driver_path = driver_path

  bot.browse("https://chat.openai.com/")

  # Login manualmente se necessário
  input("Pressione ENTER após realizar o login manual no site...")

  # Envia o prompt para o ChatGPT
  bot.find_element("prompt-textarea", By.ID, True).send_keys(entrada)
  bot.find_element('button[data-testid="send-button"]', By.CSS_SELECTOR).click()

  bot.wait(8000)  # Aguarda a resposta ser gerada

  # Copia a resposta
  bot.find_element('button[data-testid="clipboard-button"]', By.CSS_SELECTOR).click()

  # Lê o conteúdo da área de transferência
  import pyperclip
  texto = pyperclip.paste()

  # Processa o JSON retornado
  import json
  produtos = json.loads(texto)["produtos"]

  # Monta o DataFrame
  df = pd.DataFrame(produtos)
  df["preco"] = df["preco"].apply(trata_preco)

  bot.stop_browser()
  return df
