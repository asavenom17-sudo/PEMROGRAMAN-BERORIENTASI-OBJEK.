class RekeningBank:
    def __init__(self, nama, saldo):
        self.nama = nama
        self.saldo = saldo 


akun_rofik = RekeningBank("Rofik", 1000000)
print(f"Saldo awal Rofik: {akun_rofik.saldo}")

akun_rofik.saldo = -5000000
print(f"Saldo akhir Rofik: {akun_rofik.saldo}")
