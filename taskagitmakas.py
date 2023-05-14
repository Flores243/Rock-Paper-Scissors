import random

def kazananı_belirle(user_turn, computer_turn):
    if user_turn == computer_turn:
        return "berabere"
    elif (user_turn == "taş" and computer_turn == "makas") or \
         (user_turn == "makas" and computer_turn == "kağıt") or \
         (user_turn == "kağıt" and computer_turn == "taş"):
        return "oyuncu"
    else:
        return "bilgisayar"

def hamleleri_yazdır(user_turn, computer_turn):
    print("Oyuncu hamlesi:", user_turn)
    print("Bilgisayar hamlesi:", computer_turn)
    print()

def sonucu_yaz(kazanan):
    if kazanan == "berabere":
        print("Berabere!")
    else:
        print(kazanan.capitalize(), "kazandı!")

def tekrar_oyna():
    tercih = input("Tekrar oynamak istiyor musun? (y/n) ").lower()
    return tercih == "y"

while True:
    print("Taş, Kağıt, Makas oyununa hoş geldin!")
    print("Hamleni yap: taş, kağıt veya makas.")
    user_turn = input().lower()

    if user_turn not in ["taş", "kağıt", "makas"]:
        print("Geçersiz hamle! Lütfen taş, kağıt veya makas seç.")
        continue

    computer_turn = random.choice(["taş", "kağıt", "makas"])

    hamleleri_yazdır(user_turn, computer_turn)

    kazanan = kazananı_belirle(user_turn, computer_turn)
    sonucu_yaz(kazanan)

    if not tekrar_oyna():
        break

print("Oynadığın için teşekkür ederiz!")
