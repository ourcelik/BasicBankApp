from json import decoder
from time import process_time_ns
from AVL_Tree import AVL_Tree
from Account import Customer
from os import path
import json
from Account import MH, VMH, AH, VAH, YH, VYH, LastProcess
from re import findall, UNICODE

Processor = LastProcess()


class Controller:

    def __init__(self):
        self.DB_Root = None
        self.DB = AVL_Tree()
        self.LoadDB()
        self.LoadAccountDB()
        self.LoadProcessFromDB()

    def search(self, TC):
        result = self.DB.Search(TC, self.DB_Root)
        return result

    def AddUser(self, TC, first_name, last_name, password, phoneNum, momName):

        self.DB_Root = self.DB.Insert(self.DB_Root, TC, Customer(
            TC, first_name, last_name, password, phoneNum, momName))
        self.SaveToDb()

    def LoadDB(self):
        if path.exists("CustomersDB.json"):
            with open('CustomersDB.json', 'r', encoding='utf-8') as db:
                Customers = json.load(db)
                for client in Customers:
                    client = json.loads(client)
                    Tc = client['TC']
                    FirstName = client['Name']
                    LastName = client['Surname']
                    PhoneNum = client['phoneNum']
                    PhoneNum = int(PhoneNum)
                    LastNameofMom = client['momName']
                    Password = client['Password']
                    Password = int(Password)
                    self.AddUser(Tc, FirstName, LastName, Password,
                                 PhoneNum, LastNameofMom)

    def SaveToDb(self):
        _list = []
        accounts = []
        customers = self.DB.Read(self.DB_Root)
        for customer in customers:
            accounts.clear()
            for account in customer.Customer.Accounts:
                accounts.append(account)
            customer.Customer.Accounts.clear()
            _list.append(json.dumps(customer.Customer.__dict__))
            for account in accounts:
                customer.Customer.Accounts.append(account)

        with open("CustomersDB.json", 'w') as db:
            json.dump(_list, db)

    def SaveToDbAccount(self):
        _list = []
        roots = self.DB.Read(self.DB_Root)
        for root in roots:
            for acounts in root.Customer.Accounts:
                _list.append(json.dumps(acounts.__dict__))
        with open('CustomerAccountDb.json', 'w', encoding='utf-8') as dbAccount:
            json.dump(_list, dbAccount)

    def LoadAccountDB(self):
        if path.exists('CustomerAccountDb.json'):
            with open('CustomerAccountDb.json', 'r', encoding='utf-8') as dbAccount:
                Accounts = json.load(dbAccount)
                for account in Accounts:
                    Account = json.loads(account)
                    TC = Account['TC']
                    if self.search(TC):
                        Customer = self.search(TC)
                        Customer = Customer.Customer
                        Name = Account['Name']
                        Sum = Account['Sum']
                        if Name == 'MH':
                            Customer.Accounts.append(MH(Sum, TC))
                        if Name == 'VMH':
                            Customer.Accounts.append(VMH(Sum, TC))
                        if Name == 'AH':
                            Customer.Accounts.append(AH(Sum, TC))
                        if Name == 'VAH':
                            Customer.Accounts.append(VAH(Sum, TC))
                        if Name == 'YH':
                            kind = Account['Currency']
                            Customer.Accounts.append(YH(Sum, kind, TC))
                        if Name == 'VYH':
                            kind = Account['Currency']
                            Customer.Accounts.append(VYH(Sum, kind, TC))

    def SaveToProcess(self, TC, price, kind):
        if kind == 1:
            Processor.Remove(TC, price)
        elif kind == 2:
            Processor.Add(TC, price)
        self.SaveProcessToDB()

    def SaveProcessToDB(self):
        _Process = []
        for Process in Processor.ListOfDescription:
            _Process.append(json.dumps(Process))
        with open('CustomerLastProcess.json', 'w', encoding='utf-8') as dbProcess:
            json.dump(_Process, dbProcess)

    def LoadProcessFromDB(self):
        if path.exists('CustomerLastProcess.json'):
            with open('CustomerLastProcess.json', 'r', encoding='utf-8') as dbProcess:
                Processes = json.load(dbProcess)
                for process in Processes:
                    Processor.ListOfDescription.append(json.loads(process))

    def LastProcessOfCustomer(self, TC):
        for Description in Processor.ListOfDescription:
            Desc = Description.split('/')
            TC = str(TC)
            if TC == Desc[1].strip():
                print(Desc[0].strip())

    def deleteAccount(self, customer):
        self.DB_Root = self.DB.delete(self.DB_Root, customer.TC)

    def getCustomer(self, TC):
        customer = self.search(TC)
        if customer:
            customer = customer.Customer
        else:
            raise UnValidTC()
        return customer

    def ControlPass(self, customer, password):
        if customer.Password == int(password):
            return True
        else:
            raise UnValidPass()

    def SaveDB(self):
        self.SaveToDbAccount()
        self.SaveToDb()

    def String_Validation(self, string):
        valid = findall("[^a-z]", string, UNICODE)
        valid = valid.__str__()
        valid = valid.replace("[", "")
        valid = valid.replace("]", "")
        valid = valid.replace("\"", "")
        valid = valid.replace('\'', "")
        valid = valid.replace(",", "")
        valid = findall("[^A-Z]", valid, UNICODE)
        valid = valid.__str__()
        valid = valid.replace("[", "")
        valid = valid.replace("]", "")
        valid = valid.replace("\"", "")
        valid = valid.replace('\'', "")
        valid = valid.replace(",", "")
        valid = findall("[^üğişçöıİĞÇŞÖÜ ]", valid, UNICODE)
        if valid:
            raise UnValidString()

    def LenOfTC(self, TC):
        if len(TC) != 11:
            raise UnValidTC("TC 11 Haneli Olmalıdır")

    def ScanDB(self, TC):
        if self.search(TC):
            raise ExistingTC()

    def LenOfPass(self, Pass):
        if len(Pass) <= 0:
            raise UnValidPass()

    def LenOfThings(self, string):
        if len(string) <= 0:
            raise UnValidValue()


class UnValidString(Exception):
    def __init__(self, message="Geçersiz İfade girdiniz"):
        self.message = message
        super().__init__(self.message)


class UnValidTC(Exception):
    def __init__(self, message="Geçersiz TC"):
        self.message = message
        super().__init__(self.message)


class UnValidPass(Exception):
    def __init__(self, message="Geçersiz Şifre"):
        self.message = message
        super().__init__(self.message)


class UnValidAccount(Exception):
    def __init__(self, message="Geçersiz Hesap"):
        self.message = message
        super().__init__(self.message)


class ExistingTC(Exception):
    def __init__(self, message="TCniz sistemde Mevcut"):
        self.message = message
        super().__init__(self.message)


class UnValidValue(Exception):
    def __init__(self, message="Geçersiz deger"):
        self.message = message
        super().__init__(self.message)
