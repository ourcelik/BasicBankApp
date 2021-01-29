from Controller import Controller, UnValidString, UnValidTC, UnValidPass, UnValidAccount, ExistingTC, UnValidValue
from Account import MH, VMH, AH, VAH, YH, VYH
from os import sep, system
from time import sleep
from Account import Gold, Dollar, Euro
Admin = Controller()


class MainUserI():
    def __init__(self):
        self.InitUI()

    def ValidCustomer(self):
        system('cls')
        while True:
            try:
                TC = input("TC'nizi Giriniz:")
                Admin.LenOfTC(TC)
                TC = int(TC)
                Admin.ScanDB(TC)
                self.AddUser(TC)
                break
            except ValueError:
                print('Geçersiz Tuşlama Yaptınız,Tekrar Deneyin')
                sleep(1)
                system("cls")
            except UnValidTC as message:
                print(message)
                sleep(1)
                system("cls")
            except ExistingTC as message:
                print(message)
                sleep(1)
                system("cls")
                self.InitUI()

    def InitUI(self):
        system('cls')
        Title = "OnurBank İnternet Bankacılığı".center(100, '-')
        print(Title, '\n')
        print("1-Yeni Müşteri Girişi".center(100))
        print("2-Mevcut Müşteri Girişi".center(100))
        print("3.Hakkımızda".center(100))
        print("4-Çıkış".center(100))
        chose = input("yapmak istediğiniz işlemi seçiniz:")
        try:
            chose = int(chose)
        except ValueError:
            print("Hatalı girdi!")
            sleep(0.5)
            self.InitUI()

        while True:
            if chose == 1:
                self.ValidCustomer()
                break
            elif chose == 2:
                self.Login()
                break
            elif chose == 3:
                self.Info()
                break
            elif chose == 4:
                self.Exit()
            else:
                print("hatalı seçim tekrar seçiniz!")
                sleep(0.3)
                self.InitUI()

    def AddUser(self, TC):
        try:
            FirstName = input("İsminizi Giriniz : ")
            Admin.String_Validation(FirstName)
            LastName = input("Soyadınızı giriniz : ")
            Admin.String_Validation(LastName)
            PhoneNum = input("Telefon Numaranızı giriniz : ")
            PhoneNum = int(PhoneNum)
            LastNameofMom = input("Anne Kızlık Soyadınız : ")
            Admin.String_Validation(LastNameofMom)
            Password = input("Şifre giriniz : ")
            Password = int(Password)
            Admin.AddUser(TC, FirstName, LastName, Password,
                          PhoneNum, LastNameofMom)
            customer = Admin.getCustomer(TC)
            self.AccountDetail(customer)
        except UnValidString as message:
            print(message)
            sleep(1)
            system("cls")
            self.InitUI()

    def Login(self):
        system('cls')
        while True:
            try:
                TC = input('TC\'nizi giriniz : ')
                Password = input("Şifrenizi Giriniz : ")
                Admin.LenOfPass(Password)
                customer = Admin.getCustomer(int(TC))
                if Admin.ControlPass(customer, Password):
                    self.AccountDetail(customer)
                    break
            except UnValidTC as message:
                print(message)
            except UnValidPass as message:
                print(message)

    def Exit(self):
        system('cls')
        Admin.SaveToDbAccount()
        Admin.SaveToDb()
        quit()

    def Info(self):
        print("Info Area")

    def AccountDetail(self, customer):
        sumoflist = self.SumOfOne(customer)
        system('cls')
        print(
            f'Hoşgeldin {customer.Name} {customer.Surname} '.title().center(100))
        print('Varlıklar -> '.title().center(100), end='')
        self.Sum(customer)
        print('Vadesiz Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[0][0], 'TL')
        print('Vadeli Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[0][1], 'TL')
        print('1-Detay : '.title().center(100))
        print('2-Ayarlar : '.title().center(100))
        print('3-Çıkış Yap'.title().center(100))
        chose = input('Secim Yapabilirsiniz : ')
        while True:
            if chose == '1':
                self.Detail(customer)
                break
            if chose == '2':
                self.Settings(customer)
                break
            if chose == '3':
                self.Exit()
            else:
                print(
                    'Gecersiz Secim yaptınız,Lütfen Tekrar Deneyiniz.'.title().center(100))
                chose = input('Tekrar Secim Yapın:')
        Admin.SaveDB()

    def Detail(self, customer):
        system('cls')
        print("1-hesap bilgileriniz : ".title().center(100))
        print('2-yeni hesap aç : '.title().center(100))
        print('3-Müşteri Temsilcin : '.title().center(100))
        print('4-Kur Bilgileri : '.title().center(100))
        print('5-Son işlemler : '.title().center(100))
        print('6-Para Transferi : '.title().center(100))
        print('7-created by : '.title().center(100))
        print('8-Çıkış Yap'.title().center(100))

        while True:
            secim = input(
                "İlerlemek istediğiniz Alanı Seçiniz:")
            if secim == '1':
                self.AccountInfo(customer)
                break
            elif secim == '2':
                self.NewAccount(customer)
                break
            elif secim == '3':
                self.Account_Executive(customer)
                break
            elif secim == '4':
                self.Investing(customer)
                break
            elif secim == '5':
                self.LastTransaction(customer)
                break
            elif secim == '6':
                self.Transfer(customer)
                break
            elif secim == '7':
                self.CreatedBy(customer)
                break
            elif secim == '8':
                self.Exit()
            else:
                print("hatalı girdi")

    def Settings(self, customer):
        print('1-Hesabımı Sil')
        print('2-Menüye Dön')
        while True:
            option = input('Seçiminizi yapın : ')
            if option == '1':
                self.Delete_Account(customer)
            elif option == '2':
                self.AccountDetail(customer)
                break
            else:
                print("hatalı girdi")

    def Sum(self, customer):
        Sum = 0
        for account in customer.Accounts:
            type(account) is MH or type(account) is VMH
            Sum += account.Sum
        print(Sum)

    def SumOfOne(self, customer):
        mh = 0
        vmh = 0
        ah = 0
        vah = 0
        yh = 0
        vyh = 0
        yhd = 0
        vyhd = 0
        for account in customer.Accounts:
            if type(account) is MH:
                mh += account.Sum
            elif type(account) is VMH:
                vmh += account.Sum
            elif type(account) is AH:
                ah += account.Gold
            elif type(account) is VAH:
                vah += account.Gold
            elif type(account) is YH:
                if account.Currency == 'USD':
                    yhd += account.Invest
                else:
                    yh += account.Invest
            elif type(account) is VYH:
                if account.Currency == 'USD':
                    vyhd += account.Invest
                else:
                    vyh += account.Invest
        listyh = [yhd, yh]
        listvyh = [vyhd, vyh]
        _list = [mh, vmh, ah, vah]
        listsum = [_list, listyh, listvyh]
        return listsum

    def AccountInfo(self, customer):
        system('cls')
        Name = customer.Name
        Surname = customer.Surname
        Tc = customer.TC
        PhoneNum = customer.phoneNum
        Mom = customer.momName
        print(f'\n İsim : {Name} \n Soyad : {Surname} \n TC : {Tc} \n TelNo: {PhoneNum} \n AnneAdı : {Mom} '.title(
        ).center(100))
        sumoflist = self.SumOfOne(customer)
        print('Varlıklar -> '.title().center(100), end='')
        self.Sum(customer)
        print('Vadesiz Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[0][0], 'TL')
        print('Vadeli Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[0][1], 'TL')
        print('Vadesiz Altın Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[0][2], 'Gram Altın')
        print('Vadeli Altın Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[0][3], 'Gram Altın')
        print('Vadesiz Dolar Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[1][0], 'Dolar ')
        print('Vadeli Dolar Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[2][0], 'Dolar ')
        print('Vadesiz Euro Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[1][1], 'Euro')
        print('Vadeli Euro Hesap Bakiyeniz -> '.title().center(100), end='')
        print(sumoflist[2][1], ' Euro')
        while True:
            menu = input('Anamenüye Dönmek için 0 ı tuşlayınız : ')
            if menu == '0':
                self.Detail(customer)
            else:
                print("hatalı girdi")

    def NewAccount(self, customer):
        system('cls')
        print('1-Mevduat Hesabı Aç')
        print('2-Altın Hesabı Aç')
        print('3-Yatırım Hesabı Aç')
        while True:
            newAccount = input('Hesap Türünü Seçiniz:')
            if newAccount == '1':
                self.TLAccount(customer)
            elif newAccount == '2':
                self.GoldAccount(customer)
            elif newAccount == '3':
                self.InvestAccount(customer)
            else:
                print('hatalı tuşlama')

    def TLAccount(self, customer):
        system('cls')
        print('1-Vadesiz Mevduat Hesabı')
        print('2-Vadeli Mevduat Hesabı')
        kind = input('Seçiniz:')
        if kind == '1':
            invest = input('Ne kadar Yatırmak İstersiniz : ')
            invest = int(invest)
            customer.Accounts.append(MH(invest, customer.TC))
        elif kind == '2':
            invest = input('Ne kadar Yatırmak İstersiniz : ')
            invest = int(invest)
            customer.Accounts.append(VMH(invest, customer.TC))
        else:
            print('hatalı tuşlama')
        print('Ana Menüye Yönlendiriliyorsunuz')
        sleep(2)
        Admin.SaveToDbAccount()
        self.Detail(customer)

    def GoldAccount(self, customer):
        system('cls')
        print('1-Vadesiz Altın Hesabı')
        print('2-Vadeli Altın Hesabı')
        kind = input('Seçiniz:')
        if kind == '1':
            invest = input('Ne kadar Yatırmak İstersiniz : ')
            invest = int(invest)
            customer.Accounts.append(AH(invest, customer.TC))
        elif kind == '2':
            invest = input('Ne kadar Yatırmak İstersiniz : ')
            invest = int(invest)
            customer.Accounts.append(VAH(invest, customer.TC))
        else:
            print('hatalı tuşlama')
        print('Ana Menüye Yönlendiriliyorsunuz')
        sleep(2)
        Admin.SaveToDbAccount()
        self.Detail(customer)

    def InvestAccount(self, customer):
        system('cls')
        print('1-Vadesiz Yatırım Hesabı')
        print('2-Vadeli Yatırım Hesabı')
        kind = input('Seçiniz:')
        if kind == '1':
            invest = input('Ne kadar Yatırmak İstersiniz : ')
            invest = int(invest)
            while True:
                print('1-USD 2-EURO')
                kind = input('Yatırım Hesabı Kurunuzu seçiniz : ')
                if kind == '1':
                    kind = 'USD'
                    break
                elif kind == '2':
                    kind = 'EURO'
                    break
                else:
                    print('hatalı tuşlama tekrar deneyiniz:')
            customer.Accounts.append(YH(invest, kind, customer.TC))
        elif kind == '2':
            invest = input('Ne kadar Yatırmak İstersiniz : ')
            invest = int(invest)
            while True:
                print('1-USD 2-EURO')
                kind = input('Yatırım Hesabı Kurunuzu seçiniz : ')
                if kind == '1':
                    kind = 'USD'
                    break
                elif kind == '2':
                    kind = 'EURO'
                    break
                else:
                    print('hatalı tuşlama tekrar deneyiniz:')
            customer.Accounts.append(VYH(invest, kind, customer.TC))
        else:
            print('hatalı tuşlama')
        print('Ana Menüye Yönlendiriliyorsunuz')
        sleep(2)
        Admin.SaveToDbAccount()
        self.Detail(customer)

    def Investing(self, customer):
        system('cls')
        print(f'Dolar : {Dollar} '.title().center(100))
        print(f'Euro : {Euro} '.title().center(100))
        print(f'Altın : {Gold} '.title().center(100))
        enter = input('Ana Menüye dönmek için 0\'ı tuşayınız:')
        if enter == '0':
            self.Detail(customer)
        else:
            self.Detail(customer)

    def LastTransaction(self, customer):
        system('cls')
        print("Bu alanda EFT transfer geçmişinizi görebilirsiniz".title().center(50, "-"))
        Admin.LastProcessOfCustomer(customer.TC)
        enter = input('Ana Menüye dönmek için 0\'ı tuşayınız:')
        if enter == '0':
            self.Detail(customer)
        else:
            self.Detail(customer)

    def Transfer(self, customer):
        try:
            system('cls')
            ValidAc = []
            accountofOther = []
            accountsofCustomer = []
            print('1-Mevduat Hesabı ')
            print('2-Vadeli Mevduat Hesabı ')
            print('3-Altın Hesabı ')
            print('4-Vadeli Altın Hesabı ')
            print('5-Yatırım Hesabı ')
            print('6-Vadeli Yatırım Hesabı ')
            option = input('İşlem Yapmak İstediğiniz Hesap Türünü Seçiniz:')
            accountsofCustomer, option = self.ChosenAccounts(customer, option)
            count = input('Miktar giriniz:')
            Admin.LenOfThings(count)
            count = int(count)
            ValidAc, q = self.EnoughMoney(accountsofCustomer, count)
            if not ValidAc:
                raise UnValidAccount(
                    "Hesaplarınız Bu işlem için Yeterli Mevduata sahip değil")
            _currentAccount = input(
                'Lütfen Hangi Hesabı Kullanmak İstediğinizi seçiniz : ')
            Admin.LenOfThings(_currentAccount)
            _currentAccount = int(_currentAccount)
            if not _currentAccount >= 1 or not _currentAccount < q:
                raise UnValidAccount()
            currentAccount = ValidAc[_currentAccount-1]
            print(f'seçili hesap bakiyeniz : {currentAccount.Sum} ')
            TC = input(
                'Transfer Yapmak istediğiniz kişinin TC\'sini giriniz : ')
            Admin.LenOfTC(TC)
            TC = int(TC)
            Customer = Admin.search(TC)
            if Customer and Customer.TC != customer.TC:
                accountofOther, i = self.TargetAccount(TC, option)
                if not accountofOther:
                    raise UnValidAccount(
                        "Bu tür Hesabı Bulunmamaktadır")
                _currentOther = input(
                    'Gönderim Yapmak istediğiniz Hesabı Seçiniz:')
                Admin.LenOfThings(_currentOther)
                _currentOther = int(_currentOther)
                if not _currentOther >= 1 or not _currentOther < i:
                    raise UnValidAccount()
                currentOther = accountofOther[_currentOther-1]
                currentAccount.Sum -= count
                currentOther.Sum += count
                currentAccount.Update()
                currentOther.Update()
                Admin.SaveToProcess(
                    currentAccount.TC, count, 1)
                Admin.SaveToProcess(currentOther.TC, count, 2)
                print(
                    f'İşleminiz Gerçekleştirilmiştir güncel hesap bakiyeniz : {currentAccount.Sum} ')
                ValidAc.clear()
                accountsofCustomer.clear()
                accountofOther.clear()
                sleep(2)
                print('Anamenüye Yönlendiriliyorsunuz...')
                sleep(1)
                self.Detail(customer)
            elif Customer and Customer.TC == customer.TC:
                raise UnValidAccount(
                    "Kendine Para Gönderemezsin Seni AnaMenüye yönlendiriyorum")
            elif not Customer:
                raise UnValidTC("TC sistemde bulunamadı")
            else:
                raise UnValidAccount("Birşeyleri Yanlış yaptınız")
        except UnValidAccount as message:
            print(message)
            sleep(1)
            self.Detail(customer)
        except UnValidTC as message:
            print(message)
            sleep(1)
            self.Detail(customer)
        except UnValidValue as message:
            print(message)
            sleep(1)
            self.Detail(customer)

    def CreatedBy(self, customer):
        system('cls')
        print('-'.center(50, '-'))
        print('Bu Uygulama Onur Çelik Tarafından Oluşturuldu.')
        print('instagram,github : @ourcelik')
        print('-'.center(50, '-'))
        while True:
            main = input('Ana Menüye Dönmek için 0 ı tuşlayın')
            if main == '0':
                self.Detail(customer)
                break
            else:
                print('Hatalı girdi!:')

    def Account_Executive(self, customer):
        system('cls')
        print('Müşteri Temsilcisi Bilgileri:'.title().center(100))
        print('Ad-Soyad -> Onur Çelik'.title().center(100))
        print('TelNo -> 05423279899'.title().center(100))
        print('Mail -> ourcelik@icloud.com'.title().center(100))

        while True:
            Main = input('AnaMenüye Dönmek için 0 \'ı tuşlayınız')
            if Main == '0':
                self.Detail(customer)
                break
            else:
                print('hatalı Tuşlama Yaptınız Tekrar Deneyin:')

    def Delete_Account(self, customer):
        Admin.deleteAccount(customer)
        Admin.SaveDB()
        quit()

    def CustomerAccounts(self, customer, kind):
        accountofCustomer = []
        for account in customer.Accounts:
            if account.Name == kind:
                option = account.Name
                accountofCustomer.append(account)
        if not accountofCustomer:
            print('Bu Türden Bir Hesabınız Bulunmamaktadır.')
            print('Ana Menüye Yönlendiriliyorsunuz...')
            sleep(2)
            self.Detail(customer)
            return 0
        return accountofCustomer

    def EnoughMoney(self, accountsofCustomer, count):
        ValidAc = []
        q = 1
        for account in accountsofCustomer:
            if count < account.Sum:
                ValidAc.append(account)
                print(f'{q}.hesap bakiyesi = {account.Sum} ')
                q += 1
        return ValidAc, q

    def TargetAccount(self, TC, option):
        i = 1
        accountofOther = []
        Customer = Admin.search(TC)
        for account in Customer.Customer.Accounts:

            if account.Name == 'MH' and option == 'MH':
                accountofOther.append(account)
                print(f' {i} - Mevduat Hesabı {i}')
                i += 1
            if account.Name == 'VMH' and option == 'VMH':
                accountofOther.append(account)
                i += 1
                print(f' {i} - Vadeli Mevduat Hesabı {i} ')
            if account.Name == 'AH' and option == 'AH':
                accountofOther.append(account)
                print(f' {i} - Altın Hesabı {i}')
                i += 1
            if account.Name == 'VAH' and option == 'VAH':
                accountofOther.append(account)
                print(f' {i} - Vadeli Altın Hesabı {i}')
                i += 1
            if account.Name == 'YH' and option == 'YH':
                accountofOther.append(account)
                print(f' {i} - Yatırım Hesabı {i}')
                i += 1
            if account.Name == 'VYH' and option == 'VYH':
                accountofOther.append(account)
                print(f' {i} - Vadeli Yatırım Hesabı {i}')
                i += 1
        return accountofOther, i

    def ChosenAccounts(self, customer, option):
        accountsofCustomer = []
        if option == '1':
            accountsofCustomer = self.CustomerAccounts(customer, "MH")
            option = "MH"
        elif option == '2':
            accountsofCustomer = self.CustomerAccounts(customer, "VMH")
            option = "VMH"
        elif option == '3':
            accountsofCustomer = self.CustomerAccounts(customer, "AH")
            option = "AH"
        elif option == '4':
            accountsofCustomer = self.CustomerAccounts(customer, "VAH")
            option = "VAH"
        elif option == '5':
            accountsofCustomer = self.CustomerAccounts(customer, "YH")
            option = "YH"
        elif option == '6':
            accountsofCustomer = self.CustomerAccounts(customer, "VYH")
            option = "VYH"
        else:
            raise UnValidValue("gecersiz girdi")
        return accountsofCustomer, option


bnk = MainUserI()
