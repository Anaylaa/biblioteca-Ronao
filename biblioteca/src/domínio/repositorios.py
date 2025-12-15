from abc import ABC, abstractmethod

class RepositorioUsuarios(ABC):
    @abstractmethod
    def adicionar(self, usuario): pass

    @abstractmethod
    def listar_todos(self): pass

class RepositorioLivros(ABC):
    @abstractmethod
    def adicionar(self, livro): pass

    @abstractmethod
    def listar_todos(self): pass

class RepositorioEmprestimos(ABC):
    @abstractmethod
    def adicionar(self, emprestimo): pass

    @abstractmethod
    def listar_todos(self): pass
