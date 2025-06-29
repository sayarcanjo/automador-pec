# Robô Automatizador de Tarefas - e-SUS PEC

## 🎯 Objetivo do Projeto

Este projeto nasceu da necessidade de otimizar o tempo na rotina de trabalho de Agentes Comunitários de Saúde, onde uma das principais responsabilidades é manter os cadastros atualizados na plataforma e-SUS PEC, no entanto, esse processo de trabalho envolve tarefqas repetitivas em diferentes abas do sistema que consomem muito tempo e poderiam ser feitas de forma automatizada, já que utiliza as mesmas informações. 
  
## 🛠️ Tecnologias Utilizadas

* **Linguagem:** Python
* **Automação Web:** Selenium
* **Ambiente:** Docker (para containerização)
* **CI/CD:** GitHub Actions (planejado para futuras implementações)

## 🚀 Como Executar (Usando Docker)
Recomenda-se executar este robô através do Docker, que garante que o ambiente seja idêntico em qualquer máquina.

Pré-requisitos:
Git instalado.

Docker Desktop instalado e em execução.

Passo a Passo:
1. Clone o Repositório
Abra o seu terminal e execute o seguinte comando para descarregar os ficheiros do projeto:

git clone https://github.com/sayarcanjo/automador-pec.git

2. Entre na Pasta do Projeto

cd automador-pec

3. Construa a Imagem Docker
Este comando vai ler o Dockerfile e montar o ambiente completo para o robô.

docker build -t automador-pec .

4. Execute o Robô
Agora, execute o container. O comando -it torna o terminal interativo para que você possa digitar os dados que o robô pede. Substitua "seu_cpf" e "sua_senha" pelas suas credenciais reais.

docker run -it -e PEC_USUARIO="seu_cpf" -e PEC_SENHA="sua_senha" automador-pec

O robô irá iniciar no seu terminal. Siga as instruções e forneça os dados do cidadão que ele pedir.

## 📈 Progresso Atual

O robô, na sua versão atual, já é capaz de:
1.  Fazer o login de forma segura no sistema.
2.  Navegar pela estrutura de menus (Módulos -> CDS).
3.  Atingir o ecrã de Cadastro Individual.

## ⚠️ Status Atual: Em Pausa

O desenvolvimento encontra-se temporariamente em pausa. O sistema externo do e-SUS PEC, do qual este robô depende, tem apresentado instabilidade, o que impede a continuação da depuração dos seletores para as etapas de preenchimento de formulário. O projeto será retomado assim que o serviço for restabelecido.



---

