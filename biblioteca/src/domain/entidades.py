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
        self._emprestimos = []

    def emprestimos_ativos(self):
        return [e for e in self._emprestimos if e.esta_ativo()]

    def pode_emprestar(self):
        if len(self.emprestimos_ativos()) >= self.LIMITE_EMPRESTIMOS:
            raise LimiteEmprestimosExcedidoError(
                f"Usuário '{self.nome}' atingiu o limite de {self.LIMITE_EMPRESTIMOS} empréstimos ativos"
            )

        for e in self.emprestimos_ativos():
            if e.esta_atrasado():
                raise DataInvalidaError(
                    f"Usuário '{self.nome}' possui empréstimo atrasado"
                )
        return True

    def adicionar_emprestimo(self, emprestimo):
        self._emprestimos.append(emprestimo)

    def remover_emprestimo(self, emprestimo):
        self._emprestimos.remove(emprestimo)

    def esta_bloqueado(self):
        for e in self.emprestimos_ativos():
            if e.esta_atrasado():
                return True
        return False

class Livro:
    def __init__(self, id: int, titulo: str, autor: str, categoria: str, qtdeExemplares: int):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.categoria = categoria
        self.qtdeExemplares = qtdeExemplares

    def disponivel(self):
        return self.qtdeExemplares > 0

    def emprestar(self):
        if self.qtdeExemplares <= 0:
            raise LivroIndisponivelError(f"Livro '{self.titulo}' indisponível")
        self.qtdeExemplares -= 1

    def devolver(self):
        self.qtdeExemplares += 1


class Emprestimo:
    PRAZO_PADRAO = 7
    MAX_RENOVACOES = 1

    def __init__(self, id: int, usuario: Usuario, livro: Livro):
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

        livro.emprestar()
        usuario.adicionar_emprestimo(self)

    def devolver(self):
        if self.data_devolucao:
            raise EmprestimoJaDevolvidoError("Empréstimo já foi devolvido")

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
        return self.data_devolucao is None

    def esta_atrasado(self):
        return self.esta_ativo() and datetime.now() > self.data_prevista_devolucao

    def dias_restantes(self):
        if self.data_devolucao:
            return 0
        delta = self.data_prevista_devolucao - datetime.now()
        return max(delta.days, 0)

    def dias_em_atraso(self):
        if not self.esta_atrasado():
            return 0
        return (datetime.now() - self.data_prevista_devolucao).days



class Reserva:
    def __init__(self, usuario, livro, data):
        self.usuario = usuario
        self.livro = livro
        self.data = data
    def esta_valida(self):
        return datetime.now() <= self.data + timedelta(days=3)