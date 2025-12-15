📚 Sistema de Biblioteca — Empréstimo de Livros (DDD Leve)
📌 Visão Geral

Este projeto implementa um Sistema de Gerenciamento de Empréstimos de Livros, desenvolvido em Python, aplicando os princípios de Domain-Driven Design (DDD) Leve.

O sistema permite cadastrar livros e usuários, realizar empréstimos e devoluções, garantindo regras de negócio como:

Um livro não pode ser emprestado se já estiver emprestado;

Um usuário não pode ultrapassar o limite de empréstimos simultâneos;

Datas de empréstimo e devolução devem ser válidas;

Controle total do ciclo de vida do empréstimo.

O foco do projeto está na organização arquitetural, separação de responsabilidades, regras de negócio puras e testes abrangentes, conforme especificado na disciplina.

🎯 Objetivo do Trabalho

Aplicar DDD Leve na prática

Separar claramente:

Domínio

Infraestrutura

Aplicação

Interface do Usuário

Desenvolver um sistema funcional com dados em memória

Criar uma suíte completa de testes unitários, integração e E2E
