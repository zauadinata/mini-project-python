print ('==============================================')
print ('| selamat datang di program data nilai siswa |')
print ('==============================================')
print ('\n')


def akun():
    password = 'admin123'

    ps = (input ('masukkan password : '))

    if ps == password:
        print ('password benar')
    else:
        print ('password salah\n program selesai')
        exit()
    
def sistem():
    while True:
        nama = input ('masukkan nama : ')
        if nama =='exit':
            print ('program selesai')
            break
    
        umur = int (input ('masukkan umur : '))
        data =  int (input ('masukkan angka : '))

        if data <= 60:
            print ('nilai C')
        elif  60 <= data <= 80:
            print ('nilai B')
        elif 80 <= data <=100:
            print ('nilai A')
        else :
            print ('program selesai')
            continue

        lanjut = input('Lanjut? [y/n]: ').lower()
        if lanjut == 'y':
            print('Melanjutkan...')
        elif lanjut == 'n':
            print('Program selesai')
            break
        else:
            print('Input tidak dikenali. Program selesai.')
            break
akun()
sistem()


        


