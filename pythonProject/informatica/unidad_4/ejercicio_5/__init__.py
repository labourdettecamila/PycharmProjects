account_1 = {"user_id": "camilabour", "password": "cami", "saving_bank":{"account_num":"2003", "amount":40900},
             "current_account": {"account_num":"3002", "amount":90400}, "last_trxs":[100,200,300]}

account_2 = {"user_id": "marianex", "password": "mari", "saving_bank":{"account_num":"1975", "amount":30500},
             "current_account": {"account_num":"5791", "amount":50300}, "last_trxs":[400,500,600]}

accounts = [account_1, account_2]

active = True

while active:

    print("\n")
    print("-------------------------")
    print("BANCO DIGITAL LA")
    print("-------------------------")

    id = input("Nombre de usuario: ")
    password = input("Contraseña: ")

    exist = 0
    numero_de_cuenta = 0

    for account in accounts:
        if id == account["user_id"] and password == account["password"]:
            exist += 1
            account_index = accounts.index(account)

    if exist != 0:

        login = True

        while login:

            print("\nOperaciones disponibles")
            print("1) Acreditar en CA")
            print("2) Acreditar en CC")
            print("3) Consultar saldo en CA")
            print("4) Consultar saldo en CC")
            print("5) Consultar Trx")
            print("6) Salir")

            option = input("\nOpción: ")

            try:
                if int(option) < 1 or int(option) > 6:
                    print("Debe seleccionar una opcion válida.")
                    continue

                if option == "6":
                    login = False

                if option == "1":
                    acreditación_ca = input("Monto a acreditar: ")
                    accounts[numero_de_cuenta]["saving_bank"]["amount"]+= int(acreditación_ca)
                    print("Muchas gracias, monto acreditado.")

                if option == "3":
                    print("Su saldo en CA es: ")
                    print(accounts[numero_de_cuenta]["saving_bank"]["amount"])

                if option == "2":
                    acreditación_cc = input("Monto a acreditar: ")
                    accounts[numero_de_cuenta]["current_account"]["amount"] += int(acreditación_cc)
                    print("Muchas gracias, monto acreditado.")

                if option == "4":
                    print("Su saldo en CC es: ")
                    print(accounts[numero_de_cuenta]["current_account"]["amount"])

                if option == "5":
                    print("Éstas son las últimas transacciones realizadas:")
                    for trx in accounts[numero_de_cuenta]["last_trxs"]:
                        print(f"\t {trx}")

            except ValueError:
                print("Debe ingresar un número.")

    else:
        print("Permiso denegado - Usuario inválido")

