import zipfile
import rarfile
import optparse
from threading import Thread

def zip_all(zfile,password):
    try:
        zfile.extractall(pwd=password)
    except:
        pass


def main():
    parser = optparse.OptionParser('usage %prog -H' + '<zip file> -p <zip password>')
    parser.add_option('-g', dest='zip_file_type', type='int', help='zip file type')
    parser.add_option('-f', dest='zip_file', type='string', help='zip file')
    parser.add_option('-d', dest='zip_password', type='string', help='zip password')
    parser.add_option('-x', dest='zip_password_dict', type = 'string' , help = 'zip_dict')
    (options, args) = parser.parse_args()
    zip_file = options.zip_file
    zip_password = options.zip_password
    zip_file_type = options.zip_file_type
    zip_password_dict = options.zip_password_dict
    if (options.zip_file_type == None):
        print('please choose the type')
        exit(0)
    if zip_file_type == 1:
        zfile = zipfile.ZipFile(zip_file)
        zfile.extractall()
        print('successful!!')
    if zip_file_type == 2:
        ## rar算法不对外公开
        rfile = rarfile.RarFile(zip_file)
        rfile.extractall()
        print('successful!!!!')
    if zip_file_type == 3:
        zfile = zipfile.ZipFile(zip_file)
        passfile = open(zip_password_dict)
        for line in passfile.readlines():
            password = line.strip('\n')
            t = Thread(target=zip_all,args = {zfile,password})
            t.start()
    else:
        zfile = zipfile.ZipFile(zip_file)
        try:
            zfile.extractall(pwd=zip_password)
            print('successful!!!')
        except:
            print('password is wrong,please try again!')

if __name__ == '__main__':
    main()




