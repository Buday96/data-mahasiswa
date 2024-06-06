data_mahasiswa = [] # Untuk Menyimpan Semua yang diInput User
ulang = 'Y'
while ulang == 'Y':
    print("="*40)
    print("\t DATA MAHASISWA")
    print("="*40)
    print("\t MENU")
    print("1. Input Data Mahasiswa")
    print("2. Jumlah Data Mahasiswa")
    print("3. Pencarian Data Mahasiswa")
    print("4. Pengurutan Data Mahasiswa")
    print("5. Cetak Data Mahasiswa")

    print("="*40)
    pilihan = input("Pilih Menu [1-5] : ")
    print("="*40)

    if pilihan == "1":
        nama = input("Masukkan Nama Mahasiswa  : ")
        semester = input("Masukkan Semester        : ")
        npm = input("Masukkan Npm             : ")
        prodi = input("Masukkan Prodi           : ")
        kelas = input("Masukkan Pagi/Malam      : ")

        data_mahasiswa.append({"nama": nama,"semester": semester, "npm": npm, "prodi": prodi, "kelas": kelas})
        print("="*40)
        print("Data Mahasiswa Berhasil diInput!!")
        print("="*40)
        print()

        ulang = input("Apakah Anda Ingin Kembali Ke Menu? [y/n] : ").upper()
        print()

        if ulang == "N":
            print("Terima Kasih Telah Menginput Data")
            print()
    elif pilihan == "2":
        jumlah_mahasiwa = len(data_mahasiswa)
        print(f"Jumlah Mahasiswa : {jumlah_mahasiwa}")
        print("="*40)

        ulang = input("Apakah Anda Ingin Kembali Ke Menu? [y/n] : ").upper()
        print()

        if ulang == "N":
            print("Terima Kasih Telah Menginput Data")
            print()

    elif pilihan == "3":
        if not data_mahasiswa:
            print("Data Mahasiswa Belum diInput!\n")
        else:
            cari_nama = input("Masukkan Nama Mahasiswa Yang Ingin di Cari : ")
            ditemukan = False
            for mahasiswa in data_mahasiswa:
                if mahasiswa["nama"] == cari_nama:
                    print("="*40)
                    print("Data Mahasiswa diTemukan")
                    print(f"Nama     : {mahasiswa['nama']}")
                    print(f"Semester : {mahasiswa['semester']}")
                    print(f"Npm      : {mahasiswa['npm']}")
                    print(f"Prodi    : {mahasiswa['prodi']}")
                    print(f"Kelas    : {mahasiswa['kelas']}")
                    print("="*40)
                    ditemukan = True
                    break
            if not ditemukan:
                print()
                print("Data Mahasiswa Tidak diTemukan")
                print("="*40)

            ulang = input("Apakah Anda Ingin Kembali Ke Menu? [y/n] : ").upper()

            if ulang == "N":
                print("Terima Kasih Telah Menginput Data")
                print()
    elif pilihan == "4":
        if not data_mahasiswa:
            print("Data Mahasiswa Belum diInput!\n")
        else:        
            print("Pilihan Pengurutan Data")
            print("1. Berdasarkan nama")
            print("2. Berdasarkan Semester")

            pilihan_urut = input("Pilih Pengurutan [1-2] : ")
            print()
            if pilihan_urut == "1":
                data_mahasiswa.sort(key=lambda m: m["nama"])
                print("Data Mahasiswa Berhasil diUrutkan Berdaskan Nama!")
            elif pilihan_urut == "2":
                data_mahasiswa.sort(key=lambda m: m['semester'])
                print("Data Mahasiswa Berhasil diUrutkan Berdaskan Semester Terkecil!")
            else:
                print("Pengurutan Tidak Valid!!")
                
            for mahasiswa in data_mahasiswa:
                print("-"*40)
                print(f"Nama     : {mahasiswa['nama']}")
                print(f"Semester : {mahasiswa['semester']}")
                print(f"Npm      : {mahasiswa['npm']}")
                print(f"Prodi    : {mahasiswa['prodi']}")
                print(f"Kelas    : {mahasiswa['kelas']}")
                print("="*40)
                
            ulang = input("Apakah Anda Ingin Kembali Ke Menu? [y/n] : ").upper()
            print()

            if ulang == "N":
                print("Terima Kasih Telah Menginput Data")
                print()
    elif pilihan == "5":
        if not data_mahasiswa:
            print("Data Mahasiswa Belum diInput!\n")
        else:
            print("Data Mahasiswa")
            for mahasiswa in data_mahasiswa:
                print(f"Nama     : {mahasiswa['nama']}")
                print(f"Semester : {mahasiswa['semester']}")
                print(f"Npm      : {mahasiswa['npm']}")
                print(f"Prodi    : {mahasiswa['prodi']}")
                print(f"Kelas    : {mahasiswa['kelas']}")
                print("="*40)
                print()
            
            ulang = input("Apakah Anda Ingin Kembali Ke Menu? [y/n] : ").upper()
            print()

            if ulang == "N":
                print("Terima Kasih Telah Menginput Data")
                print()
    else:
        print("Pilihan Data Tidak Valid!. Silahkan Pilih Menu [1-5] : ")


            
                
                
            




            
            
        



