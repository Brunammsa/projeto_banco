from functions.client import Client
from functions.helpers import format_float_to_str_currency


class BankAccount:

    code: int = 1001

    def __init__(self: object, client: Client) -> None:
        self.__number_account: int = BankAccount.code
        self.__client: Client = client
        self.__balance_account: float = 0.0
        self.__limit: float = 100.0
        self.__balance_account_total: float = (
            self._calculate_balance_account_total
        )
        BankAccount.code += 1

    def __str__(self: object) -> str:

        return f'Número da conta: {self.number_account}\nCliente: {self.client.name}\n\
Saldo total: {format_float_to_str_currency(self.balance_account_total)}'

    @property
    def number_account(self: object) -> int:
        return self.__number_account

    @property
    def client(self: object) -> Client:
        return self.__client

    @property
    def balance_account(self: object) -> float:
        return self.__balance_account

    @balance_account.setter
    def balance_account(self: object, value: float) -> None:
        self.__balance_account = value

    @property
    def limit(self: object) -> float:
        return self.__limit

    @limit.setter
    def limit(self: object, value: float) -> None:
        self.__limit = value

    @property
    def balance_account_total(self: object) -> float:
        return self.__balance_account_total

    @balance_account_total.setter
    def balance_account_total(self: object, value: float) -> None:
        self.__balance_account_total = value

    @property
    def _calculate_balance_account_total(self: object) -> float:
        return self.balance_account + self.limit

    def deposit_money(self: object, value: float) -> None:

        if value > 0:
            self.balance_account = self.balance_account + value

            self.balance_account_total = self._calculate_balance_account_total

            print('Depósito efetuado com sucesso')

        else:
            print('Erro ao efetuar o depósito, tente novamente.')

    def withdrawal_money(self: object, value: float) -> None:
        if value > 0 and self.balance_account_total >= value:
            if self.balance_account >= value:
                self.balance_account = self.balance_account - value
                self.balance_account_total = (
                    self._calculate_balance_account_total
                )
            else:
                rest: float = self.balance_account - value
                self.limit = self.limit + rest
                self.balance_account_total = (
                    self._calculate_balance_account_total
                )
            print('Saque efetuado com sucesso')
        else:
            print('Saque não realizado, tente novamente')

    def transfer_money(
        self: object, destination: object, value: float
    ) -> None:
        if value > 0 and self.balance_account >= value:
            if self.balance_account >= value:
                self.balance_account = self.balance_account - value
                self.balance_account_total = (
                    self._calculate_balance_account_total
                )
                destination.balance_account = (
                    destination.balance_account + value
                )
                destination.balance_account_total = (
                    destination._calculate_balance_account_total
                )

            else:
                rest: float = self.balance_account - value
                self.balance_account = 0
                self.limit = self.limit + rest
                self.balance_account_total = (
                    self._calculate_balance_account_total
                )
                destination.balance_account = (
                    destination.balance_account + value
                )
                destination.balance_account_total = (
                    destination._calculate_balance_account_total
                )
            print('Transferência realizada com sucesso')
        else:
            print('Transferência não realizada, tente novamente')
