from domain.repositorios import RepositorioUsuarios, RepositorioLivros, RepositorioEmprestimos

class RepositorioUsuariosMemoria(RepositorioUsuarios):
    def __init__(self):
        self.usuarios = []

    def adicionar(self, usuario):
        self.usuarios.append(usuario)

    def listar_todos(self):
        return self.usuarios

class RepositorioLivrosMemoria(RepositorioLivros):
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def listar_todos(self):
        return self.livros

class RepositorioEmprestimosMemoria(RepositorioEmprestimos):
    def __init__(self):
        self.emprestimos = []

    def adicionar(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def listar_todos(self):
        return self.emprestimos
