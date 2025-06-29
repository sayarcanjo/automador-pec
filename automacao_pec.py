# --- 1. FERRAMENTAS DO ROBÔ ---
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from datetime import datetime

# --- 2. CONFIGURAÇÕES E DADOS ---
USUARIO = os.environ.get('PEC_USUARIO')
SENHA = os.environ.get('PEC_SENHA')
URL_LOGIN_PEC = "https://esus.iguatu.ce.gov.br/"

if not USUARIO or not SENHA:
    print("ERRO: Credenciais não definidas no terminal!")
    exit()

print("--- Robô Atualizador de Cadastro do PEC (Completo) ---")
nome_completo_busca = input("Digite o NOME COMPLETO do cidadão para comparar: ")
data_nascimento_busca = input("Digite a DATA DE NASCIMENTO (DD/MM/AAAA) para a busca: ")
nova_microarea = input("Digite a NOVA micro área: ")
novo_cep = input("Digite o NOVO CEP: ")
novo_numero_casa = input("Digite o NOVO número da casa: ")
print("\nIniciando automação...")

# --- 3. LÓGICA DE AUTOMAÇÃO ---
try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    wait = WebDriverWait(driver, 15)
    driver.get(URL_LOGIN_PEC)

    # ========================================================================
    # ETAPA 0: ACEITAR COOKIES
    # ========================================================================
    print("ETAPA 0: Procurando pelo banner de cookies...")
    try:
        cookie_wait = WebDriverWait(driver, 5)
        # O robõ procura por um elemento com o texto "Aceitar todos".
        botao_cookies = cookie_wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Aceitar todos')]")))
        botao_cookies.click()
        print("Banner de cookies aceite.")
    except Exception:
        print("Nenhum banner de cookies encontrado. Continuando...")
    
    # ========================================================================
    # ETAPA A: FAZER LOGIN
    # ========================================================================
    print("ETAPA A: Fazendo login...")
    
    print("--> Tentando encontrar o campo 'Usuário' (username)...")
    wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(USUARIO)
    
    print("--> Tentando encontrar o campo 'Senha' (password)...")
    wait.until(EC.presence_of_element_located((By.NAME, "password"))).send_keys(SENHA)
    
    print("--> Tentando encontrar o botão 'Entrar'...")
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    
    print("Login realizado com sucesso!")
    time.sleep(5)

    # ========================================================================
    # PARTE 1: ATUALIZAÇÃO NO CADASTRO INDIVIDUAL (CDS)
    # ========================================================================
    print("\n--- INICIANDO PARTE 1: ATUALIZAÇÃO DO CADASTRO INDIVIDUAL (CDS) ---")

    # ETAPA B: NAVEGAR PARA O CADASTRO INDIVIDUAL
    print("ETAPA B: Navegando para Módulos -> CDS -> Cadastro Individual...")
    
    print("--> Tentando clicar no menu 'Módulos'...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Módulos')]"))).click()
    time.sleep(1) # Pequena pausa para o próximo menu carregar
    
    print("--> Tentando clicar no menu 'CDS'...")
    wait.until(EC.element_to_be_clickable((By.XPATH, "//span[span/span[normalize-space()='CDS']]"))).click()
    
    ###Adicionando uma pausa extra para garantir que o submenu está pronto.
    time.sleep(1) 

    # print("--> Tentando clicar no submenu 'Cadastro Individual'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    # time.sleep(3)

    # # ETAPA C: FILTRAR POR DATA DE NASCIMENTO
    # print("ETAPA C: Filtrando por data de nascimento...")
    
    # print("--> Tentando clicar na caixa de seleção inicial...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "(..."))).click()
    # time.sleep(1)

    # print("--> Tentando clicar no botão 'Filtros'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    # print("--> Tentando encontrar o campo 'dataNascimento'...")
    # wait.until(EC.presence_of_element_located((By.NAME, "..."))).send_keys(data_nascimento_busca)
    # print("--> Tentando clicar no botão 'Pesquisar'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    # time.sleep(3)

    # # ETAPA D: ENCONTRAR E ABRIR O CADASTRO
    # print("ETAPA D: Procurando o paciente na lista...")
    # print("--> Tentando clicar no primeiro botão 'Atualizar' da lista...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "(..."))).click()
    # time.sleep(3)

    # # ETAPA E: ATUALIZAR DATA E MICROÁREA
    # print("ETAPA E: Atualizando data e microárea...")
    # data_hoje = datetime.now().strftime('%d/%m/%Y')
    # print("--> Tentando encontrar o campo 'dataAtendimento'...")
    # wait.until(EC.presence_of_element_located((By.NAME, "..."))).send_keys(data_hoje)
    # print("--> Tentando encontrar o campo 'microarea'...")
    # campo_ma_cds = wait.until(EC.presence_of_element_located((By.NAME, "...")))
    # campo_ma_cds.clear()
    # campo_ma_cds.send_keys(nova_microarea)
    
    # # ETAPA F: SALVAR CADASTRO INDIVIDUAL
    # print("ETAPA F: Salvando o Cadastro Individual...")
    # print("--> Tentando clicar no botão 'Salvar'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "...]"))).click()
    # print("Cadastro Individual salvo com sucesso!")
    # time.sleep(5)

    # # ========================================================================
    # # PARTE 2: ATUALIZAÇÃO NO CADASTRO DO CIDADÃO
    # # ========================================================================
    # print("\n--- INICIANDO PARTE 2: ATUALIZAÇÃO DO CADASTRO DO CIDADÃO ---")
    
    # # ETAPA G: NAVEGAR PARA A ABA CIDADÃO
    # print("ETAPA G: Navegando para a aba Cidadão...")
    # print("--> Tentando clicar no menu 'Cidadão'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    # time.sleep(3)

    # # ETAPA H: PESQUISAR CIDADÃO NOVAMENTE
    # print("ETAPA H: Pesquisando cidadão por data de nascimento...")
    # print("--> Tentando encontrar o campo de busca 'dataNascimento'...")
    # wait.until(EC.presence_of_element_located((By.NAME, "..."))).send_keys(data_nascimento_busca)
    # print("--> Tentando clicar no botão 'Buscar cidadão'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    # time.sleep(3)
    
    # # ETAPA I: ABRIR CADASTRO DO CIDADÃO
    # print("ETAPA I: Encontrando e abrindo o cadastro...")
    # print("--> Tentando clicar no botão 'Atualizar cadastro'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    # time.sleep(3)

    # # ETAPA J: ATUALIZAR ENDEREÇO
    # print("ETAPA J: Atualizando CEP e número...")
    # print("--> Tentando encontrar o campo 'endereco.cep'...")
    # campo_cep = wait.until(EC.presence_of_element_located((By.NAME, "...")))
    # campo_cep.clear()
    # campo_cep.send_keys(novo_cep)
    # print("--> Tentando clicar no botão 'Pesquisar' do CEP...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    # time.sleep(2)
    # print("--> Tentando encontrar o campo 'endereco.numero'...")
    # campo_num = wait.until(EC.presence_of_element_located((By.NAME, "...")))
    # campo_num.clear()
    # campo_num.send_keys(novo_numero_casa)
    
    # # ETAPA K: ATUALIZAR MICROÁREA NOVAMENTE
    # print("ETAPA K: Atualizando a microárea no cadastro do cidadão...")
    # print("--> Tentando encontrar o campo 'endereco.microArea'...")
    # campo_ma_cid = wait.until(EC.presence_of_element_located((By.NAME, "...")))
    # campo_ma_cid.clear()
    # campo_ma_cid.send_keys(nova_microarea)
    
    # # ETAPA L: SALVAR CADASTRO DO CIDADÃO
    # print("ETAPA L: Salvando o Cadastro do Cidadão...")
    # print("--> Tentando clicar no botão 'Salvar'...")
    # wait.until(EC.element_to_be_clickable((By.XPATH, "..."))).click()
    #print("Cadastro do Cidadão salvo com sucesso!")
    
    #print("\n[SUCESSO] AUTOMAÇÃO CONCLUÍDA!")
    
except Exception as e:
    print(f"\n[ERRO] Falha na automação.")
    print(f"O robô parou porque não conseguiu encontrar ou interagir com o último elemento que procurava.")
    print(f"Detalhe técnico do erro: {e}")

finally:
    input("Pressione Enter para fechar o navegador...")
    if 'driver' in locals():
        driver.quit()



