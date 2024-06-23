#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Lenival Gomes"
__version__ = "0.1.0"
__license__ = "MIT"

import numpy as np

MAX_CNPJ_ANTIGO = (np.uint64(10)**np.uint64(14)-np.uint64(1))


"""
to_uint64 recebe uma string e retorna o uint64 do CNPJ correspondente.
"""
def to_uint64(cnpj_string):
    if not isinstance(cnpj_string, str):
        raise Exception("Não é uma string")
    if not str.isalnum(cnpj_string):
        raise Exception("Não alfanumérico")
    
    cnpj_string_u = cnpj_string.upper()
    # print(cnpj_string_u)
    # print(cnpj_string_u[::-1])
    
    # Inicialização de acumuladores multiplicativo e aditivo
    acum_m = np.uint64(1)
    acum_a = np.uint64(0)
    acum_a += (0 if str.isnumeric(cnpj_string) else MAX_CNPJ_ANTIGO)
    
    # Seleciona a base 10 para CNPJ antigo e 36 para novos
    base = np.uint64(10 if str.isnumeric(cnpj_string) else 36)
    
    for alfanum in list(cnpj_string_u[::-1]):
        #print(alfanum)
        #print(ord(alfanum))
        ##print(ord(alfanum)-48)
        #print(ord(alfanum)-48-(7 if ord(alfanum)>=65 else 0))
        acum_a += np.uint64(acum_m*np.uint64(ord(alfanum)-48-(7 if ord(alfanum)>=65 else 0)))
        #print(acum_a)
        acum_m *=base
        #print(acum_m)
        #print(type(acum_m))
        #print(type(acum_a))
    
    # print(int(acum_m))
    print(f'O valor inteiro para {cnpj_string} é {int(acum_a)}')
    return acum_a
    
"""
to_string recebe um uint64 e retorna a string do CNPJ correspondente.
"""
def to_string(cnpj_uint64):
    if not isinstance(cnpj_uint64, np.uint64):
        raise Exception("Não é um uint64")
        
    if cnpj_uint64 <= MAX_CNPJ_ANTIGO:
        (base,expoente,resto) = (np.uint64(10),np.uint64(11),cnpj_uint64)
    else:
        (base,expoente,resto) = (np.uint64(36),np.uint64(11),cnpj_uint64-MAX_CNPJ_ANTIGO)
        
    acum_m = np.uint64(base**np.uint64(expoente))
    quociente = np.uint64(0)
    cnpj_string = ''
    
    while(acum_m != np.uint64(0)):
        quociente = resto//acum_m
        resto -= quociente*acum_m
        cnpj_string = cnpj_string + (chr(quociente + np.uint64(48) + np.uint64(7 if quociente > 9 else 0)))
        # print(f'quociente:{quociente} resto:{resto} acum_m:{acum_m} base:{base} cnpj_string:' + cnpj_string)
        acum_m = acum_m//base
    # print(base)
    # print(expoente)
    # print(acum_m) 
    print(f'O CNPJ uint64 {cnpj_uint64} como string é: '+cnpj_string)


def main():
    """ Main entry point of the app """
    print("hello world")
    to_uint64("UM1000DEPEAO") # 4029288161716827807
    #to_uint64("um1000depeao") # 4029288161716827807
    to_uint64("123456789011") # 123456789011
    to_uint64("ZZZZZZZZZZZZ") # 4738481338321616894
    to_uint64("00000000000A") # 4738481338321616894
    
    #to_string(1234)
    #to_uint64("um1000 depeao")
    #to_uint64(int(1234))
    #to_string(np.uint64(1)+np.uint64(10)**np.uint64(14))
    #to_string(np.uint64(10)**np.uint64(14))
    #to_string(np.uint64(4029188161716827808))
    to_string(np.uint64(4029288161716827807)) # UM1000DEPEAO
    to_string(np.uint64(4738481338321616894)) # ZZZZZZZZZZZZ
    to_string(np.uint64(123456789011)) # 123456789011
    to_string(np.uint64(100000000000009)) # 00000000000A
    
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()