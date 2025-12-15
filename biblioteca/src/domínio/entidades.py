from datetime import datetime
from domain.excecoes import LivroIndisponivel, EmprestimoJaDevolvido

class Usuario:
    def __init__(self, id: int, nome: str, email: str):
        self.id = id
        self.nome = nome
        self.email = email

class Livro:
    def __init__(self, id: int, titulo: str, autor: str):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Emprestimo:
    def __init__(self, id: int, usuario: Usuario, livro: Livro):
        if not livro.disponivel:
            raise LivroIndisponivel(f"Livro '{livro.titulo}' indisponível")
        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_devolucao = None
        livro.disponivel = False

    def devolver(self):
        if self.data_devolucao is not None:
            raise EmprestimoJaDevolvido("Empréstimo já foi devolvido")
        self.data_devolucao = datetime.now()
        self.livro.disponivel = True
