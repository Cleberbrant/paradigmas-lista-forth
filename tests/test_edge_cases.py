"""
Testes extras de edge case para exercicios.fs — cenários que o professor pode usar.
"""


# sort-two: iguais, negativos
def test_sort_two_equal(io):
    assert io("exercicios.fs", ["5 5 sort-two", ".s"]).stack == [5, 5]


def test_sort_two_negative(io):
    assert io("exercicios.fs", ["-3 -1 sort-two", ".s"]).stack == [-3, -1]
    assert io("exercicios.fs", ["-1 -3 sort-two", ".s"]).stack == [-3, -1]


# sort-three: iguais, negativos, mistos
def test_sort_three_equal(io):
    assert io("exercicios.fs", ["5 5 5 sort-three", ".s"]).stack == [5, 5, 5]


def test_sort_three_negative(io):
    assert io("exercicios.fs", ["-1 -3 -2 sort-three", ".s"]).stack == [-3, -2, -1]


def test_sort_three_two_equal(io):
    assert io("exercicios.fs", ["3 1 3 sort-three", ".s"]).stack == [1, 3, 3]


# dots: 0 e 1
def test_dots_zero(io):
    assert io("exercicios.fs", ["0 dots"]).output == ""


def test_dots_one(io):
    assert io("exercicios.fs", ["1 dots"]).output == "."


# **: edge cases
def test_power_one(io):
    assert io("exercicios.fs", ["7 1 **", ".s"]).stack == [7]


def test_power_base_one(io):
    assert io("exercicios.fs", ["1 100 **", ".s"]).stack == [1]


def test_power_zero_zero(io):
    # 0^0 = 1 (por convenção matemática e do loop)
    assert io("exercicios.fs", ["0 0 **", ".s"]).stack == [1]


def test_power_base_zero(io):
    assert io("exercicios.fs", ["0 5 **", ".s"]).stack == [0]


# 3dup: verifica que não mexe no resto da pilha
def test_3dup_preserves_below(io):
    assert io("exercicios.fs", ["99 1 2 3 3dup", ".s"]).stack == [99, 1, 2, 3, 1, 2, 3]


# put: posição 1 (equivale a swap + manter)
def test_put_pos1(io):
    assert io("exercicios.fs", ["10 20 30 42 1 put", ".s"]).stack == [10, 20, 42, 30]


def test_put_deep(io):
    assert io("exercicios.fs", ["10 20 30 40 50 99 3 put", ".s"]).stack == [10, 20, 99, 30, 40, 50]


# reverse: 1 elemento, 2 elementos
def test_reverse_one(io):
    assert io("exercicios.fs", ["42 1 reverse", ".s"]).stack == [42]


def test_reverse_two(io):
    assert io("exercicios.fs", ["10 20 2 reverse", ".s"]).stack == [20, 10]


def test_reverse_four(io):
    assert io("exercicios.fs", ["1 2 3 4 4 reverse", ".s"]).stack == [4, 3, 2, 1]


# drop-many: drop tudo
def test_drop_many_all(io):
    assert io("exercicios.fs", ["1 2 3 3 drop-many", ".s"]).stack == []


def test_drop_many_one(io):
    assert io("exercicios.fs", ["1 2 3 1 drop-many", ".s"]).stack == [1, 2]


# drop-at: último da pilha (fundo)
def test_drop_at_last(io):
    assert io("exercicios.fs", ["1 2 3 2 drop-at", ".s"]).stack == [2, 3]


# pop-at: fundo
def test_pop_at_bottom(io):
    assert io("exercicios.fs", ["1 2 3 2 pop-at", ".s"]).stack == [2, 3, 1]


# print-change: valor 0, valor exato
def test_print_change_zero(io):
    assert io("exercicios.fs", ["0 print-change"]).lines == [
        "0 nota(s) de 100",
        "0 nota(s) de 50",
        "0 nota(s) de 20",
        "0 nota(s) de 10",
        "0 nota(s) de 5",
        "0 nota(s) de 2",
        "0 moeda(s) de 1",
    ]


def test_print_change_exact_100(io):
    assert io("exercicios.fs", ["100 print-change"]).lines == [
        "1 nota(s) de 100",
        "0 nota(s) de 50",
        "0 nota(s) de 20",
        "0 nota(s) de 10",
        "0 nota(s) de 5",
        "0 nota(s) de 2",
        "0 moeda(s) de 1",
    ]


def test_print_change_188(io):
    # 1x100 + 1x50 + 1x20 + 1x10 + 1x5 + 1x2 + 1x1 = 188
    assert io("exercicios.fs", ["188 print-change"]).lines == [
        "1 nota(s) de 100",
        "1 nota(s) de 50",
        "1 nota(s) de 20",
        "1 nota(s) de 10",
        "1 nota(s) de 5",
        "1 nota(s) de 2",
        "1 moeda(s) de 1",
    ]


# max-n: todos negativos
def test_max_n_all_negative(io):
    assert io("exercicios.fs", ["-10 -5 -20 3 max-n", ".s"]).stack == [-5]


# max-n: todos iguais
def test_max_n_equal(io):
    assert io("exercicios.fs", ["7 7 7 3 max-n", ".s"]).stack == [7]


# reset: pilha já vazia
def test_reset_empty(io):
    assert io("exercicios.fs", ["reset", ".s"]).stack == []


# all-positive: zero não é positivo
def test_all_positive_with_zero(io):
    assert io("exercicios.fs", ["1 2 0 all-positive", ".s"]).stack == [0]


# all-positive: um elemento
def test_all_positive_single(io):
    assert io("exercicios.fs", ["5 all-positive", ".s"]).stack == [-1]


def test_all_positive_single_negative(io):
    assert io("exercicios.fs", ["-1 all-positive", ".s"]).stack == [0]


# all-sorted: um elemento
def test_all_sorted_single(io):
    assert io("exercicios.fs", ["42 all-sorted", ".s"]).stack == [-1]


# all-sorted: iguais
def test_all_sorted_equal(io):
    assert io("exercicios.fs", ["5 5 5 all-sorted", ".s"]).stack == [-1]


# all-sorted: decrescente
def test_all_sorted_descending(io):
    assert io("exercicios.fs", ["3 2 1 all-sorted", ".s"]).stack == [0]


# all-sorted: 2 elementos
def test_all_sorted_two(io):
    assert io("exercicios.fs", ["1 2 all-sorted", ".s"]).stack == [-1]
    assert io("exercicios.fs", ["2 1 all-sorted", ".s"]).stack == [0]


# filter-positive: tudo negativo
def test_filter_positive_all_negative(io):
    assert io("exercicios.fs", ["-1 -2 -3 filter-positive", ".s"]).stack == []


# filter-positive: pilha vazia
def test_filter_positive_empty(io):
    assert io("exercicios.fs", ["filter-positive", ".s"]).stack == []


# filter-positive: tudo positivo
def test_filter_positive_all_positive(io):
    assert io("exercicios.fs", ["5 10 15 filter-positive", ".s"]).stack == [5, 10, 15]


# filter-positive: somente zeros
def test_filter_positive_zeros(io):
    assert io("exercicios.fs", ["0 0 0 filter-positive", ".s"]).stack == [0, 0, 0]
