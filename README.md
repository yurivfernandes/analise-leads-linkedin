# 📊 Análise de Leads do LinkedIn

    Este projeto realiza uma clusterização de leads do LinkedIn, utilizando dados fictícios para simular leads e organizá-los em clusters com base em várias dimensões, como cargo, setor, localização e tamanho da empresa.

    ## 🛠️ Pré-requisitos

    - Certifique-se de que o **Python 3** esteja instalado em sua máquina. Verifique a instalação com:
      ```bash
      python3 --version
      ```

    ## 🚀 Instalação

    1. **Crie um ambiente virtual** para isolar as dependências do projeto:
       ```bash
       python3 -m venv venv
       ```

    2. **Ative o ambiente virtual**:
       - No macOS/Linux:
         ```bash
         source venv/bin/activate
         ```
       - No Windows:
         ```bash
         .\venv\Scripts\activate
         ```

    3. **Instale as dependências** listadas no arquivo `requirements.txt`:
       ```bash
       pip install -r requirements.txt
       ```

    4. **Gere as migrações** para preparar o banco de dados:
       ```bash
       python3 src/manage.py makemigrations
       ```

    5. **Realize as migrações** para aplicar as alterações no banco de dados:
       ```bash
       python3 src/manage.py migrate
       ```

    ## ⚙️ Execução

    Para executar o processo completo de geração de leads, popular dimensões e preencher clusters, utilize o comando principal:

    ```bash
    python3 src/manage.py run_all_commands [quantidade_de_registros]
    ```

    - **Com quantidade de registros**: Se você fornecer a quantidade de registros, o comando irá gerar o número especificado de leads.
      ```bash
      python3 src/manage.py run_all_commands 500
      ```

    - **Sem quantidade de registros**: Se você não fornecer a quantidade, o comando irá gerar **1.000 leads** por padrão.
      ```bash
      python3 src/manage.py run_all_commands
      ```

    Certifique-se de executar o comando principal para garantir que todos os dados sejam processados adequadamente.

    ---

    **Nota**: Mantenha o ambiente virtual ativado durante todo o processo para garantir que as dependências corretas sejam utilizadas.
