from typing import List
from time import sleep

from functions.client import Client
from functions.bank_account import BankAccount

accounts: List[BankAccount] = []


def main() -> None:
    menu()


def menu() -> None:
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~ CAIXA ELETRÔNICO 01 ~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~~ Nuxa bank ~~~~~~~~~~~~~~~~~~~~~~~')
    print('\n')

    print('Selecione uma opção no menu:')
    print(
        '1- Criar conta\n2- Efetuar saque\n3- Efetuar depósito\n4- Efetuar transferência\n\
5- Listar contas\n6- Sair do sistema'
    )

    option: int = int(input())

    if option == 1:
        creating_an_account()
    elif option == 2:
        bank_withdrawal()
    elif option == 3:
        bank_deposit()
    elif option == 4:
        bank_transfer()
    elif option == 5:
        list_accounts()
    elif option == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(2)
        menu()


def creating_an_account() -> None:
    print('Informe os dados do cliente')

    name: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    birth_date: str = input('Data de nascimento do cliente: ')

    client: Client = Client(name, email, cpf, birth_date)

    account_client: BankAccount = BankAccount(client)

    accounts.append(account_client)

    print('\nConta criada com sucesso!')
    print('-------------- Dados da conta --------------')
    print('--------------------------------------------\n')
    print(account_client)
    sleep(2)
    menu()


def bank_withdrawal() -> None:

    if len(accounts) > 0:
        number_account: int = int(input('Informe o número da sua conta: '))
        account: BankAccount = search_by_bank_account_number(number_account)

        if account:
            value: float = float(input('Informe o valor do saque: '))
            account.withdrawal_money(value)

        else:
            print(
                f'Não foi possível encontrar a conta com o número: {number_account}'
            )

    else:
        print('Ainda não existem contas cadastradas')

    sleep(2)
    menu()


def bank_deposit() -> None:

    if len(accounts) > 0:
        number_account: int = int(
            input('Informe o número da conta para depósito: ')
        )
        account: BankAccount = search_by_bank_account_number(number_account)

        if account:
            value: float = float(input('Informe o valor do depósito: '))
            account.deposit_money(value)

        else:
            print(
                f'Não foi possível encontrar a conta com o número: {number_account}'
            )

    else:
        print('Ainda não existem contas cadastradas')

    sleep(2)
    menu()


def bank_transfer() -> None:

    if len(accounts) > 0:
        number_source_account: int = int(
            input('Informe o número da conta de origem: ')
        )
        source_account: BankAccount = search_by_bank_account_number(
            number_source_account
        )

        if source_account:
            destination_number_account: int = int(
                input('Informe o número da conta de destino: ')
            )
            destination_account: BankAccount = search_by_bank_account_number(
                destination_number_account
            )

            if destination_account:
                value: float = float(
                    input('Informe o valor da transferência: ')
                )
                source_account.transfer_money(destination_account, value)

            else:
                print(
                    'O número da conta de destino não encontra-se no sistema'
                )

        else:
            print(
                f'Não foi possível encontrar a conta com o número: {number_source_account}'
            )

    else:
        print('Ainda não existem contas cadastradas')

    sleep(2)
    menu()


def list_accounts() -> None:

    if len(accounts) > 0:
        print('~~~~~~~~~~~~~~ Lista de contas ~~~~~~~~~~~~~~\n')

        for account in accounts:
            print(account)
            print('-------------------------')
            sleep(1)

    else:
        print('Não existem constas cadastradas')

    sleep(2)
    menu()


def search_by_bank_account_number(number: int) -> BankAccount:

    ac: BankAccount = None

    if len(accounts) > 0:

        for account in accounts:
            if account.number_account == number:
                ac = account
    return ac


if __name__ == '__main__':
    main()
