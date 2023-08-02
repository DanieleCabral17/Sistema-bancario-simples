MENU = """

[d] = Deposito 
[s] = Saque
[e] = Extrato
[a] = Sair

=>  """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
limite_saque = 3

while True:
   
    opcao = input(MENU)
    
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor > 0:
           saldo += valor
           extrato += f"Deposito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor informado é invalido.")        
        
    elif opcao == "s":
        valor = float(input("Informe o valor do Saque: "))
        
        excedeu_saldo = valor > saldo
       
        excedeu_limite = valor > limite
       
        excedeu_saque = numero_saque >= limite_saque
       
        if excedeu_saldo:
           print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque:  
            print("Operação falhou! Número de saques excedido.")
        
        elif valor > 0:
             saldo -= valor
             extrato += f"saque: R$ {valor:.2f}\n"
             numero_saque += 1   
        else:
            print ("Operação falhou,O valor informado é inválido.")  
        
    elif opcao == "e":
        print("\n##########EXTRATO############")
        print("Não foram realizados movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("#############################################################")
        
    elif  opcao == "a":
        break
        
    else:
        print ("Operação inválida, por favor selecione novamente a operação desejada.")