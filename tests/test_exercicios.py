def test_sort_two(io):
    assert io("exercicios.fs", ["1 2 sort-two", ".s"]).stack == [1, 2]
    assert io("exercicios.fs", ["2 1 sort-two", ".s"]).stack == [1, 2]
    assert io("exercicios.fs", ["3 2 1 sort-two", ".s"]).stack == [3, 1, 2]


def test_sort_three(io):
    assert io("exercicios.fs", ["1 2 3 sort-three", ".s"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["2 1 3 sort-three", ".s"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["3 2 1 sort-three", ".s"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["4 3 2 1 sort-three", ".s"]).stack == [4, 1, 2, 3]
    

def test_dots(io):
    assert io("exercicios.fs", ["3 dots"]).output == "..."
    assert io("exercicios.fs", ["4 dots"]).output == "...."


def test_power(io):
    assert io("exercicios.fs", ["2 3 **", ".s"]).stack == [8]
    assert io("exercicios.fs", ["5 0 **", ".s"]).stack == [1]
    assert io("exercicios.fs", ["2 10 **", ".s"]).stack == [1024]


def test_3dup(io):
    assert io("exercicios.fs", ["1 2 3 3dup", ".s"]).stack == [1, 2, 3, 1, 2, 3]
    assert io("exercicios.fs", ["1 2 3 4 5 6 3dup", ".s"]).stack == [1, 2, 3, 4, 5, 6, 4, 5, 6]


def test_put(io):
    assert io("exercicios.fs", ["1 2 3 42 2 put", ".s"]).stack == [1, 42, 2, 3]
    assert io("exercicios.fs", ["1 2 3 42 0 put", ".s"]).stack == [1, 2, 3, 42]


def test_reverse(io):
    assert io("exercicios.fs", ["10 20 30 3 reverse", ".s"]).stack == [30, 20, 10]
    assert io("exercicios.fs", ["0 10 20 30 3 reverse", ".s"]).stack == [0, 30, 20, 10]
    assert io("exercicios.fs", ["1 2 0 reverse", ".s"]).stack == [1, 2]


def test_drop_many(io):
    assert io("exercicios.fs", ["1 2 3 4 2 drop-many", ".s"]).stack == [1, 2]
    assert io("exercicios.fs", ["1 2 3 0 drop-many", ".s"]).stack == [1, 2, 3]


def test_drop_at(io):
    assert io("exercicios.fs", ["1 2 3 1 drop-at", ".s"]).stack == [1, 3]
    assert io("exercicios.fs", ["1 2 3 4 2 drop-at", ".s"]).stack == [1, 3, 4]
    assert io("exercicios.fs", ["1 2 3 4 0 drop-at", ".s"]).stack == [1, 2, 3]


def test_pop_at(io):
    assert io("exercicios.fs", ["1 2 3 4 2 pop-at", ".s"]).stack == [1, 3, 4, 2]
    assert io("exercicios.fs", ["1 2 3 0 pop-at", ".s"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["1 2 3 1 pop-at", ".s"]).stack == [1, 3, 2]


def test_print_change(io):
    assert io("exercicios.fs", ["42 print-change"]).lines == [
        "0 nota(s) de 100",
        "0 nota(s) de 50",
        "2 nota(s) de 20",
        "0 nota(s) de 10",
        "0 nota(s) de 5",
        "1 nota(s) de 2",
        "0 moeda(s) de 1",
    ]
    assert io("exercicios.fs", ["256 print-change"]).lines == [
        "2 nota(s) de 100",
        "1 nota(s) de 50",
        "0 nota(s) de 20",
        "0 nota(s) de 10",
        "1 nota(s) de 5",
        "0 nota(s) de 2",
        "1 moeda(s) de 1",
    ]

def test_max_n(io):
    assert io("exercicios.fs", ["10 42 -1 20 4 max-n", ".s"]).stack == [42]
    assert io("exercicios.fs", ["10 42 -1 20 10 2 4 max-n", ".s"]).stack == [10, 42, 20]
    assert io("exercicios.fs", ["10 1 max-n", ".s"]).stack == [10]


def test_reset(io):
    assert io("exercicios.fs", ["1 2 3 reset", ".s"]).stack == []
    assert io("exercicios.fs", ["1 2 3 4 reset", ".s"]).stack == []


def test_all_positive(io):
    assert io("exercicios.fs", ["1 2 3 all-positive", ".s"]).stack == [-1]
    assert io("exercicios.fs", ["all-positive", ".s"]).stack == [-1]
    assert io("exercicios.fs", ["1 -1 2 all-positive", ".s"]).stack == [0]


def test_all_sorted(io):
    assert io("exercicios.fs", ["1 2 3 all-sorted", ".s"]).stack == [-1]
    assert io("exercicios.fs", ["1 3 2 all-sorted", ".s"]).stack == [0]
    assert io("exercicios.fs", ["all-sorted", ".s"]).stack == [-1]


def test_filter_positive(io):
    assert io("exercicios.fs", ["1 2 3 filter-positive", ".s"]).stack == [1, 2, 3]
    assert io("exercicios.fs", ["-1 0 2 -3 4 filter-positive", ".s"]).stack == [0, 2, 4]

