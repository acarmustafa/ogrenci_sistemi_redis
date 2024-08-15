import redis
from datetime import datetime
r=redis.Redis(host='localhost',port=6379,db=0)
if r.ping():
    print("Redis bağlantısı başarılı.")
else:
    print("Redis bağlantısı başarısız.")
def sınıf_ekle(id,isim,kat):
    r.hset(f'sınıf:{id}',mapping={
        'isim':isim,
        'kat':kat
    }) 
    print(f'{id} numaralı id başarıyla eklendi.') 
def öğrenci_ekle(id,isim,soyisim,doğum_tarihi,cinsiyet,telefon,sınıf_id):
    r.hset(f'öğrenci:{id}', 'isim', isim)
    r.hset(f'öğrenci:{id}', 'soyisim', soyisim)
    r.hset(f'öğrenci:{id}', 'doğum_tarihi', doğum_tarihi)
    r.hset(f'öğrenci:{id}', 'cinsiyet', cinsiyet)
    r.hset(f'öğrenci:{id}', 'telefon', telefon)
    r.hset(f'öğrenci:{id}', 'sınıf_id', sınıf_id)
    print(f'{id} numaralı öğrenci başarıyla eklendi')
        
    
    print(f'{id} numaralı id başarıyla eklendi')

def branş_ekle(id,isim) :
    r.hset(f'branş:{id}',mapping={
        'isim':isim
    })   
    print(f'branş:{id} numaralı branş başarıyla eklendi.')
def hobi_ekle(id,isim):
    r.hset(f'hobi:{id}',mapping={
        'isim':isim
    }) 
    print(f'{id} numaralı hobi başarıyla eklendi')    

def öğretmen_ekle(id, isim, soyisim, branş_id, doğum_tarihi, cinsiyet, telefon):
    r.hset(f'öğretmen:{id}', 'isim', isim)
    r.hset(f'öğretmen:{id}', 'soyisim', soyisim)
    r.hset(f'öğretmen:{id}', 'branş_id', branş_id)
    r.hset(f'öğretmen:{id}', 'doğum_tarihi', doğum_tarihi)
    r.hset(f'öğretmen:{id}', 'cinsiyet', cinsiyet)
    r.hset(f'öğretmen:{id}', 'telefon', telefon)
    print(f'{id} numaralı öğretmen başarıyla eklendi') 
def öğrenci_getir(id):
    öğrenci=r.hgetall(f'öğrenci:{id}')
    if öğrenci:
        öğrenci={key.decode():value.decode() for key,value in öğrenci.items()}
        sınıf_id=öğrenci.get('sınıf_id')
        if sınıf_id:
          sınıf=r.hgetall(f'sınıf:{sınıf_id}')
          if sınıf :
            sınıf = {key.decode(): value.decode() for key, value in sınıf.items()}
            öğrenci['sınıf'] = sınıf
          else:
            print(f'{sınıf_id} isimli sınıf bulunamadı.') 
        else:
          print(f'{id} numaralı öğrenci bulunamadı.')
        return öğrenci
def branş_getir(id):
    branş=r.hgetall(f'branş:{id}')
    if branş:
        branş={key.decode():value.decode() for key,value in branş.items()}
        return branş
    else:
        print(f'{id} numaralı branş bulunamadı.') 
        return None           
    
def hobi_getir(id):
    hobi=r.hgetall(f'hobi:{id}')
    if hobi:
        hobi={key.decode():value.decode() for key,value in hobi.items()}
        return hobi
    else:
        print(f'{id} numaralı hobi bulunamadı.')
        return None
def sınıf_getir(id):
    sınıf=r.hgetall(f'sınıf:{id}')
    if sınıf:
        sınıf={key.decode():value.decode() for key,value in sınıf.items()}
        return sınıf
    else:
        print(f'{id} numaralı sınıf bulunamadı.')    
def öğretmen_getir(id):
    öğretmen=r.hgetall(f'öğretmen:{id}')
    if öğretmen:
        öğretmen={key.decode():value.decode() for key,value in öğretmen.items()}
        return öğretmen
    else:
        print(f'{id} numaralı öğretmen bulunamadı.')
