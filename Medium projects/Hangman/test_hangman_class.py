from hangman_class  import SecretWord


def test_secret_word_show_letters():
    word = SecretWord("vancouver")
    assert word.show_letters(["V"]) == "V _ _ _ _ _ V _ _"
    assert word.show_letters(["V", "A"]) == "V A _ _ _ _ V _ _"


def test_secret_word_check_letters():
    word = SecretWord("pizza")
    assert word.check_letters(["P", "I", "Z", "A"]) is True
    assert word.check_letters(["A", "Z", "P", "I"]) is True

    word = SecretWord("Tim")
    assert word.check_letters(["G"]) is False


def test_secret_word_check():
    word = SecretWord("vancouver")
    assert word.check("VanCOuver") is True
    assert word.check("VANCOUVER") is True
    assert word.check("hello") is False
