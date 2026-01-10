import pytest
from datetime import timedelta

# Entidades do domínio
from src.domain.entidades import Usuario, Livro, Emprestimo
from src.domain.excecoes import LivroIndisponivelError, EmprestimoJaDevolvidoError
from src.infrastructure.repositorios_memoria import (
    RepositorioUsuariosMemoria,
    RepositorioLivrosMemoria,
    RepositorioEmprestimosMemoria
)
from src.application.biblioteca_service import BibliotecaService

@pytest.fixture
def setup_biblioteca():
    repo_usuarios = RepositorioUsuariosMemoria()
    repo_livros = RepositorioLivrosMemoria()
    repo_emprestimos = RepositorioEmprestimosMemoria()
    service = BibliotecaService(repo_usuarios, repo_livros, repo_emprestimos)

    usuario = Usuario(None, "Alice")
    repo_usuarios.adicionar(usuario)
    
    livro = Livro(None, "Python 101", "Autor", "Programação", 2)
    repo_livros.adicionar(livro)

    return service, usuario, livro

def test_emprestar_livro(setup_biblioteca):
    service, usuario, livro = setup_biblioteca
    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    assert emprestimo.usuario == usuario
    assert emprestimo.livro == livro
    assert livro.qtdeExemplares == 1
    assert not livro.disponivel if livro.qtdeExemplares == 0 else livro.disponivel

def test_devolver_livro(setup_biblioteca):
    service, usuario, livro = setup_biblioteca
    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    service.devolver_livro(emprestimo.id)
    assert livro.qtdeExemplares == 2
    assert livro.disponivel

def test_renovar_emprestimo(setup_biblioteca):
    service, usuario, livro = setup_biblioteca
    emprestimo = service.emprestar_livro(usuario.id, livro.id)

    # implementa renovar_emprestimo no service
    prazo_original = emprestimo.data_prevista_devolucao
    service.renovar_emprestimo(emprestimo.id)
    assert emprestimo.data_prevista_devolucao > prazo_original
