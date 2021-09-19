print("\t\t\tEl's Comp")
print("_____________________")
print("Kode             Jenis                          Harga")
print("_____________________")
print(" 1              Printer                      Rp.1.200.000")
print(" 2               Mouse                       Rp.105.000")
print(" 3           S'Flashdisk 8GB                  Rp.80.000")
print(" 4           Laptop Acer XXX                 Rp.4.500.000")
print(" 5           Laptop Del YYY                  Rp.4.500.00")
print(" 6           Laptop Samsung XYZ              Rp.5.000.000")
print("____________________")
garis="--------------------------------------------------------------"

ulang = "ya " or "Ya" or "YA" or "iya" or "Iya" or "IYA"  
nama  = ["","","","","","","","","",""]
harga = [0,0,0,0,0,0]
qty   = [0,0,0,0,0,0]

jumlah_barang = (1,2,3,4,5,6)
kode = ("1","2","3","4","5","6")
kode_nama_barang = {"1":" Printer","2":"Mouse","3":"S'Flashdisk 8GB ","4":"Laptop Acer XXX ","5":"  Laptop Del","6":"Laptop Samsung XYZ"}
kode_harga_barang= {"1":1200000,"2":105000,"3":80000,"4":4500000,"5":4500000,"6":"5000000"}
nama_pelanggan=input("Pesanan Atas Nama :")
tgl_transaksi=input("Masukkan Tgl transaksi anda dengan format dd/mm/yy :")
jam=input("Masukkan waktu pembelian :")


while True:
    sub_total = 0
    print("Kode Jenis   [1/2/3/4/5/6] ")
    jumlah = int(input("Jumlah Jenis <1-6>:"))
    if jumlah not in jumlah_barang:
        print("Jumlah yang anda masukkan tidak tersedia!")
        continue
    for barang in range(jumlah):
        input_barang = input("Masukkan Barang ke -"+str(barang+1)+"<1/2/3/4/5/6>\t :")
        qty[barang] = int(input("Masukkan Jumlah Barang ke "+str(barang+1)+"\t:"))
        if input_barang in kode:
            nama[barang]  = kode_nama_barang[input_barang]
            harga[barang] = kode_harga_barang[input_barang]
        else:
            nama[barang]  = "Barang Tidak Dijual Di toko kami "
            harga[barang] = 0
    for hasil in range(jumlah):
        print("Barang\t ke",hasil+1,"\t:",nama[hasil])
        print("Harga\t ke",hasil+1,"\t:",harga[hasil])
        print("Jumlah\t ke",hasil+1,"\t:",qty[hasil])
        print("Total\t ke",hasil+1,"\t:",harga[hasil]*qty[hasil])
        print(garis)
        print("")
        sub_total += harga[hasil]*qty[hasil]
        

    if (sub_total >=30000000):
            diskon = sub_total*(15/100)
            total= sub_total-diskon
            print("Total Harga\t:",sub_total)
            print("karena Anda belanja lebih dari Rp.30.000.000,-") 
            print("Selamat Anda Mendapat potongan Harga sebesar 15%")
            print(garis)
            print("")
            print("Harga Barang\t:", int(total))
            print("______Anda Terkena Pajak sebesar 2%______")
    else:  
            total = sub_total
            print("Harga Barang\t:", int(total))
            print(garis)
            print("______Anda Terkena Pajak sebesar 2%______")
   
            print("")

    if total:
        ppn= total*(2/100)
        total_barang= total+ppn
        print("Total Bayar\t:",int(total_barang))
        print("" )
        print("")
        print("Atas Nama\t :",nama_pelanggan.upper())
        print("Tanggal pembelian:",tgl_transaksi.upper())
        print("Jam pembelian\t :",jam)
        print("********TERIMA KASIH*********")
    else:
        total=0
        print("Tidak ada barang")
        print("Total Bayar\t:",int(total))
        print("")
        print("")
        print("Atas Nama\t :",nama_pelanggan.upper())
        print("Tanggal pembelian:",tgl_transaksi.upper())
        print("Jam pembelian\t :",jam)
        print("********TERIMA KASIH*********")




    ulang=input("Apakah anda ingin melanjutkan pembelian? <Ya/Tidak> ")
    if ulang == "Tidak":
        break