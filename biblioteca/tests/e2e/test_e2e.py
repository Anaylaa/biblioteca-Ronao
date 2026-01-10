import pytest
from src.domain.entidades import Usuario, Livro
from src.infrastructure.repositorios_memoria import (
    RepositorioUsuariosMemoria,
    RepositorioLivrosMemoria,
    RepositorioEmprestimosMemoria
)
from src.application.biblioteca_service import BibliotecaService
from src.domain.excecoes import LivroIndisponivelError


def test_fluxo_completo():
    repo_usuarios = RepositorioUsuariosMemoria()
    repo_livros = RepositorioLivrosMemoria()
    repo_emprestimos = RepositorioEmprestimosMemoria()

    service = BibliotecaService(
        repo_usuarios,
        repo_livros,
        repo_emprestimos
    )

    # Criar usuários
    u1 = Usuario(None, "Alice")
    u2 = Usuario(None, "Bob")
    repo_usuarios.adicionar(u1)
    repo_usuarios.adicionar(u2)

    # Criar livro com apenas 1 exemplar
    l1 = Livro(None, "Python 101", "Autor", "Programação", 1)
    repo_livros.adicionar(l1)

    # Alice pega o livro
    e1 = service.emprestar_livro(u1.id, l1.id)
    assert l1.qtdeExemplares == 0

    # Bob NÃO consegue pegar
    with pytest.raises(LivroIndisponivelError):
        service.emprestar_livro(u2.id, l1.id)

    # Alice devolve
    service.devolver_livro(e1.id)
    assert l1.qtdeExemplares == 1

    # Bob agora consegue pegar
    e2 = service.emprestar_livro(u2.id, l1.id)
    assert e2.usuario == u2
    assert l1.qtdeExemplares == 0
