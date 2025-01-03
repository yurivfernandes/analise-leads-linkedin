# Análise de Leads do LinkedIn

    Este projeto realiza uma clusterização de leads do LinkedIn. Ele utiliza dados fictícios para simular leads e organiza esses dados em clusters com base em várias dimensões, como cargo, setor, localização e tamanho da empresa.

    ## Instalação

    1. Instale as dependências do projeto listadas no arquivo `requirements.txt`:
       ```bash
       pip install -r requirements.txt
       ```

    2. Realize as migrações do banco de dados:
       ```bash
       python3 src/manage.py migrate
       ```

    ## Execução

    O projeto possui três comandos principais que devem ser executados na seguinte ordem:

    1. **Gerar Leads**: Este comando gera dados fictícios de leads. É necessário especificar a quantidade de registros a serem criados.
       ```bash
       python3 src/manage.py 1_gerar_leads <quantidade_de_registros>
       ```

    2. **Popular Dimensões**: Este comando preenche as tabelas de dimensão com base nos dados gerados.
       ```bash
       python3 src/manage.py 2_popular_dimensoes
       ```

    3. **Preencher Cluster**: Este comando associa os IDs das dimensões aos leads na tabela de clusters.
       ```bash
       python3 src/manage.py 3_preencher_cluster
       ```

    Certifique-se de executar os comandos na ordem correta para garantir que os dados sejam processados adequadamente.
