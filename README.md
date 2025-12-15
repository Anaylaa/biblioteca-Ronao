 # Sistema de Biblioteca — Empréstimo de Livros
### Domain-Driven Design (DDD Leve)
## Visão Geral

Este projeto implementa um Sistema de Gerenciamento de Empréstimos de Livros, desenvolvido em Python (≥ 3.13), utilizando os princípios de Domain-Driven Design (DDD Leve).

O sistema controla livros, usuários e empréstimos, garantindo consistência, validações e regras de negócio puras, com dados mantidos exclusivamente em memória.

O foco principal do trabalho é a arquitetura, a separação de responsabilidades e a qualidade dos testes, conforme a especificação da disciplina.

        ✅ Funcionalidades do Sistema

        📖 Cadastro de livros

        👤 Cadastro de usuários

        🔄 Empréstimos e devoluções

        🤝 Regras de Negócio Respeitadas

        🚫 Um livro não pode ser emprestado se já estiver emprestado

        🔢 Um usuário não pode ultrapassar o limite de empréstimos simultâneos

        📅 Datas de empréstimo e devolução devem ser válidas

        🔁 Controle completo do ciclo de vida do empréstimo

🎯 Objetivo do Trabalho

1. Aplicar os conceitos de DDD Leve na prática

2. Separar claramente as camadas do sistema:

        🧠 Domínio

        ⚙️ Aplicação

        🏗️ Infraestrutura

        🖥️ Interface do Usuário

3. Desenvolver um sistema funcional com dados em memória

4. Criar uma suíte completa de testes:

        ✅ Testes Unitários

        🔗 Testes de Integração

        🧪 Testes End-to-End (E2E)

## Regras de Negócio do Sistema de Biblioteca
1️⃣ Regras Gerais

- Todas as regras estão exclusivamente no Domínio

Nenhuma regra acessa:

input

print

arquivos

banco de dados

Violações geram exceções de domínio, com mensagens em PT-BR

2️⃣ Regras de Livro
    
1.  Cadastro

Um livro deve possuir:

        ID único

        Título

        Autor

2. Regras:

        ❌ Não é permitido cadastrar livros com IDs duplicados

        ✅ Todo livro inicia como disponível

📕 Estado do Livro

Um livro pode estar em apenas um estado:

1. Disponível

2. Emprestado

Regras:

- Livro emprestado não pode ser emprestado novamente

- O livro só volta a ficar disponível após devolução válida

3️⃣ Regras de Usuário

👤 Cadastro

Um usuário deve possuir:

        ID único

        Nome

Regras:

- Não é permitido cadastrar usuários com IDs duplicados

- Limite de Empréstimos:

        - Um usuário pode ter no máximo 7 empréstimos ativos simultâneos

- Ao atingir o limite, novos empréstimos são bloqueados

4️⃣ Regras de Empréstimo

🔹 Criação

Um empréstimo deve conter:

        Livro

        Usuário

        Data do empréstimo

        Data prevista de devolução

Regras:

- A data prevista de devolução deve ser posterior à data do empréstimo

Não é permitido criar empréstimo para:

- Livro inexistente

- Usuário inexistente

O empréstimo só ocorre se:

- O livro estiver disponível

- O usuário não tiver atingido o limite

- Usuário não tiver com devolução atrasada

🔒 Exclusividade

- Um livro pode ter apenas um empréstimo ativo

- Empréstimo ativo é aquele sem data de devolução real

5️⃣ Regras de Devolução

A devolução deve registrar:

- Data real de devolução

Regras:

- A data de devolução real não pode ser anterior à data do empréstimo

Após a devolução:

- O empréstimo deixa de ser ativo

- O livro volta a ficar disponível

- A quantidade de cópias daquele livro aumenta +1

6️⃣ Regras de Consistência

❌ Não é permitido:

        Devolver livro não emprestado

        Devolver o mesmo empréstimo duas vezes

✅ Consistência obrigatória:

        Livro emprestado ⇒ existe empréstimo ativo

        Livro disponível ⇒ não existe empréstimo ativo

7️⃣ Regras de Consulta

O sistema permite:

- Listar livros disponíveis

- Listar livros emprestados

- Listar empréstimos ativos por usuário

📌 Consultas não alteram o estado do sistema

8️⃣ Regras de Erro

Toda violação gera uma exceção específica de domínio, como:

        LivroIndisponivelError

        LimiteEmprestimosExcedidoError

        DataInvalidaError

# As mensagens devem ser claras, objetivas e amigáveis





 
