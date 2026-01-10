from src.domain.entidades import Usuario, Livro
from src.infrastructure.repositorios_memoria import (
    RepositorioUsuariosMemoria,
    RepositorioLivrosMemoria,
    RepositorioEmprestimosMemoria
)
from application.biblioteca_service import BibliotecaService

# === SETUP ===
repo_usuarios = RepositorioUsuariosMemoria()
repo_livros = RepositorioLivrosMemoria()
repo_emprestimos = RepositorioEmprestimosMemoria()

service = BibliotecaService(repo_usuarios, repo_livros, repo_emprestimos)

# === CRIA USUÁRIO E LIVRO ===
usuario = Usuario(None, "Alice")
repo_usuarios.adicionar(usuario)

livro = Livro(None, "Python 101", "Autor", "Programação", 2)
repo_livros.adicionar(livro)

print("Usuário ID:", usuario.id)
print("Livro ID:", livro.id)
print("Exemplares:", livro.qtdeExemplares)

# === EMPRÉSTIMO ===
emprestimo = service.emprestar_livro(usuario.id, livro.id)

print("\nApós empréstimo:")
print("Empréstimo ID:", emprestimo.id)
print("Exemplares:", livro.qtdeExemplares)
print("Ativo:", emprestimo.esta_ativo())

# === RENOVAÇÃO ===
service.renovar_emprestimo(emprestimo.id)
print("\nApós renovação:")
print("Nova data:", emprestimo.data_prevista_devolucao)

# === DEVOLUÇÃO ===
service.devolver_livro(emprestimo.id)

print("\nApós devolução:")
print("Exemplares:", livro.qtdeExemplares)
print("Ativo:", emprestimo.esta_ativo())
print("Data de devolução:", emprestimo.data_devolucao)
# === FIM DO TESTE MANUAL ===