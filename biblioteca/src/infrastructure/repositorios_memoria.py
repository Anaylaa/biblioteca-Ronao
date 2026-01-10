from src.domain.repositorios import (
    RepositorioUsuarios,
    RepositorioLivros,
    RepositorioEmprestimos
)
from src.domain.excecoes import EntidadeNaoEncontradaError


class RepositorioBaseMemoria:
    def __init__(self):
        self._dados = []
        self._contador_id = 1

    def _gerar_id(self):
        id_atual = self._contador_id
        self._contador_id += 1
        return id_atual

    def listar_todos(self):
        return self._dados

    def buscar_por_id(self, id):
        for obj in self._dados:
            if obj.id == id:
                return obj
        raise EntidadeNaoEncontradaError(f"ID {id} não encontrado")


# ===================== USUÁRIOS =====================

class RepositorioUsuariosMemoria(RepositorioBaseMemoria, RepositorioUsuarios):

    def adicionar(self, usuario):
        usuario.id = self._gerar_id()
        self._dados.append(usuario)
        return usuario


# ===================== LIVROS =====================

class RepositorioLivrosMemoria(RepositorioBaseMemoria, RepositorioLivros):

    def adicionar(self, livro):
        livro.id = self._gerar_id()
        self._dados.append(livro)
        return livro


# ===================== EMPRÉSTIMOS =====================

class RepositorioEmprestimosMemoria(RepositorioBaseMemoria, RepositorioEmprestimos):

    def adicionar(self, emprestimo):
        emprestimo.id = self._gerar_id()
        self._dados.append(emprestimo)
        return emprestimo
