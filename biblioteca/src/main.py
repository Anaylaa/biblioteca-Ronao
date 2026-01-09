from domain.entidades import Usuario, Livro
from infrastructure.repositorios_memoria import (
    RepositorioUsuariosMemoria,
    RepositorioLivrosMemoria,
    RepositorioEmprestimosMemoria
)
from application.biblioteca_service import BibliotecaService
from interface.cli import menu
from domain.excecoes import (
    LivroIndisponivelError,
    LimiteEmprestimosExcedidoError,
    EmprestimoJaDevolvidoError,
    EntidadeNaoEncontradaError,
    DataInvalidaError
)

def main():
    # Inicializando repositórios
    repo_usuarios = RepositorioUsuariosMemoria()
    repo_livros = RepositorioLivrosMemoria()
    repo_emprestimos = RepositorioEmprestimosMemoria()

    # Inicializando service
    biblioteca = BibliotecaService(repo_usuarios, repo_livros, repo_emprestimos)

    # Cadastro de exemplo
    usuario1 = Usuario(None, "Alice")
    usuario2 = Usuario(None, "Bob")
    repo_usuarios.adicionar(usuario1)
    repo_usuarios.adicionar(usuario2)

    livro1 = Livro(None, "Domínio Limpo", "Robert C. Martin", 2)
    livro2 = Livro(None, "Código Limpo", "Robert C. Martin", 1)
    livro3 = Livro(None, "Python 101", "Michael Driscoll", 3)
    repo_livros.adicionar(livro1)
    repo_livros.adicionar(livro2)
    repo_livros.adicionar(livro3)

    # Seleção do usuário atual
    print("Usuários cadastrados:")
    for u in repo_usuarios.listar_todos():
        print(f"{u.id} - {u.nome}")
    usuario_id = int(input("Digite seu ID de usuário: "))
    
    try:
        usuario_atual = repo_usuarios.buscar_por_id(usuario_id)
    except EntidadeNaoEncontradaError as e:
        print(e)
        return

    # Loop do menu
    while True:
        opcao = menu()
        try:
            if opcao == "1":
                livros = biblioteca.listar_livros_disponiveis()
                print("\n📖 Livros disponíveis:")
                for l in livros:
                    print(f"{l.id} - {l.titulo} (Exemplares: {l.qtdeExemplares})")
            elif opcao == "2":
                livro_id = int(input("Digite o ID do livro que deseja alugar: "))
                emprestimo = biblioteca.emprestar_livro(usuario_id, livro_id)
                print(f"✅ Livro '{emprestimo.livro.titulo}' emprestado com sucesso!")
            elif opcao == "3":
                emprestimos = biblioteca.emprestimos_ativos_do_usuario(usuario_id)
                print("Seus empréstimos ativos:")
                for e in emprestimos:
                    print(f"{e.id} - {e.livro.titulo}")
                emprestimo_id = int(input("Digite o ID do empréstimo que deseja devolver: "))
                biblioteca.devolver_livro(emprestimo_id)
                print("✅ Livro devolvido com sucesso!")
            elif opcao == "4":
                emprestimos = biblioteca.emprestimos_ativos_do_usuario(usuario_id)
                print("Seus empréstimos ativos:")
                for e in emprestimos:
                    print(f"{e.id} - {e.livro.titulo} (Devolver até {e.data_prevista_devolucao.date()})")
            elif opcao == "5":
                emprestimos = biblioteca.emprestimos_ativos_do_usuario(usuario_id)
                print("Seus empréstimos ativos:")
                for e in emprestimos:
                    print(f"{e.id} - {e.livro.titulo} (Devolver até {e.data_prevista_devolucao.date()})")
                emprestimo_id = int(input("Digite o ID do empréstimo que deseja renovar: "))
                biblioteca.renovar_emprestimo(emprestimo_id)
                print("✅ Empréstimo renovado com sucesso!")
            elif opcao == "6":
                emprestimos = biblioteca.emprestimos_ativos_do_usuario(usuario_id)
                print("Dias restantes dos seus empréstimos:")
                for e in emprestimos:
                    print(f"{e.livro.titulo}: {e.dias_restantes()} dias restantes")
            elif opcao == "0":
                print("Saindo...")
                break
            else:
                print("Opção inválida")
        except (LivroIndisponivelError,
                LimiteEmprestimosExcedidoError,
                EmprestimoJaDevolvidoError,
                EntidadeNaoEncontradaError,
                DataInvalidaError) as e:
            print(f"❌ Erro: {e}")

if __name__ == "__main__":
    main()
