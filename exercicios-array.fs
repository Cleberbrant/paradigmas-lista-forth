\ Responda os exercícios aqui. Lembre-se de remover qualquer código fora de
\ definições antes de enviar a resposta final.

\ ==============================================================================
\ DEFINIÇÕES
\ ==============================================================================

: get-number ( -- n )
    pad 20 accept pad swap  ( lê até 20 caracteres e deixa addr n na pilha )
    s>number? if            ( converte string para número de dupla precisão e uma flag )
        drop                ( remove a parte de dupla precisão, deixando apenas a parte baixa na pilha )
    else 
        2drop 0             ( limpa a pilha em caso de falha e retorna 0 )
    then 
;

: get ( i -- n ) ;
: set ( i n -- ) ;
: read-array ( -- ) ;
: print-array ( -- ) ;
: add-array ( -- sum ) ;
: max-array ( -- max ) ;
: min-array ( -- min ) ;
: average-array ( -- avg ) ;


\ ==============================================================================
\ TESTES
\ ==============================================================================
\ Não esqueça de apagar ou comentar código fora das definições antes de enviar 
\ a submissão final ou rodar os testes usando o pytest.

read-array 
." Números: " print-array cr
." Tamanho: " size @ . cr
." Soma: " add-array . cr
." Max: " max-array . cr
." Media: " average-array F. cr

bye
