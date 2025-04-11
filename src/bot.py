from botcity.web import WebBot, Browser, By
from botcity.web.browsers.chrome import default_options
import os

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


  input()

  bot.stop_browser()

def main():
  coleta_dados_produtos()
  print("Dados coletados com sucesso!")

if __name__ == "__main__":
  main()