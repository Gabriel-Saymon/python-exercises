def exibir_menu():
    print("\n--- Banco Digital ---")
    print("1: Depositar")
    print("2: Sacar")
    print("3: Consultar Saldo")
    print("4: Criar Nova Conta")
    print("5: Listar Contas")
    print("0: Sair")
    print("---------------------")

def depositar(contas):
    num_conta = input("Digite o número da conta para depósito: ")

    if num_conta in contas:
        try:
            valor = float(input("Digite o valor a ser depositado: R$ "))
            if valor > 0:
                contas[num_conta] += valor
                print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
                print(f"Novo saldo: R$ {contas[num_conta]:.2f}")
            else:
                print("Erro: O valor do depósito deve ser positivo.")
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número.")
    else:
        print(f"Erro: Conta '{num_conta}' não encontrada.")

def sacar(contas):
    num_conta = input("Digite o número da conta para saque: ")

    if num_conta in contas:
        try:
            valor = float(input("Digite o valor a ser sacado: R$ "))
            if valor <= 0:
                print("Erro: O valor do saque deve ser positivo.")
                return

            # Verifica se há saldo suficiente
            if valor <= contas[num_conta]:
                contas[num_conta] -= valor
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
                print(f"Novo saldo: R$ {contas[num_conta]:.2f}")
            else:
                print("Erro: Saldo insuficiente.")
                print(f"Saldo disponível: R$ {contas[num_conta]:.2f}")
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número.")
    else:
        print(f"Erro: Conta '{num_conta}' não encontrada.")

def consultar_saldo(contas):
    """Consulta o saldo de uma conta específica."""
    num_conta = input("Digite o número da conta para consulta: ")
    
    if num_conta in contas:
        saldo = contas[num_conta]
        print(f"Saldo da conta {num_conta}: R$ {saldo:.2f}")
    else:
        print(f"Erro: Conta '{num_conta}' não encontrada.")

def criar_conta(contas):
    """Cria uma nova conta no dicionário."""
    num_conta = input("Digite o número da nova conta (ex: 1234-5): ")

    if num_conta in contas:
        print("Erro: Esta conta já existe!")
    else:
        try:
            # Permite um depósito inicial opcional
            saldo_inicial = float(input("Digite o depósito inicial (ou 0 se não houver): R$ "))
            if saldo_inicial < 0:
                print("Erro: O depósito inicial não pode ser negativo.")
                return
            
            contas[num_conta] = saldo_inicial
            print(f"Conta {num_conta} criada com sucesso com saldo de R$ {saldo_inicial:.2f}!")
        except ValueError:
            print("Erro: Valor inválido. Por favor, digite um número.")

def listar_contas(contas):
    """Lista todas as contas existentes."""
    print("\n--- Contas Cadastradas ---")
    if not contas:
        print("Nenhuma conta cadastrada.")
    else:
        for conta, saldo in contas.items():
            print(f"Conta: {conta} | Saldo: R$ {saldo:.2f}")

# --- Programa Principal ---
if __name__ == "__main__":
    
    banco_de_dados = {
        "123-4": 1500.75,
        "567-8": 250.00,
        "901-2": 5000.00
    }
    
    while True:
        exibir_menu()
        
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            depositar(banco_de_dados)
        elif escolha == '2':
            sacar(banco_de_dados)
        elif escolha == '3':
            consultar_saldo(banco_de_dados)
        elif escolha == '4':
            criar_conta(banco_de_dados)
        elif escolha == '5':
            listar_contas(banco_de_dados)
        elif escolha == '0':
            print("Obrigado por usar nosso banco. Volte sempre!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")