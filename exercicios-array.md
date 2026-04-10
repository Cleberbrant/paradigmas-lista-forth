# Arrays

Crie duas variáveis globais "buf" (com 1000 células) e "size" (inicializada com
0). A variável "buf" deve ser usada para armazenar uma sequência de números, e a
variável "size" deve manter o número de elementos atualmente armazenados em
"buf".

Em seguida, implemente as seguintes palavras para manipular essa estrutura de
dados:

- `push ( a -- )`: lê um número da pilha e o adiciona ao final da sequência em
  "buf", incrementando "size" em 1.

- `pop ( -- a )`: remove o último número da sequência em "buf", decrementando
  "size" em 1.

- `get ( i -- a )`: lê um índice `i` da pilha e deixa o número correspondente da
  sequência em "buf" no topo da pilha. Assuma que `i` é um número não negativo e
  menor que "size".

- `set ( a i -- )`: lê um número `a` e um índice `i` da pilha e atualiza o
  número correspondente da sequência em "buf" para `a`. Assuma que `i` é um
  número não negativo e menor que "size".

- `print-array ( -- )`: imprime todos os números atualmente armazenados em "buf",
  separados por espaços.

- `array-sum ( -- sum )`: calcula a soma de todos os números atualmente
  armazenados em "buf" e deixa o resultado no topo da pilha.

- `array-max ( -- max )`: encontra o maior número atualmente armazenado em "buf"
  e deixa o resultado no topo da pilha.

- `array-min ( -- min )`: encontra o menor número atualmente armazenado em "buf"
  e deixa o resultado no topo da pilha.

- `array-average ( F: -- avg )`: calcula a média de todos os números atualmente
  armazenados em "buf" e deixa o resultado no topo da pilha de floats.


Agora declare a palavra `get-number` como abaixo:

```forth
: get-number ( -- n )
    pad 20 accept pad swap  ( lê até 20 caracteres e deixa addr n na pilha )
    s>number? if            ( converte string para número de dupla precisão e uma flag )
        drop                ( remove a parte de dupla precisão, deixando apenas a parte baixa na pilha )
    else 
        2drop 0             ( limpa a pilha em caso de falha e retorna 0 )
    then 
;
```

Use isto para implementar uma função `read-array ( -- )` que lê números do
usuário armazenando-os em "buf". A função deve continuar lendo números até que o
usuário digite um número não reconhecido ou igual a zero.

Finalmente, use as palavras definidas acima para implementar o programa:

```forth
read-array 
." Números: " print-array cr
." Tamanho: " size @ . cr
." Soma: " add-array . cr
." Max: " max-array . cr
." Media: " average-array F. cr

bye
```