def test_push_and_size(io):
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "size @ .s"])
    assert r.stack == [3]


def test_pop(io):
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "pop .s"])
    assert r.stack == [30]


def test_pop_decrements_size(io):
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "pop drop size @ .s"])
    assert r.stack == [2]


def test_get(io):
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "0 get .s"])
    assert r.stack == [10]
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "1 get .s"])
    assert r.stack == [20]
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "2 get .s"])
    assert r.stack == [30]


def test_set(io):
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "99 1 set", "0 get 1 get 2 get .s"])
    assert r.stack == [10, 99, 30]


def test_print_array(io):
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "print-array"])
    assert r.output == "10 20 30"


def test_print_array_single(io):
    r = io("exercicios-array.fs", ["42 push", "print-array"])
    assert r.output == "42"


def test_add_array(io):
    r = io("exercicios-array.fs", ["10 push 20 push 30 push", "add-array .s"])
    assert r.stack == [60]


def test_add_array_single(io):
    r = io("exercicios-array.fs", ["7 push", "add-array .s"])
    assert r.stack == [7]


def test_add_array_negatives(io):
    r = io("exercicios-array.fs", ["-5 push 10 push -3 push", "add-array .s"])
    assert r.stack == [2]


def test_max_array(io):
    r = io("exercicios-array.fs", ["10 push 50 push 30 push", "max-array .s"])
    assert r.stack == [50]


def test_max_array_negatives(io):
    r = io("exercicios-array.fs", ["-10 push -5 push -30 push", "max-array .s"])
    assert r.stack == [-5]


def test_max_array_single(io):
    r = io("exercicios-array.fs", ["42 push", "max-array .s"])
    assert r.stack == [42]


def test_min_array(io):
    r = io("exercicios-array.fs", ["10 push 50 push 30 push", "min-array .s"])
    assert r.stack == [10]


def test_min_array_negatives(io):
    r = io("exercicios-array.fs", ["-10 push -5 push -30 push", "min-array .s"])
    assert r.stack == [-30]


def test_min_array_single(io):
    r = io("exercicios-array.fs", ["42 push", "min-array .s"])
    assert r.stack == [42]


def test_push_pop_sequence(io):
    r = io("exercicios-array.fs", [
        "1 push 2 push 3 push",
        "pop drop pop drop",
        "size @ .s"
    ])
    assert r.stack == [1]


def test_set_and_get_boundaries(io):
    r = io("exercicios-array.fs", [
        "100 push 200 push 300 push 400 push 500 push",
        "999 0 set",
        "888 4 set",
        "0 get 4 get .s"
    ])
    assert r.stack == [999, 888]