def öğrenci_güncelle(id,isim=None,soyisim=None,doğum_tarihi=None,cinsiyet=None,telefon=None,sınıf_id=None):
    öğrenci=r.hgetall(f'öğrenci:{id}')
    if not öğrenci:
        print(f'{id} numaralı öğrenci bulunamadı.')
    if isim:
        r.hset(f'öğrenci:{id}','isim',isim)
    if soyisim:
        r.hset(f'öğrenci:{id}','soyisim',soyisim)
    if doğum_tarihi:
        r.hset(f'öğrenci:{id}','doğum_tarihi',doğum_tarihi)
    if cinsiyet:
        r.hset(f'öğrenci:{id}','cinsiyet',cinsiyet)
    if telefon:
        r.hset(f'öğrenci:{id}','telefon',telefon)
    if sınıf_id:
        r.hset(f'öğrenci:{id}','öğreci_id',sınıf_id)
    print(f'{id} numaralı öğrenci başarıyla güncellendi.') 
def branş_güncelle(id,isim=None):
    branş=r.hgetall(f'branş:{id}')                              
    if not branş:
        print(f'{id} numaralı branş bulunamadı.')
    if isim:
        r.hset(f'branş:{id}','isim',isim)
    else:
        print(f'{id} numaralı branş bulunamadı.')
def hobi_güncelle(id,isim=None):
    hobi=r.hgetall(f'hobi:{id}')
    if not hobi:
        print(f'{id} numaralı hobi bulunamadı') 
    if isim:
        r.hset(f'hobi:{id}','isim',isim)
    print(f'{id} nuamralı hobi başarıyla güncellendi.')
def öğretmen_güncelle(id,isim=None,soyisim=None,branş_id=None,doğum_tarihi=None,cinsiyet=None,telefon=None) :
    öğretmen=r.hgetall(f'öğretmen:{id}')
    if not öğretmen:
        print(f'{id} numaralı öğretmen bulunamadı')
    if isim:
        r.hset(f'öğretmen:{id}','isim',isim)
    if soyisim:
        r.hset(f'öğretmen:{id}','soyisim',soyisim)
    if branş_id:
        r.hset(f'öğretmen:{id}','branş_id',branş_id)
    if doğum_tarihi:
        r.hset(f'öğretmen:{id}','doğum_tarihi',doğum_tarihi)
    if cinsiyet:
        r.hset(f'öğretmen:{id}','cinsiyet',cinsiyet)
    if telefon:
        r.hset(f'öğretmen:{id}','telefon',telefon)
    print(f'{id} numaralı öğretmen başarıyla güncellendi.')
def sınıf_güncelle(id,isim=None,kat=None):
    sınıf=r.hgetall(f'sınıf:{id}')
    if not sınıf:
        print(f'{id} numaralı sınıf bulunamadı.')
    if isim:
        r.hset(f'sınıf:{id}','isim',isim)
    if kat:
        r.hset(f'sınıf:{id}','kat',kat)    
    print(f'{id} numaralı sınıf başarıyla güncellendi.')            
def öğrenci_sil(id):
    öğrenci=r.exists(f'öğrenci:{id}')
    if not öğrenci:
        print(f'{id} numaralı öğrenci bulunamadı.')
    r.delete(f'öğrenci:{id}')
    print(f'{id} numaralı öğrenci başarıyla silindi.')     
                                                  
def sınıf_sil(id):
    sınıf=r.exists(f'sınıf:{id}')  
    if not sınıf:
        print(f'{id} numaralı sınıf bulunamadı.')
    r.delete(f'sınıf:{id}')
    print(f'{id} numaralı sınıf başarıyla silindi.') 
def öğretmen_sil(id):
    öğretmen=r.exists(f'öğretmen:{id}')
    if not öğretmen:
        print(f'{id} numaralı öğretmen bulunamadı.')
    r.delete(f'öğretmen:{id}')
    print(f'{id} numaralı öğretmen başarıyla silindi.')                         
def hobi_sil(id):
    hobi=r.exists(f'hobi:{id}')
    if not hobi:
        print(f'{id} numaralı hobi bulunamadı.')
    r.delete(f'hobi:{id}')
    print(f'{id} numaralı hobi başarıyla silindi.')
def branş_sil(id):
    branş=r.exists(f'branş:{id}')
    if not branş:
        print(f'{id} numaralı branş bulunamadı.')
    r.delete(f'branş:{id}')
    print(f'{id} numaralı hobi başarıyla silindi.')  


def menu():
    print('Hoşgeldiniz, seçiminizi yapınız:')
    print('1 - Yeni kayıt ekle')
    print('2 - Kayıt güncelleme')
    print('3 - Kayıt silme')
    print('4 - Kayıtları listeleme')
    print('5 - sınıf bilgisi ve doğum tarihi alınarak belirtilen tarihten  önce ve sonra doğanlar')
    print('6 - İsmi girilen öğrencinin hangi katta olduğu ')
    print('7 - Öğrenciye yeni hobi ekle: ')  
    print('0-  Çıkış')                       

