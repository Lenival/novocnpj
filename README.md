# novocnpj
Repositório com rotinas para tratamento de CNPJ como números inteiros de 64 bits, visando retrocompatibilidade com soluções pré-existentes em 2024.

# Contexto
Em virtude da Nota Técnica conjunta COCAD/SUARA/RFB nº 49 de 14 de maio de 2024, o padrão de CNPJ passará a adotar letras e números (string alfanumérica) para o campo raiz e ordem, mantendo apenas estritamente numéricos os dois caracteres do dígito verificador (DV).

# Impactos
O novo formato possibilita que cada uma das 12 posições (8 para raiz e 4 para ordem) assuma 36 valores diferentes que podem ser cada um do 10 dígitos decimais ou 26 letras do alfabeto. Essa modificação faz com que a quantidade de CNPJ possíveis passe a ser 36^12=4738381338321616896 (19 dígitos). Bases de dados que armazenam o CNPJ como um número de 12 (sem DV) ou 14 dígitos (com DV) não terão como armazenar novos CNPJ sem modificações.

# Proposta
Visando a retrocompatibilidade com sistemas em operação que representam CNPJ como inteiros (NUMBER(14), por exemplo), proponho que sejam utilizado o tipo NUMBER(19) (ou uint64 em sistema sem esse tipo). Dessa forma os antigos CNPJ continuam a ser representados da mesma forma que já eram e os novos serão associados a valores inteiros a partir de 10^14.

# Algoritmo para conversão de string para inteiro
Para CNPJ com apenas dígitos, a representação será feita por um valor inteiro entre 0 e 10^14-1 cujos dígitos em cada posição do CNPJ coincidem com os dígitos do inteiro que representador. Essencialmente esse é uma representação da string por um número de base 10. Essa representação possibilita a retrocompatibilidade com sistemas existentes.
Para CNPJ que contenham ao menos uma letra do alfabeto, cada caracter representará o dígito de um número na base 36. Os dígitos decimais de 0 a 9 ainda mantém seus valores de 0 a 9 na nova base, e a partir do valor 10 até o 35 são usadas as letras de A até Z. Isso é análogo ao que é feito com a representação de hexadecimais, onde a base é 16. Como os 10^14 primeiros valores já são utilizados, o valor decimal correspontes ao CNPJ estritamente alfanuméricos será adicionado de 10^14-1. Dessa forma, o primeiro CNPJ estritamente alfanumérico, cuja representação em base 36 é 00000000000A, será associado ao número decimal 100000000000009; e o último, ZZZZZZZZZZZZ, é representado por 4738481338321616894.

# Valores proibidos
Nessa forma de representar, alguns valores são proibidos para representação, como por exemplo o inteiro 100000000000008 que representaria 000000000009, mas 000000000009 já possui representação menor que 10^14. Particularidades como essa são análogas ao que acontece com o padrão IEEE-754, o ponto flutuante mais comum usado nas mais diversas tecnologias, em que certos valores não rotulados como NaN.
