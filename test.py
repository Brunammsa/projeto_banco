from functions.client import Client
from functions.bank_account import BankAccount

Bruna: Client = Client(
    'Bruna Piluxa', 'bruna@gmail.com', '123.456.789-00', '09/06/1993'
)
Vanessa: Client = Client(
    'Vanessa nhoc', 'vanessa@gmail.com', '987.654.321-00', '07/10/1993'
)

# print(Bruna)
# print(Vanessa)

accountb = BankAccount(Bruna)
accountv = BankAccount(Vanessa)

# print(accountb)
# print(accountv)
