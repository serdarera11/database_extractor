import time

def simulate_hack():
    print("Bağlantı kuruluyor...")
    time.sleep(1)
    print("Veritabanı bağlantısı sağlandı...")
    time.sleep(1)
    print("Veriler çekiliyor...")
    time.sleep(1)
    print("Veritabanı .txt dosyasına kaydedildi: database.txt")
    time.sleep(1)
    print("\n\nVeri tabanı kaydedilde.")

def main():
    print("Veritabanını çekmek istediğiniz sitenin adını girin:")
    site = input("Site Adı: ")
    print(f"{site} veritabanı çekiliyor...")
    simulate_hack()
    
    with open("database.txt", "w") as file:
        file.write(f"Site: {site}\n")
        file.write("=" * 30 + "\n")
        file.write("Dosya başarı ile oluşturuldu!\n")

    print("database.txt oluşturuldu! Dosyayı açıp bakabilirsiniz.")

if _name_ == "_main_":
    main()
