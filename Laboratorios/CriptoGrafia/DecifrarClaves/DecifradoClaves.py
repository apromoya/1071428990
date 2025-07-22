import hashlib

def decifrar():
    resolverhash = str(input('Ingrese hash para resolver: '))
    type = input('Indique el tipo Cifrado: ')
    
    resolverclave = open('10-million-password-list-top-10000.txt', 'r')
    for x in resolverclave.readlines():
        a = x.strip('\n').encode('utf-8')
        if type == 'md5' :
            a = hashlib.md5(a).hexdigest()
        elif type == 'sha1':
            a = hashlib.sha1(a).hexdigest()
        elif type == 'sha224':
            a = hashlib.sha224(a).hexdigest()
        elif type == 'sha256':
            a = hashlib.sha256(a).hexdigest()
        elif type == 'sha384':
            a = hashlib.sha384(a).hexdigest()
        elif type == 'sha512':
            a = hashlib.sha512(a).hexdigest()
        else:
            ('Tipo de cifrado %s no valido ' %str(type))
        if a == resolverhash :
            print('Clave: %s - ha sido resuelta: %s - Cifrado %s' %(str(x.rstrip()), str(a), str(type) ))
        
if __name__ == '__main__':
    decifrar()