def insert_case():
    print('Öğrenci için: ')
    print('Eklemek istemiyorsanız q tuşuna basın.')
    id = input("Öğrenci ID'sini girin: ") 
    if id=='q':
        pass
    else:
        isim = input("Öğrenci ismini girin: ")
        soyisim = input("Öğrenci soyismini girin: ")
        doğum_tarihi = input("Doğum tarihini girin (YYYY-AA-GG): ")
        cinsiyet = input("Cinsiyetini girin: ")
        telefon = input("Telefon numarasını girin: ")
        sınıf_id = input("Sınıf ID'sini girin: ")
        öğrenci_ekle(id, isim, soyisim, doğum_tarihi, cinsiyet, telefon, sınıf_id)
    print('Branş için: ')
    print('Eklemek istemiyorsanız q tuşuna basın.')
    id=input("Branş ID'sini girin:")
    if id=='q':
        pass    
    else:
        isim=input('Branş ismini girin: ')
        branş_ekle(id,isim)
    print('Öğretmen için: ')
    print('Eklemek istemiyorsanız q tuşuna basın.')
    id=input("Öğretmen ID'sini girin:")
    if id=='q':
        pass
    else:
        isim=input('İsmini girin: ')
        soyisim=input('Soyismini girin: ')
        branş_id=input('Branş_id girin: ')
        doğum_tarihi = input("Doğum tarihini girin (YYYY-AA-GG): ")
        cinsiyet=input('Cinsiyetini girin: ')
        telefon = input("Telefon numarasını girin: ")
        öğretmen_ekle(id,isim,soyisim,branş_id,doğum_tarihi,cinsiyet,telefon)
    print('Hobi için: ') 
    print('Eklemek istemiyorsanız q tuşuna basın.')
    id=input('Hobi ID girin: ')
    if id=='q':
        pass   
    else:
        isim=input('İsmini girin: ') 
        hobi_ekle(id,isim)
    print('Sınıf için') 
    print('Eklemek istemiyorsanız q tuşuna basın.')
    id=input('Sınıf ID girin: ')
    if id=='q':
        pass
    else:
        isim=input('İsmini girin: ')
        kat=input('KAT: ') 
    sınıf_ekle(id,isim,kat) 
