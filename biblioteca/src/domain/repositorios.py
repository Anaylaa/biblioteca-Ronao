from abc import ABC, abstractmethod

class RepositorioUsuarios(ABC):
    @abstractmethod
    def adicionar(self, usuario): pass

    @abstractmethod
    def listar_todos(self): pass

    @abstractmethod
    def buscar_por_id(self, id): pass


class RepositorioLivros(ABC):
    @abstractmethod
    def adicionar(self, livro): pass

    @abstractmethod
    def listar_todos(self): pass

    @abstractmethod
    def buscar_por_id(self, id): pass


class RepositorioEmprestimos(ABC):
    @abstractmethod
    def adicionar(self, emprestimo): pass

    @abstractmethod
    def listar_todos(self): pass

    @abstractmethod
    def buscar_por_id(self, id): pass

class RepositorioReservas(ABC):
    @abstractmethod
    def adicionar(self, reserva): ...
    @abstractmethod

    def listar_todos(self): ... 
    @abstractmethod

    def buscar_por_usuario_e_livro(self, usuario_id, livro_id): ...
    def remover(self, reserva): ...
    @abstractmethod

    def listar_reservas_por_livro(self, livro_id): ...
    @abstractmethod

    def listar_reservas_por_usuario(self, usuario_id): ...
    @abstractmethod

    def listar_reservas_expiradas(self): ...
    @abstractmethod

    def listar_reservas_validas(self): ...
    @abstractmethod

    def listar_reservas_validas(self): ...
    pass

