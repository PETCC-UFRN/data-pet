# data-pet
Projeto de Ciência de Dados e Machine Learning do PET
## Instalação para os petianos
### Configuração do Git
Antes crie a adicione uma chave SSH ao GitHub. [Link da documentação do Github](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys)
```bash
# Primeiro configure o repositório git
mkdir data-pet
cd data-pet
git init
git remote add origin git@github.com:PETCC-UFRN/data-pet.git
git config user.name "seu_username"
git config user.email "seu_email_do_github@dominio.com"
git branch -M main
git pull origin main
```
### Configuração do UV
Os comandos abaixo só funcionam se você instalou o uv de forma prévia. [Link da documentação do uv](https://docs.astral.sh/uv/getting-started/installation/)
```bash
# Este comando cria um ambiente virtual com python na versão definida com as bibliotecas necessárias.
uv sync
```