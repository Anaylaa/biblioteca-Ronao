from src.domain.entidades import Emprestimo

class BibliotecaService:
    def __init__(self, repo_usuarios, repo_livros, repo_emprestimos):
        self.repo_usuarios = repo_usuarios
        self.repo_livros = repo_livros
        self.repo_emprestimos = repo_emprestimos

    # ------------------- Empréstimo -------------------
    def emprestar_livro(self, usuario_id: int, livro_id: int):
        usuario = self.repo_usuarios.buscar_por_id(usuario_id)
        livro = self.repo_livros.buscar_por_id(livro_id)

        # ✅ regra no domínio
        emprestimo = Emprestimo(None, usuario, livro)
        self.repo_emprestimos.adicionar(emprestimo)
        return emprestimo

    # ------------------- Devolução -------------------
    def devolver_livro(self, emprestimo_id: int):
        emprestimo = self.repo_emprestimos.buscar_por_id(emprestimo_id)
        emprestimo.devolver()
        return emprestimo

    # ------------------- Renovação -------------------
    def renovar_emprestimo(self, emprestimo_id: int):
        emprestimo = self.repo_emprestimos.buscar_por_id(emprestimo_id)
        emprestimo.renovar()
        return emprestimo

    # ------------------- Consultas -------------------
    def listar_livros_disponiveis(self):
        return [l for l in self.repo_livros.listar_todos() if l.disponivel()]

    def listar_emprestimos_ativos_por_usuario(self, usuario_id: int):
        usuario = self.repo_usuarios.buscar_por_id(usuario_id)
        return usuario.emprestimos_ativos()

    def listar_emprestimos_por_livro(self, livro_id: int):
        return [
            e for e in self.repo_emprestimos.listar_todos()
            if e.livro.id == livro_id and e.esta_ativo()
        ]

    def listar_todos_emprestimos(self):
        return self.repo_emprestimos.listar_todos()

    def historico_emprestimos_usuario(self, usuario_id: int):
        return [
            e for e in self.repo_emprestimos.listar_todos()
            if e.usuario.id == usuario_id
        ]

    def listar_emprestimos_atrasados(self):
        return [
            e for e in self.repo_emprestimos.listar_todos()
            if e.esta_atrasado()
        ]

    def calcular_multa(self, emprestimo_id: int):
        emprestimo = self.repo_emprestimos.buscar_por_id(emprestimo_id)
        return emprestimo.dias_em_atraso() * 2
