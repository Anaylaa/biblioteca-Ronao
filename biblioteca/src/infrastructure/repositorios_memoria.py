from src.domain.repositorios import RepositorioUsuarios, RepositorioLivros, RepositorioEmprestimos
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


class RepositorioUsuariosMemoria(RepositorioBaseMemoria, RepositorioUsuarios):
    def __init__(self):
        super().__init__()

    def adicionar(self, usuario):
        usuario.id = self._gerar_id()
        self._dados.append(usuario)
    def adicionar(self, entidade):
        if any(e.id == entidade.id for e in self._dados if hasattr(entidade, 'id')):
            raise ValueError(f"ID {entidade.id} já existe")
        entidade.id = self._gerar_id()
        self._dados.append(entidade)
    


class RepositorioLivrosMemoria(RepositorioBaseMemoria, RepositorioLivros):
    def __init__(self):
        super().__init__()

    def adicionar(self, livro):
        livro.id = self._gerar_id()
        self._dados.append(livro)


class RepositorioEmprestimosMemoria(RepositorioEmprestimos, RepositorioBaseMemoria):
    def __init__(self):
        super().__init__()

    def adicionar(self, emprestimo):
        emprestimo.id = self._gerar_id()
        self._dados.append(emprestimo)
