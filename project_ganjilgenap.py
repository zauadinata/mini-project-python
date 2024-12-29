print ('===========================')
print ('penentuan ganjil atau genap')
print ('===========================')


data_angka = int (input ('masukkan angka : '))


hasil = data_angka % 2
output_bagi = data_angka / 2 
if hasil == 0:
    # data_angka di modulus 2 menghasilkan sisa bagi
    # jika hasil bagi tidak merata, maka ganjil
    # == 0 untuk memeriksa hasil modulus sama dengan 0, jika iya maka genap
    print (f'angka                : {data_angka} adalah genap')
    print (f'data yang diinputkan : {data_angka}')
    print (f'hasil dari modulus   : {hasil}')
    print (f'hasil sisa bagi      : {output_bagi}')
else :
    print (f'angka                : {data_angka} adalah ganjil')
    print (f'data yang diinputkan : {data_angka}')
    print (f'hasil dari modulus   : {hasil}')
    print (f'hasil sisa bagi      : {output_bagi}')


