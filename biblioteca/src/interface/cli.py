from src.application.biblioteca_service import BibliotecaService

def menu():
    print("\n=== Biblioteca ===")
    print("1. Listar livros disponíveis")
    print("2. Alugar livro")
    print("3. Devolver livro")
    print("4. Listar meus empréstimos ativos")
    print("5. Renovar empréstimo")
    print("6. Ver dias restantes de empréstimos")
    print("0. Sair")
    return input("Escolha uma opção: ")
