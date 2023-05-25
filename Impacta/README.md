# Exercício de Integração de Serviços em Python

Este exercício consiste em criar dois serviços em Python que se integram usando a biblioteca Flask. O primeiro serviço, chamado "alunos.py", implementa rotas para os métodos GET, POST e DELETE. O segundo serviço, chamado "call-alunos.py", utiliza as rotas do primeiro serviço para cada respectivo método.

## Serviço 1 - API de Teste (`alunos.py`)

O primeiro serviço é implementado no arquivo `alunos.py` e possui as seguintes rotas:

- `GET /alunoss`: Retorna os registros da tabela `TB_ALUNOSS` do banco de dados.
- `POST /alunoss`: Adiciona um novo aluno à tabela `TB_ALUNOSS` no banco de dados.
- `DELETE /alunoss`: Deleta um aluno da tabela `TB_ALUNOSS` no banco de dados.

### Configuração do Banco de Dados

Antes de executar o serviço, é necessário criar a tabela `TB_ALUNOSS` no banco de dados. Utilize o seguinte comando SQL:

```sql
CREATE TABLE TB_ALUNOSS (
  ID INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
  ALUNOSS VARCHAR(30) NOT NULL UNIQUE
);

Além disso, certifique-se de configurar corretamente as informações de conexão com o banco de dados no arquivo `alunos.py`. Altere os parâmetros `host`, `database`, `user` e `password` de acordo com a sua configuração.

#### Como executar o serviço 1

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo alunos.py está localizado.
3. Execute o seguinte comando para iniciar o serviço: `python alunos.py`
4. O serviço estará disponível no seguinte endereço: [http://localhost:5000](http://localhost:5000).

## Serviço 2 - Integração com o Serviço 1 (`call-alunos.py`)

O segundo serviço é implementado no arquivo `call-alunos.py` e consome as rotas do primeiro serviço para cada respectivo método.

### Pré-requisitos

Certifique-se de ter instalado as seguintes dependências:

- Python 3.x
- Flask

### Como executar o serviço 2

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde o arquivo `call-alunos.py` está localizado.
3. Execute o seguinte comando para iniciar o serviço: `python call-alunos.py`
4. O serviço estará disponível no seguinte endereço: [http://localhost:5001](http://localhost:5001).

## Testando as Rotas

Após iniciar ambos os serviços, você pode testar as rotas do serviço 2 utilizando ferramentas como cURL, Postman ou navegadores.

- **GET /**: Retorna os registros da tabela `TB_ALUNOSS` do serviço 1.
- **POST /**: Adiciona um novo aluno ao serviço 1.
- **DELETE /**: Deleta um aluno do serviço 1.

Certifique-se de fornecer os parâmetros corretos na URL para cada rota, como `cust` e `id` quando necessário.

## Feito por:
Aluno: Amália Emilia da Rocha Pitta RA: 2200519
Aluno: Beatriz Borges Cantero RA: 2202122
