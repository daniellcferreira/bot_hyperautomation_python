from botcity.web import WebBot, Browser, By
from botcity.web.browsers.chrome import default_options
from botcity.core import DesktopBot
import os
import pandas as pd

user_dir = None


entrada = "Você poderia gerar no formato json com o nome 'produtos' os dados de 3 produtos eletronicos \
  contendo as informações: nome, categoria, codigo, identificador, descrição, preço e quantidade?"

def coleta_dados_produtos():
  bot = WebBot()
  bot.headless = False
  bot.browser = Browser.CHROME
  bot.driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "drivers", "chromedriver.exe"))

  options = default_options(headless=bot.headless, user_data_dir=user_dir)
  bot.options = options

  bot.browse("https://flowgpt.com/chat")
  bot.maximize_window()
  bot.wait(20000)

  input_text = bot.find_element(
    selector= "#__next > div.bg-fgMain-1000.scrollbar-hide > div > main > div > div > div.relative.h-full.w-full.flex-1.overflow-hidden.rounded-none.lg\:rounded-lg.bg-fgMain-950 > div > div > div > div.relative.w-full > div > div.flex-1 > div > div.flex-1.md\:py-0 > textarea",
    by=By.CSS_SELECTOR
  )
  input_text.send_keys(entrada)

  botao_enviar = bot.find_element(
    selector= "#__next > div.bg-fgMain-1000.scrollbar-hide > div > main > div > div > div.relative.h-full.w-full.flex-1.overflow-hidden.rounded-none.lg\:rounded-lg.bg-fgMain-950 > div > div > div > div.relative.w-full > div > div.flex-1 > div > div.\!text-fgMain-3f > svg > path:nth-child(1)",
    by=By.CSS_SELECTOR
  )

  botao_enviar.click()
  bot.wait(2000)

  while botao_enviar.get_attribute("disabled") == "true":
    print("Aguardando os dados serem gerados...")
    bot.wait(2000)

  dados = bot.find_element("language-json", By.CLASS_NAME).get_attribute("textContent")
  print(dados)

  dados = pd.read_json(dados)
  df = pd.json_normalize(dados["produtos"])
  print(df)

  df.to_excel("produtos.xlsx", index=False)
  print("Arquivo Excel gerado com sucesso!")

  bot.wait(2000)
  bot.stop_browser()

  return df

def cadastra_produto(data_frame: pd.DataFrame):
  bot = DesktopBot()

  bot.execute(r"Fakturama.exe")

def main():
  dados_produtos = coleta_dados_produtos()
  cadastra_produto(dados_produtos)

if __name__ == "__main__":
  main()