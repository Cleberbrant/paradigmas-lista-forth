\ Responda os exercícios aqui. Lembre-se de remover qualquer código fora de
\ definições antes de enviar a resposta final.

\ ==============================================================================
\ DEFINIÇÕES
\ ==============================================================================

\ ( a b -- x y ) coloca a e b em ordem crescente
: sort-two
    2dup > if swap then
;

\ ( a b c -- x y z ) coloca a, b e c em ordem crescente
: sort-three
    sort-two >r sort-two r> sort-two
;

\ ( n -- ) imprime n pontos
: dots
    0 ?do [char] . emit loop
;

\ ( a b -- a^b ) exponenciação, b >= 0
: **
    1 swap 0 ?do over * loop nip
;

\ ( a b c -- a b c a b c ) duplica os 3 do topo
: 3dup
    2 pick 2 pick 2 pick
;

\ ( ... a n -- ... a ... ) insere a na posição n da pilha
: put
    dup 0 = if drop exit then
    1-
    rot >r
    recurse
    r>
;

\ ( ... n -- ... ) inverte os n elementos do topo
: reverse
    dup 1 <= if drop exit then
    dup >r 1- roll
    r> 1-
    swap >r
    recurse
    r>
;

\ ( ... n -- ... ) remove n elementos do topo
: drop-many
    0 ?do drop loop
;

\ ( ... n -- ... ) remove o elemento na posição n (0=topo)
: drop-at
    roll drop
;

\ ( ... n -- ... a ) move o elemento na posição n para o topo
: pop-at
    roll
;

\ ( a -- ) imprime decomposição em notas e moedas
: print-change
    dup 100 / . ." nota(s) de 100" cr
    100 mod
    dup 50 / . ." nota(s) de 50" cr
    50 mod
    dup 20 / . ." nota(s) de 20" cr
    20 mod
    dup 10 / . ." nota(s) de 10" cr
    10 mod
    dup 5 / . ." nota(s) de 5" cr
    5 mod
    dup 2 / . ." nota(s) de 2" cr
    2 mod
    . ." moeda(s) de 1" cr
;

\ ( ... n -- max ) retorna o maior entre n elementos do topo
: max-n
    1- 0 ?do max loop
;

\ ( ... -- ) remove todos os elementos da pilha
: reset
    begin depth while drop repeat
;

\ ( ... -- flag ) true se todos os elementos são positivos (>0)
: all-positive
    depth 0 = if true exit then
    true
    depth 1- 0 ?do
        swap 0> and
    loop
;

\ ( ... -- flag ) true se os elementos estão em ordem crescente
: all-sorted
    depth 1 <= if
        begin depth while drop repeat
        true exit
    then
    begin depth 2 >= while
        2dup > if
            begin depth while drop repeat
            false exit
        then
        drop
    repeat
    drop
    true
;

\ ( ... -- ... ) mantém apenas elementos >= 0
: filter-positive
    depth 0 = if exit then
    >r recurse r>
    dup 0 < if drop then
;


\ ==============================================================================
\ TESTES
\ ==============================================================================
\ Não esqueça de apagar ou comentar código fora das definições antes de enviar 
\ a submissão final ou rodar os testes usando o pytest.

\ 1 2 3 sort-two .s cr \ deve imprimir "1 2 3"
\ 3 2 1 sort-two .s cr \ deve imprimir "2 3 1"
