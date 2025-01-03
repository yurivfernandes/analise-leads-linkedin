<div align="center">

  # 📊 Análise de Leads do LinkedIn

  [![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://docs.python.org/3/)
  [![Django](https://img.shields.io/badge/Django-3.2-green?style=for-the-badge&logo=django)](https://docs.djangoproject.com/en/3.2/)
  [![Faker](https://img.shields.io/badge/Faker-9.8.1-yellow?style=for-the-badge)](https://faker.readthedocs.io/en/master/)
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/yurianalistabi/)
</div>

## 📑 Índice
- [Sobre o Projeto](#-sobre-o-projeto)
- [Pré-requisitos](#️-pré-requisitos)
- [Instalação](#-instalação)
- [Como Usar](#-como-usar)
- [Contribuição](#-contribuição)

## 🎯 Sobre o Projeto
Uma poderosa ferramenta de análise que realiza clusterização de leads do LinkedIn, utilizando dados para categorizar contatos em grupos estratégicos baseados em:

- 👔 Cargo
- 🏢 Setor
- 📍 Localização
- 📊 Tamanho da empresa

## 🛠️ Pré-requisitos

<img src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png" alt="Python" width="40" align="left" />

**Python 3** é necessário para executar o projeto. Verifique sua instalação:
```bash
python3 --version
```

## 🚀 Instalação

### 1. Prepare o Ambiente Virtual
```bash
# Criar ambiente virtual
python3 -m venv venv

# Ativar ambiente (Mac/Linux)
source venv/bin/activate

# Ativar ambiente (Windows)
.\venv\Scripts\activate
```

### 2. Configure o Projeto
```bash
# Instalar dependências
pip install -r requirements.txt

# Preparar banco de dados
python3 src/manage.py makemigrations
python3 src/manage.py migrate
```

## 💻 Como Usar

Execute o comando principal para iniciar a análise:

```bash
# Gerar 1000 leads (padrão)
python3 src/manage.py run_all_commands

# Ou especifique a quantidade
python3 src/manage.py run_all_commands 500
```

## 📈 Resultados

A ferramenta irá gerar:
- 📊 Clusters de leads organizados
- 📑 Relatórios detalhados
- 🎯 Insights estratégicos

## 🤝 Contribuição

Contribuições são sempre bem-vindas! Veja como você pode ajudar:

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

---

<div align="center">
  <p>Desenvolvido por <a href="https://www.linkedin.com/in/yurianalistabi/">Yuri Fernandes</a></p>
  
  [![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/yurianalistabi/)
</div>
