AVL BANKA UYGULAMASI

uygulamanın arkaplanında müşterileri tutmak için avl ağaç yapısı kullanılmıştır.

CustomersDB -> Yeni eklenen Müşterilerde dahil olmak üzere müşteri bilgilerini tutar.
CustomerAccountDB -> Müşterilere ait hesapları tutar
CustomerLastProcess -> müşteriler arasında yapılan para transferlerinin geçmişini tutar.

Sistemde bulunan bir kullanıcı kullanıcı girişi yaptığında avl ağacının dengeli bts yapısı sayesinde 
en hızlı şekilde db de bulur ve gerekli bilgileri ekrana getirir.2^32 gibi yüklü bir kayıtı bile 
32 adımda bulabilir.Bir banka uygulamasında search ön planda olacağından veri yapımız avl ile tasarlanmıştır.

8 Tür Mevduat Hesabı bulunmaktadır.
Yeni hesap açabilir farklı kullanıcı hesaplarına para gönderimi yapabilir veya alabilirsiniz.
Güncel kur bilgilerini İnternet bağlantınız olması durumunda Alacak tüm yatırım hesaplarınızdaki usd ve euro miktarları
güncel kur ile hesaplanacak ,olmaması durumunda default değerleri alacaksınız.
Yapılan para transferi işlemlerinin size ait tüm geçmişini görebilirsiniz.
İstediğinizde Sistemden Hesabınızı silebilirsiniz.