import pytest
from datetime import timedelta

# ===== Entidades do domínio =====
from src.domain.entidades import Usuario, Livro, Emprestimo
from src.domain.excecoes import (
    LivroIndisponivelError,
    EmprestimoJaDevolvidoError,
    LimiteEmprestimosExcedidoError
)

# ===== Repositórios em memória =====
from src.infrastructure.repositorios_memoria import (
    RepositorioUsuariosMemoria,
    RepositorioLivrosMemoria,
    RepositorioEmprestimosMemoria
)

# ===== Serviço da aplicação =====
from src.application.biblioteca_service import BibliotecaService


# =========================================================
# FIXTURE PRINCIPAL
# =========================================================
@pytest.fixture
def setup_biblioteca():
    repo_usuarios = RepositorioUsuariosMemoria()
    repo_livros = RepositorioLivrosMemoria()
    repo_emprestimos = RepositorioEmprestimosMemoria()

    service = BibliotecaService(
        repo_usuarios,
        repo_livros,
        repo_emprestimos
    )

    usuario = Usuario(None, "Alice")
    repo_usuarios.adicionar(usuario)

    livro = Livro(None, "Python 101", "Autor", "Programação", 2)
    repo_livros.adicionar(livro)

    return service, usuario, livro


# =========================================================
# TESTES DE EMPRÉSTIMO
# =========================================================
def test_emprestar_livro(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    emprestimo = service.emprestar_livro(usuario.id, livro.id)

    assert emprestimo.usuario == usuario
    assert emprestimo.livro == livro
    assert livro.qtdeExemplares == 1
    assert livro.disponivel()
    assert emprestimo.esta_ativo()


def test_livro_indisponivel(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    service.emprestar_livro(usuario.id, livro.id)
    service.emprestar_livro(usuario.id, livro.id)

    with pytest.raises(LivroIndisponivelError):
        service.emprestar_livro(usuario.id, livro.id)


# =========================================================
# TESTES DE DEVOLUÇÃO
# =========================================================
def test_devolver_livro(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    service.devolver_livro(emprestimo.id)

    assert livro.qtdeExemplares == 2
    assert livro.disponivel()
    assert not emprestimo.esta_ativo()
    assert emprestimo.data_devolucao is not None


def test_devolver_emprestimo_ja_devolvido(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    service.devolver_livro(emprestimo.id)

    with pytest.raises(EmprestimoJaDevolvidoError):
        service.devolver_livro(emprestimo.id)


# =========================================================
# TESTES DE RENOVAÇÃO
# =========================================================
def test_renovar_emprestimo(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    prazo_original = emprestimo.data_prevista_devolucao

    service.renovar_emprestimo(emprestimo.id)

    assert emprestimo.data_prevista_devolucao > prazo_original
    assert emprestimo.esta_ativo()


def test_renovar_emprestimo_devolvido(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    service.devolver_livro(emprestimo.id)

    with pytest.raises(EmprestimoJaDevolvidoError):
        service.renovar_emprestimo(emprestimo.id)


# =========================================================
# TESTES DE CONSULTA
# =========================================================
def test_listar_emprestimos_ativos_por_usuario(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    emprestimo = service.emprestar_livro(usuario.id, livro.id)
    emprestimos_ativos = service.listar_emprestimos_ativos_por_usuario(usuario.id)

    assert len(emprestimos_ativos) == 1
    assert emprestimos_ativos[0] == emprestimo


def test_listar_livros_disponiveis(setup_biblioteca):
    service, usuario, livro = setup_biblioteca

    livros_disponiveis = service.listar_livros_disponiveis()
    assert livro in livros_disponiveis

    service.emprestar_livro(usuario.id, livro.id)
    service.emprestar_livro(usuario.id, livro.id)

    livros_disponiveis = service.listar_livros_disponiveis()
    assert livro not in livros_disponiveis
