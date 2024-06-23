#!/usr/bin/env python3
"""
Module Docstring
"""

__author__ = "Lenival Gomes"
__version__ = "0.1.0"
__license__ = "MIT"

MAX_CNPJ_ANTIGO = (int(10)**int(14)-int(1))


"""
to_uint64 recebe uma string e retorna o uint64 do CNPJ correspondente.
"""
def to_uint64(cnpj_string):
    if not isinstance(cnpj_string, str):
        raise Exception("Não é uma string")
    if not str.isalnum(cnpj_string):
        raise Exception("Não alfanumérico")
    
    # Adequando eventuais caracteres maiúsculos
    cnpj_string_u = cnpj_string.upper()
    
    deslocamento = int(0 if str.isnumeric(cnpj_string) else MAX_CNPJ_ANTIGO)
    
    # Seleciona a base 10 para CNPJ antigo e 36 para novos
    base = int(10 if str.isnumeric(cnpj_string) else 36)
    
    # Convertendo para base adequada e adicionando o deslocamento
    cnpj_int = int(cnpj_string,base) + deslocamento
    
    print(f'O valor inteiro para {cnpj_string} é {cnpj_int}')
    
    return cnpj_int
    
"""
to_string recebe um uint64 e retorna a string do CNPJ correspondente.
"""
def to_string(cnpj_int):
    if not isinstance(cnpj_int, int):
        raise Exception("Não é um uint64")
    
    cnpj_string = ''
    if cnpj_int <= MAX_CNPJ_ANTIGO:
        cnpj_string = str(cnpj_int)
    else:
        (base,expoente,resto) = (int(36),int(11),int(cnpj_int-MAX_CNPJ_ANTIGO))
        
        acum_m = int(base**int(expoente))
        quociente = int(0)
        
        while(acum_m != int(0)):
            quociente = resto//acum_m
            resto -= quociente*acum_m
            deslocamento_ascii = int((int(7) if quociente > 9 else int(0)))
            cnpj_string = cnpj_string + (chr( int(quociente + int(48) + deslocamento_ascii)))
            acum_m = acum_m//base
    print(f'O CNPJ int {cnpj_int} como string é: '+cnpj_string)
    return cnpj_string


def main():
    """ Main entry point of the app """
    print("hello world")
    to_uint64("UM1000DEPEAO") # 4029288161716827807
    #to_uint64("um1000depeao") # 4029288161716827807
    to_uint64("123456789011") # 123456789011
    to_uint64("12345678901112") # 123456789011
    to_uint64("ZZZZZZZZZZZZ") # 4738481338321616894
    to_uint64("00000000000A") # 4738481338321616894
    
    #to_string(1234)
    #to_uint64("um1000 depeao")
    #to_uint64(int(1234))
    #to_string(np.uint64(1)+np.uint64(10)**np.uint64(14))
    #to_string(np.uint64(10)**np.uint64(14))
    #to_string(np.uint64(4029188161716827808))
    to_string(int(4029288161716827807)) # UM1000DEPEAO
    to_string(int(4738481338321616894)) # ZZZZZZZZZZZZ
    to_string(int(123456789011)) # 123456789011
    to_string(int(12345678901112)) # 123456789011
    to_string(int(100000000000009)) # 00000000000A
    
    

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()