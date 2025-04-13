from botcity.core import DesktopBot

def cadastra_produto(df):
  """
  Usa o BotCity Desktop para automatizar o cadastro de produtos no sistema Fakturama.
  Preenche: nome, descrição, preço, categoria, código do produto e estoque.
  """
  bot = DesktopBot()

  for idx, row in df.iterrows():
    # Captura os dados do DataFrame
    nome = row["nome"]
    descricao = row["descricao"]
    preco = row["preco"]
    categoria = row["categoria"]
    codigo = row["codigo"]
    estoque = row["estoque"]

    # Clicar no botão de adicionar novo produto
    bot.click(100, 200)  # Coordenada do botão "Novo Produto" (ajuste conforme necessário)
    bot.wait(1000)

    # Preencher os campos
    bot.type_keys(nome)  # Nome
    bot.tab()

    bot.type_keys(descricao)  # Descrição
    bot.tab()

    bot.type_keys(str(preco))  # Preço
    bot.tab()

    bot.type_keys(categoria)  # Categoria
    bot.tab()

    bot.type_keys(codigo)  # Código do Produto
    bot.tab()

    bot.type_keys(str(estoque))  # Estoque
    bot.tab()

    # Salvar o produto
    bot.key_press("ctrl", "s")
    bot.wait(1500)  # Esperar para garantir o salvamento antes de seguir

  print("Produtos cadastrados com sucesso!")