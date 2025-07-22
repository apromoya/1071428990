#Cifrado Claves
import hashlib

def cifrar():
    clave = str(input('Ingrese una clave')).encode('utf-8')
    
    md5 = hashlib.md5(clave).hexdigest()
    print('Hash MD5: %s' % str(md5))
    
    sha1 = hashlib.sha1(clave).hexdigest()
    print('Hash sha1: %s' % str(sha1))
    
    sha224 = hashlib.sha224(clave).hexdigest()
    print('Hash sha224: %s' % str(sha224))
    
    sha256 = hashlib.sha256(clave).hexdigest()
    print('Hash sha256: %s' % str(sha256))

    sha384 = hashlib.sha384(clave).hexdigest()
    print('Hash sha384: %s' % str(sha384))

    sha512 = hashlib.sha512(clave).hexdigest()
    print('Hash sha512: %s' % str(sha512))
    
if __name__ == '__main__':
    cifrar()