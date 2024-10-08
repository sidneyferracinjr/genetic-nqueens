from sequential_solver import main as sequential_main
from parallel_solver import main as parallel_main
from thread_solver import main as thread_main
from save_board import clear_logs

def main(n):
    """
    Função principal para executar todas as implementações do problema das N-rainhas.
    
    Repositório Git do trabalho: https://github.com/sidneyferracinjr/ds-nqueens
    """
    # Limpa os logs antigos antes de iniciar uma nova execução
    clear_logs()

    print("Executando Sequential Solver:")
    sequential_main(n)
    
    print("\nExecutando Parallel Solver:")
    parallel_main(n)
    
    print("\nExecutando Thread Solver:")
    thread_main(n)

# Exemplo de uso:
if __name__ == "__main__":
    main(12)  # Substitua 8 pelo tamanho desejado do tabuleiro
    input("Pressione Enter para sair...")


"""
github: https://github.com/sidneyferracinjr/ds-nqueens
"""