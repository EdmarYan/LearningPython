import os  # Manipulação de arquivos e diretórios
import requests  # Para realizar requisições HTTP
from bs4 import BeautifulSoup  # Para analisar HTML
from urllib.parse import urljoin, urlparse  # Manipulação de URLs
import tkinter as tk  # Interface gráfica
from tkinter import messagebox  # Exibir mensagens para o usuário

def obter_caminho_area_trabalho():
    # Função para obter o caminho da área de trabalho do usuário
    return os.path.join(os.path.expanduser("~"), "Desktop")

def extrair_nome_site(url_site):
    # Função para extrair o nome do site entre "www" e ".com"
    partes_url = urlparse(url_site).netloc.split('.')
    for parte in partes_url:
        if parte != 'www':
            return parte  # Retorna o nome do site (por exemplo, 'exemplo' de www.exemplo.com)

def baixar_arquivo(url_arquivo, pasta_destino):
    # Função para baixar um arquivo dado uma URL e a pasta de destino
    nome_arquivo = os.path.basename(urlparse(url_arquivo).path)  # Extrai o nome do arquivo da URL
    caminho_arquivo = os.path.join(pasta_destino, nome_arquivo)  # Define o caminho completo para salvar o arquivo
    resposta = requests.get(url_arquivo)  # Envia a requisição GET

    if resposta.status_code == 200:  # Verifica se a requisição foi bem-sucedida
        with open(caminho_arquivo, 'wb') as arquivo:  # Abre o arquivo para escrita binária
            arquivo.write(resposta.content)  # Escreve o conteúdo no arquivo
        print(f"Arquivo baixado: {nome_arquivo}")
    else:
        print(f"Erro ao baixar {url_arquivo}: Status {resposta.status_code}")

def salvar_pagina(url_site):
    # Função para salvar a página web e seus recursos
    caminho_area_trabalho = obter_caminho_area_trabalho()  # Obtém o caminho da área de trabalho do usuário
    nome_site = extrair_nome_site(url_site)  # Extrai o nome do site a partir da URL
    pasta_site_clonado = os.path.join(caminho_area_trabalho, nome_site)  # Cria uma pasta com o nome do site

    resposta = requests.get(url_site)  # Faz a requisição GET para a página
    
    if resposta.status_code == 200:  # Verifica se a requisição foi bem-sucedida
        conteudo_pagina = resposta.text  # Obtém o conteúdo da página como texto
        sopa_html = BeautifulSoup(conteudo_pagina, 'html.parser')  # Analisa o conteúdo HTML da página
        
        if not os.path.exists(pasta_site_clonado):  # Verifica se a pasta não existe
            os.makedirs(pasta_site_clonado)  # Cria a pasta para salvar o site clonado
        
        caminho_html = os.path.join(pasta_site_clonado, 'index.html')  # Define o caminho para o arquivo HTML
        with open(caminho_html, 'w', encoding='utf-8') as arquivo_html:  # Abre o arquivo HTML para escrita
            arquivo_html.write(sopa_html.prettify())  # Escreve o conteúdo HTML no arquivo
        messagebox.showinfo("Sucesso", f'Página HTML salva em: {caminho_html}')  # Mensagem de sucesso

        # Cria subpastas para salvar os arquivos CSS, JavaScript e Imagens
        pasta_css = os.path.join(pasta_site_clonado, 'css')
        pasta_js = os.path.join(pasta_site_clonado, 'js')
        pasta_imagens = os.path.join(pasta_site_clonado, 'imagens')
        
        os.makedirs(pasta_css, exist_ok=True)  # Cria a pasta CSS
        os.makedirs(pasta_js, exist_ok=True)  # Cria a pasta JS
        os.makedirs(pasta_imagens, exist_ok=True)  # Cria a pasta de Imagens
        
        # Baixa os arquivos CSS
        for link in sopa_html.find_all('link', rel="stylesheet"):
            url_css = urljoin(url_site, link.get('href'))  # Monta a URL completa do CSS
            baixar_arquivo(url_css, pasta_css)  # Baixa o arquivo CSS
        
        # Baixa os arquivos JavaScript
        for script in sopa_html.find_all('script', src=True):
            url_js = urljoin(url_site, script.get('src'))  # Monta a URL completa do JS
            baixar_arquivo(url_js, pasta_js)  # Baixa o arquivo JavaScript
        
        # Baixa as imagens
        for img in sopa_html.find_all('img', src=True):
            url_imagem = urljoin(url_site, img.get('src'))  # Monta a URL completa da imagem
            baixar_arquivo(url_imagem, pasta_imagens)  # Baixa a imagem
        
    else:
        messagebox.showerror("Erro", f"Erro ao acessar {url_site}: Status {resposta.status_code}")  # Mensagem de erro

def iniciar_clonagem():
    # Função para iniciar o processo de clonagem
    url = entrada_url.get()  # Obtém a URL digitada pelo usuário
    if not url:  # Verifica se o campo da URL está vazio
        messagebox.showwarning("Aviso", "Por favor, insira uma URL válida.")  # Mensagem de aviso
        return
    
    salvar_pagina(url)  # Chama a função para salvar a página

# Interface Gráfica (GUI)
janela = tk.Tk()  # Cria a janela principal da GUI
janela.title("Clonador de Sites")  # Define o título da janela
janela.geometry("400x150")  # Define o tamanho da janela

# Rótulo para a URL do site
rotulo_url = tk.Label(janela, text="Digite a URL do site:")
rotulo_url.pack(pady=5)

# Entrada de texto para a URL
entrada_url = tk.Entry(janela, width=50)
entrada_url.pack(pady=5)

# Botão para iniciar a clonagem
botao_clonar = tk.Button(janela, text="Clonar Site", command=iniciar_clonagem)
botao_clonar.pack(pady=20)

# Inicia o loop da interface gráfica
janela.mainloop()
