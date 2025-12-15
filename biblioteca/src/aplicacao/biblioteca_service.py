from domain.entidades import Emprestimo

class BibliotecaService:
    def __init__(self, repo_usuarios, repo_livros, repo_emprestimos):
        self.repo_usuarios = repo_usuarios
        self.repo_livros = repo_livros
        self.repo_emprestimos = repo_emprestimos

    def emprestar_livro(self, usuario_id, livro_id):
        usuario = next(u for u in self.repo_usuarios.listar_todos() if u.id == usuario_id)
        livro = next(l for l in self.repo_livros.listar_todos() if l.id == livro_id)
        emprestimo = Emprestimo(len(self.repo_emprestimos.listar_todos()) + 1, usuario, livro)
        self.repo_emprestimos.adicionar(emprestimo)
        return emprestimo

    def devolver_livro(self, emprestimo_id):
        emprestimo = next(e for e in self.repo_emprestimos.listar_todos() if e.id == emprestimo_id)
        emprestimo.devolver()
        return emprestimo
