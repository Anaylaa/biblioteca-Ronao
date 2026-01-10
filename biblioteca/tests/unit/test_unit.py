import pytest
from src.domain.entidades import Usuario, Livro
from src.infrastructure.repositorios_memoria import (
    RepositorioUsuariosMemoria,
    RepositorioLivrosMemoria,
    RepositorioEmprestimosMemoria
)
from src.application.biblioteca_service import BibliotecaService
from src.domain.excecoes import (
    LivroIndisponivelError,
    LimiteEmprestimosExcedidoError,
    EmprestimoJaDevolvidoError
)

@pytest.fixture
def setup_biblioteca():
    repo_usuarios = RepositorioUsuariosMemoria()
    repo_livros = RepositorioLivrosMemoria()
    repo_emprestimos = RepositorioEmprestimosMemoria()
    service = BibliotecaService(repo_usuarios, repo_livros, repo_emprestimos)

    usuario = Usuario(None, "Alice")
    repo_usuarios.adicionar(usuario)

    livro = Livro(None, "Python 101", "Autor","Programação", 2)
    repo_livros.adicionar(livro)

    return service, usuario, livro

def test_emprestar_livro(setup_biblioteca):
    service, usuario, livro = setup_biblioteca
    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    assert emprestimo.usuario == usuario
    assert emprestimo.livro == livro
    assert livro.qtdeExemplares == 1

def test_devolver_livro(setup_biblioteca):
    service, usuario, livro = setup_biblioteca
    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    service.devolver_livro(emprestimo.id)
    assert livro.qtdeExemplares == 2

def test_renovar_emprestimo(setup_biblioteca):
    service, usuario, livro = setup_biblioteca
    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    prazo_original = emprestimo.data_prevista_devolucao
    service.renovar_emprestimo(emprestimo.id)
    assert emprestimo.data_prevista_devolucao > prazo_original

def test_limite_emprestimos(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    for i in range(7):
        l = Livro(None, f"Livro {i}", "Autor", "Programação", 1)
        service.repo_livros.adicionar(l)
        service.emprestar_livro(usuario.id, l.id)

    l_extra = Livro(None, "Extra", "Autor", "Programação", 1)
    service.repo_livros.adicionar(l_extra)

    with pytest.raises(LimiteEmprestimosExcedidoError):
        service.emprestar_livro(usuario.id, l_extra.id)
