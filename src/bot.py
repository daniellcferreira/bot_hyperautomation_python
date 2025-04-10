from botcity.web import WebBot, Browser, By
from botcity.web.browsers.edge import default_options
import os

user_dir = None

entrada = "Você poderia gerar no formato json com o nome 'produtos' os dados de 3 produtos eletronicos \
  contendo as informações: nome, categoria, codigo, identificador, descrição, preço e quantidade?"

def coleta_dados_produtos():
  bot = WebBot()
  bot.headless = False
  bot.browser = Browser.EDGE
  bot.driver_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "drivers", "msedgedriver.exe"))

  options = default_options(headless=bot.headless, user_data_dir=user_dir)
  bot.options = options

  bot.browse("https://flowgpt.com/chat")
  bot.maximize_window()
  bot.wait(20000)

  bot.stop_browser()

def main():
  coleta_dados_produtos()
  print("Dados coletados com sucesso!")

if __name__ == "__main__":
  main()