\ Responda os exercícios aqui. Lembre-se de remover qualquer código fora de
\ definições antes de enviar a resposta final.

\ ==============================================================================
\ DEFINIÇÕES
\ ==============================================================================

variable size
0 size !
create buf 1000 cells allot

: get-number ( -- n )
    pad 20 accept pad swap  ( lê até 20 caracteres e deixa addr n na pilha )
    s>number? if            ( converte string para número de dupla precisão e uma flag )
        drop                ( remove a parte de dupla precisão, deixando apenas a parte baixa na pilha )
    else 
        2drop 0             ( limpa a pilha em caso de falha e retorna 0 )
    then 
;

\ ( a -- ) adiciona a ao final do array
: push
    buf size @ cells + !
    1 size +!
;

\ ( -- a ) remove e retorna o último elemento
: pop
    -1 size +!
    buf size @ cells + @
;

\ ( i -- a ) retorna o elemento na posição i
: get
    cells buf + @
;

\ ( a i -- ) define o valor na posição i
: set
    cells buf + !
;

\ ( -- ) lê números do usuário até 0 ou inválido
: read-array
    begin
        get-number
        dup 0 <>
    while
        push
    repeat
    drop
;

\ ( -- ) imprime todos os elementos separados por espaço
: print-array
    size @ 0 ?do
        i get .
    loop
;

\ ( -- sum ) soma todos os elementos
: add-array
    0
    size @ 0 ?do
        i get +
    loop
;

\ ( -- max ) retorna o maior elemento
: max-array
    0 get
    size @ 1 ?do
        i get max
    loop
;

\ ( -- min ) retorna o menor elemento
: min-array
    0 get
    size @ 1 ?do
        i get min
    loop
;

\ ( F: -- avg ) retorna a média como float
: average-array
    add-array s>f size @ s>f f/
;


\ ==============================================================================
\ TESTES
\ ==============================================================================
\ Não esqueça de apagar ou comentar código fora das definições antes de enviar 
\ a submissão final ou rodar os testes usando o pytest.

\ read-array 
\ ." Números: " print-array cr
\ ." Tamanho: " size @ . cr
\ ." Soma: " add-array . cr
\ ." Max: " max-array . cr
\ ." Media: " average-array F. cr
\ 
\ bye
