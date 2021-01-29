import requests
import json
from time import sleep
Dollar = 0
Euro = 0
Gold = 447
try:
    url = "https://api.exchangeratesapi.io/latest?base=TRY&symbols=USD,EUR"
    url = requests.get(url)
    url = json.loads(url.text)
    url = url['rates']
    Dollar = url['USD']
    Euro = url['EUR']
except requests.exceptions.ConnectionError:
    Dollar = 0.127
    Euro = 0.100


class Customer():
    def __init__(self,  TC, first_name, last_name, password, phoneNum, momName):
        self.Name = first_name
        self.Surname = last_name
        self.Accounts = list()
        self.TC = TC
        self.Password = password
        self.phoneNum = phoneNum
        self.momName = momName


class MH():
    def __init__(self, sum, TC):
        self.Name = 'MH'
        self.TC = TC
        self.Sum = int(sum)
        self.Currency = "TL"
        self.Created()

    def Created(self):
        print(
            f'Hesabınız Açılmıştır. Hesap Bakiye Tutarı : {self.Sum} {self.Currency} ')

    def Update(self):
        self.Sum = self.Sum


class VMH(MH):
    def __init__(self, sum, TC):
        super(VMH, self).__init__(sum, TC)
        self.Name = 'VMH'
        self.Rate_Interest = 0.10
        self.Interest()

    def Interest(self):
        self.Sum = self.Sum * (1+self.Rate_Interest)
        print(
            f'İlk Yıl Faiz Ödeneğiniz Kampanyamız Dahilinde Yapılmıştır.Faiz İle Beraber Yeni Para Tutarınız -> {self.Sum} {self.Currency} ')

    def Update(self):
        self.Sum = self.Sum


class AH():
    def __init__(self, sum, TC):
        self.Name = 'AH'
        self.TC = TC
        self.Sum = sum
        self.Gold = int(sum)/Gold
        self.Currency = "Gram Altın"
        self.Created()

    def Created(self):
        print(
            f'Hesabınız Açılmıştır. Hesap Bakiye Tutarı : {self.Gold} {self.Currency} ')

    def Update(self):
        self.Gold = self.Sum/Gold


class VAH(AH):
    def __init__(self, sum, TC):
        super(VAH, self).__init__(sum, TC)
        self.Name = 'VAH'
        self.Rate_Interest = 0.10
        self.Interest()

    def Interest(self):
        self.Sum = self.Sum * (1+self.Rate_Interest)
        self.Gold = self.Sum/Gold
        print(
            f'İlk Yıl Faiz Ödeneğiniz Kampanyamız Dahilinde Yapılmıştır.Faiz İle Beraber Yeni Para Tutarınız -> {self.Gold} {self.Currency} ')

    def Update(self):
        self.Gold = self.Sum/Gold


class YH():
    def __init__(self, sum, kind, TC):
        self.Name = 'YH'
        self.TC = TC
        self.Currency = str(kind)
        if kind == 'EURO':
            self.Sum = int(sum)
            self.Invest = self.Sum*Euro
        elif kind == 'USD':
            self.Sum = int(sum)
            self.Invest = int(sum)*Dollar
        self.Created()

    def Created(self):
        print(
            f'Hesabınız Açılmıştır. Hesap Bakiye Tutarı : {self.Invest} {self.Currency} ')

    def Update(self):
        if self.Currency == 'EURO':
            self.Invest = self.Sum*Euro
        elif self.Currency == 'USD':
            self.Invest = self.Sum*Dollar


class VYH(YH):
    def __init__(self, sum, kind, TC):
        super(VYH, self).__init__(sum, kind, TC)
        self.Name = 'VYH'
        self.Rate_Interest = 0.10
        self.Interest()

    def Interest(self):
        self.Sum += self.Sum * self.Rate_Interest
        print(
            f'İlk Yıl Faiz Ödeneğiniz Kampanyamız Dahilinde Yapılmıştır.Faiz İle Beraber Yeni Para Tutarınız -> {self.Invest} {self.Currency} ')

    def Update(self):
        self.Sum += self.Sum*self.Rate_Interest


class LastProcess:

    def __init__(self):
        self.ListOfDescription = []

    def Add(self, TC, price):
        TC = TC
        description = f'Hesabınıza {price} \' lık bir aktarım yapılmıştır. / {TC} '
        self.ListOfDescription.append(description)

    def Remove(self, TC, price):
        TC = TC
        description = f'Hesabınızdan {price} \' lık çekim gerçekleştirilmiştir./ {TC} '
        self.ListOfDescription.append(description)