def update_case():
    print('Öğrenci için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    id=input('Öğrenci ID girin: ') 
    if id =='q':
        pass
    else:
        isim=input('ISIM: ') 
        soyisim=input('SOYISIM: ') 
        doğum_tarihi=input('DOĞUM TARIHI: ')
        cinsiyet= input('CINSIYET: ')
        telefon=input('TELEFON: ')
        sınıf_id=input('SINIF_ID: ')
        öğrenci_güncelle(id,isim,soyisim,doğum_tarihi,cinsiyet,telefon,sınıf_id)
    print('Sınıf için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    id=input('Sınıf ID girin: ') 
    if id=='q':
        pass
    else:
        isim=input('ISIM: ')
        kat=input('KAT: ')  
        sınıf_güncelle(id,isim,kat)
    print('Branş için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    id=input('Branş ID girin: ') 
    if id=='q':
        pass
    else:
        isim=input('ISIM: ')  
        branş_güncelle(id,isim)
    print('Hobi için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    id=input('Hobi ID girin: ')
    if id=='q':
        pass
    else: 
        isim=input('ISIM: ') 
        hobi_güncelle(id,isim) 
    print('Öğretmen için')
    print('Güncellemek istemiyorsanız q tuşuna basın.')
    id=input('Öğretmen ID girin: ') 
    if id=='q':
        pass
    else:
        isim=input('ISIM: ')  
        soyisim=input('SOYISIM: ')
        branş_id=input('BRANS_ID: ') 
        doğum_tarihi=input('DOGUM_TARIHI: ')
        cinsiyet=input('CINSIYET: ')
        telefon=input('TELEFON: ')
        öğretmen_güncelle(id,isim,soyisim,branş_id,doğum_tarihi,cinsiyet,telefon) 
def delete_case(): 
    print('Öğrenci için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    id = input("Öğrenci ID'sini girin: ") 
    if id=='q':
        pass 
    else:
        öğrenci_sil(id)
    print('Sınıf için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    id = input("Sınıf ID'sini girin: ") 
    if id=='q':
        pass
    else:
        sınıf_sil(id)
    print('Branş için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    id = input("Branş ID'sini girin: ") 
    if id=='q':
        pass 
    else:
        branş_sil(id)
    print('Hobi için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    id = input("Hobi ID'sini girin: ") 
    if id=='q':
        pass
    else:
        hobi_sil(id)  
    print('Öğretmen için: ')
    print('Silmek istemiyorsanız q tuşuna basın.')
    id = input("Öğretmen ID'sini girin: ") 
    if id=='q':
        pass
    else:
        öğretmen_sil(id) 
def list_case():
    def listele(prefix):
        anahtarlar=r.keys(f'{prefix}:*')
        if not anahtarlar:
            print(f'{prefix} bulunamadı.')
            return
        for anahtar in anahtarlar:
            kayıt=r.hgetall(anahtar)
            kayıt={key.decode():value.decode() for key,value in kayıt.items()}
            print(f"{prefix.capitalize()} ID: {anahtar.decode().split(':')[1]}")
            print(kayıt)
            print('-' * 30)
    listele('öğrenci')
    listele('sınıf')
    listele('branş')
    listele('hobi')
    listele('öğretmen')                         
def filter_by_class_and_birth():
    sınıf_id=input('Sınıf bilgisini giriniz: ')
    tarih=input('Doğum yılını giriniz:')
     
     
    try:
        verilen_tarih=datetime.strptime(tarih, '%Y-%m-%d')  
        anahtarlar=r.keys('öğrenci:*')
        önce_doğanlar=[]
        sonra_doğanlar=[]
        for anahtar in anahtarlar:
            öğrenci=r.hgetall(anahtar)
            öğrenci={key.decode(): value.decode() for key,value in öğrenci.items()}
            if öğrenci.get('sınıf_id')==sınıf_id:
                doğum_tarihi=datetime.strptime(öğrenci.get('doğum_tarihi'), '%Y-%m-%d')
                if doğum_tarihi<verilen_tarih:
                    önce_doğanlar.append(öğrenci)
                else:
                    sonra_doğanlar.append(öğrenci)   
        print(f"\n{tarih} tarihinden ÖNCE doğan öğrenciler:")
        for öğrenci in önce_doğanlar:
            print(öğrenci)

        print(f"\n{tarih} tarihinden SONRA doğan öğrenciler:")
        for öğrenci in sonra_doğanlar:
            print(öğrenci)
    except ValueError as e:
        print(f'Tarih format hatası: {e}')
def find_floor():
    isim=input('öğrencinin ismini girin: ')
    anahtarlar=r.keys('öğrenci:*')
    for anahtar in anahtarlar:
        öğrenci=r.hgetall(anahtar)
        öğrenci={key.decode():value.decode() for key,value in öğrenci.items()}
        if öğrenci.get('isim')==isim:
            sınıf_id=öğrenci.get('sınıf_id')
            if sınıf_id:
                sınıf=r.hgetall(f'sınıf:{sınıf_id}')
                sınıf={key.decode():value.decode() for key,value in sınıf.items()}
                kat=sınıf.get('kat')
                if kat:
                    print(f"{isim} adlı öğrenci {kat}. katta.")
                else:
                    print(f"{isim} adlı öğrencinin kat bilgisi bulunamadı.")
                return
        else:
            print(f'{isim} isimli öğrenci bulunamadı') 
def add_hobbies_to_student():
    öğrenci_id=input('Öğrenci ID girin: ') 
    hobi_id=input('Hobi ID  girin: ') 
    öğrenci=r.hgetall(f'öğrenci:{öğrenci_id}') 
    hobi=r.hgetall(f'öğrenci:{hobi_id}') 
    if not öğrenci:
        print(f'{öğrenci_id} numaralı öğrenci bulunamadı.')  
        return
    if not hobi:
        print(f'{hobi_id} numaralı hobi bulunamadı.')  
    mevcut_hobiler=r.smembers(f'öğrenci_hobileri:{öğrenci_id}')
    if hobi_id.encode() in mevcut_hobiler:
        print(f'{hobi_id} numaralı öğrenci zaten öğrenciye eklenmiş.')
    else:
        r.sadd(f'öğrenci_hobileri:{öğrenci_id}', hobi_id)
        print(f'{öğrenci_id} numaralı öğrenciye {hobi_id} numaralı hobi başarıyla eklendi.')    
        
                 
            
     
                                            
          
                  
         
switch={
    '1':insert_case,
    '2':update_case,
    '3':delete_case,
    '4':list_case,
    '5':filter_by_class_and_birth,
    '6':find_floor,
    '7':add_hobbies_to_student
}
    
while True:
    
    menu()
    seçim = input("Lütfen seçiminizi yapın: ")
    
    
    action = switch.get(seçim)
    if action:
        if seçim == '0':  
            if not action():
                break
        else:
            action()
    else:
        print("Geçersiz seçim, lütfen tekrar deneyin.")




        
 

   