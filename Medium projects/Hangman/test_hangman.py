from hangman import reveal_letters, all_letters_found

def test_reveal_letters():
    assert reveal_letters("Vancouver", ["V", "A"]) == "V A _ _ _ _ V _ _"
    assert reveal_letters("TIM", ["G", "V"]) == "_ _ _"

def test_all_letters_found():
    assert all_letters_found("PIZZA", ["P", "I", "Z", "A"]) == True
    assert all_letters_found("HELLO", ["H", "E", "L"]) == False