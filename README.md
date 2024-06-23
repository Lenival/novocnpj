# novocnpj
Repositório com rotinas para tratamento de CNPJ como números inteiros de 64 bits, visando retrocompatibilidade com soluções pré-existentes em 2024.

# Contexto
Em virtude da Nota Técnica conjunta COCAD/SUARA/RFB nº 49 de 14 de maio de 2024, o padrão de CNPJ passará a adotar letras e números (string alfanumérica) para o campo raiz e ordem, mantendo apenas estritamente numéricos os dois caracteres do dígito verificador (DV).

# Impactos
Essa modificação faz com que a quantidade de CNPJ possíveis passe a ser 36^12=4738381338321616896 (19 dígitos). Bases de dados que armazenam o CNPJ como um número de 12 (sem DV) ou 14 dígitos (com DV) não terão como armazenar novos CNPJ sem modificações.

# Proposta
Visando a retrocompatibilidade com sistemas em operação que representam CNPJ como inteiros (NUMBER(14), por exemplo), proponho que sejam utilizado o tipo NUMBER(19) (ou uint64 em sistema sem esse tipo). Dessa forma os antigos CNPJ continuam a ser representados da mesma forma que já eram e os novos serão associados a valores inteiros a partir de 10^14.

# Algoritmo para conversão de string para inteiro
A fazer...
