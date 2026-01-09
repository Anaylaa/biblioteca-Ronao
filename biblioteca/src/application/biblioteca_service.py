from datetime import datetime
from src.domain.entidades import Usuario, Livro, Emprestimo
from src.domain.excecoes import (
    LivroIndisponivelError,
    LimiteEmprestimosExcedidoError,
    EmprestimoJaDevolvidoError,
    EntidadeNaoEncontradaError
)

class BibliotecaService:
    def __init__(self, repo_usuarios, repo_livros, repo_emprestimos):
        self.repo_usuarios = repo_usuarios
        self.repo_livros = repo_livros
        self.repo_emprestimos = repo_emprestimos

    # ------------------- Empréstimo -------------------
    def emprestar_livro(self, usuario_id: int, livro_id: int) -> Emprestimo:
        usuario = self.repo_usuarios.buscar_por_id(usuario_id)
        livro = self.repo_livros.buscar_por_id(livro_id)

        if livro.qtdeExemplares <= 0:
            raise LivroIndisponivelError(f"Livro '{livro.titulo}' indisponível")
        if len(usuario.emprestimos_ativos()) >= 7:
            raise LimiteEmprestimosExcedidoError("Usuário atingiu o limite de empréstimos")

        emprestimo = Emprestimo(None, usuario, livro)
        self.repo_emprestimos.adicionar(emprestimo)
        return emprestimo

    # ------------------- Devolução -------------------
    def devolver_livro(self, emprestimo_id: int):
        emprestimo = self.repo_emprestimos.buscar_por_id(emprestimo_id)
        emprestimo.devolver()
        return emprestimo

    # ------------------- Renovação -------------------
    def renovar_emprestimo(self, emprestimo_id: int):
        emprestimo = self.repo_emprestimos.buscar_por_id(emprestimo_id)
        emprestimo.renovar()
        return emprestimo

    # ------------------- Consultas -------------------
    def listar_livros_disponiveis(self):
        return [l for l in self.repo_livros.listar_todos() if l.disponivel()]

    def listar_livros_emprestados(self):
        return [l for l in self.repo_livros.listar_todos() if not l.disponivel()]

    def listar_emprestimos_ativos_por_usuario(self, usuario_id: int):
        usuario = self.repo_usuarios.buscar_por_id(usuario_id)
        return usuario.emprestimos_ativos()
