# Autor: Hugo Araya Carrasco
def lectura(nombre):
    ent = open(nombre)
    cantidad = int(ent.readline().rstrip('\n'))
    linea1 = ent.readline().rstrip('\n').split(' ')
    linea2 = ent.readline().rstrip('\n').split(' ')
    linea3 = ent.readline().rstrip('\n').split(' ')
    ent.close()
    digitos = []
    i = 0
    while i < cantidad:
        digi1 = linea1[i] + linea2[i] + linea3[i]
        digitos.append(digi1)
        i = i + 1
    return digitos

def traduccion(digi_braille):
    numeros = ['.***..', '*.....', '*.*...', '**....', '**.*..', '*..*..', '***...', '****..','*.**..', '.**...']
    nro_str = ''
    for digito in digi_braille:
        nro = numeros.index(digito)
        nro_str = nro_str + str(nro)
    return nro_str

def genera_archivo(nombre, digi_arabigo):
    sal = open(nombre, 'w')
    sal.write(digi_arabigo+'\n')
    sal.close()


if __name__ == '__main__':
    digi_braille = lectura('mensaje_in.txt')
    digi_arabigo = traduccion(digi_braille)
    genera_archivo('mensaje_out.txt', digi_arabigo)
