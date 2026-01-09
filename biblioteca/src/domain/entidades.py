from datetime import datetime, timedelta
from .excecoes import (
    LivroIndisponivelError,
    LimiteEmprestimosExcedidoError,
    EmprestimoJaDevolvidoError,
    DataInvalidaError
)

class Usuario:
    LIMITE_EMPRESTIMOS = 7

    def __init__(self, id: int, nome: str):
        self.id = id
        self.nome = nome
        self.emprestimos_ativos = []

    def pode_emprestar(self):
        if len(self.emprestimos_ativos) >= self.LIMITE_EMPRESTIMOS:
            raise LimiteEmprestimosExcedidoError(
                f"Usuário '{self.nome}' atingiu o limite de {self.LIMITE_EMPRESTIMOS} empréstimos ativos"
            )
        for e in self.emprestimos_ativos:
            if e.esta_atrasado():
                raise DataInvalidaError(f"Usuário '{self.nome}' possui empréstimo atrasado")
        return True

    def adicionar_emprestimo(self, emprestimo):
        self.emprestimos_ativos.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self.emprestimos_ativos.remove(emprestimo)


class Livro:
    def __init__(self, id: int, titulo: str, autor: str, qtdeExemplares: int):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.qtdeExemplares = qtdeExemplares

    def disponivel(self):
        return self.qtdeExemplares > 0

    def emprestar(self):
        if self.qtdeExemplares <= 0:
            raise LivroIndisponivelError(f"Livro '{self.titulo}' indisponível")
        self.qtdeExemplares -= 1

    def devolver(self):
        self.qtdeExemplares += 1


from datetime import datetime, timedelta
from src.domain.entidades import Usuario, Livro
from src.domain.excecoes import (
    LivroIndisponivelError,
    EmprestimoJaDevolvidoError,
    DataInvalidaError
)

class Emprestimo:
    PRAZO_PADRAO = 7  # dias
    MAX_RENOVACOES = 1

    def __init__(self, id: int, usuario: Usuario, livro: Livro):
        # Validar regras de negócio
        if not livro.disponivel():
            raise LivroIndisponivelError(f"Livro '{livro.titulo}' indisponível")
        usuario.pode_emprestar()

        self.id = id
        self.usuario = usuario
        self.livro = livro
        self.data_emprestimo = datetime.now()
        self.data_prevista_devolucao = self.data_emprestimo + timedelta(days=self.PRAZO_PADRAO)
        self.data_devolucao = None
        self.renovacoes = 0

        # Atualizar estado do usuário e do livro
        livro.emprestar()
        usuario.adicionar_emprestimo(self)

    def devolver(self):
        if self.data_devolucao:
            raise EmprestimoJaDevolvidoError("Empréstimo já foi devolvido")
        if datetime.now() < self.data_emprestimo:
            raise DataInvalidaError("Data de devolução anterior à data do empréstimo")

        self.data_devolucao = datetime.now()
        self.livro.devolver()
        self.usuario.remover_emprestimo(self)

    def renovar(self):
        if self.data_devolucao:
            raise EmprestimoJaDevolvidoError("Não é possível renovar empréstimo já devolvido")
        if self.renovacoes >= self.MAX_RENOVACOES:
            raise DataInvalidaError("Limite de renovações atingido")

        self.data_prevista_devolucao += timedelta(days=self.PRAZO_PADRAO)
        self.renovacoes += 1

    def esta_ativo(self):
        """Verifica se o empréstimo ainda não foi devolvido"""
        return self.data_devolucao is None

    def esta_atrasado(self):
        """Verifica se o empréstimo está ativo e passou da data prevista de devolução"""
        return self.esta_ativo() and datetime.now() > self.data_prevista_devolucao

    def dias_restantes(self):
        """Retorna a quantidade de dias restantes até a devolução"""
        if self.data_devolucao:
            return 0
        delta = self.data_prevista_devolucao - datetime.now()
        return max(delta.days, 0)
