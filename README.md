 # Visão Geral

### Este projeto implementa um Sistema de Gerenciamento de Empréstimos de Livros, desenvolvido em Python, aplicando os princípios de Domain-Driven Design (DDD) Leve.

## O sistema permite:

📖 Cadastro de livros

👤 Cadastro de usuários

🔄 Empréstimos e devoluções

        Respeitando rigorosamente as regras de negócio:

❌ Um livro não pode ser emprestado se já estiver emprestado

🔢 Um usuário não pode ultrapassar o limite de empréstimos simultâneos

📅 Datas de empréstimo e devolução devem ser válidas

🔁 Controle completo do ciclo de vida do empréstimo

### O foco do projeto está na organização arquitetural, separação de responsabilidades, regras de negócio puras e testes abrangentes, conforme especificado na disciplina.

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