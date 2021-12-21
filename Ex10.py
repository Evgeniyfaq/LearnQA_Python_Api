

phrase = input("Введите любую фразу короче 15 символов:")
if len(phrase) >= 15:
    assert len(phrase) <= 15, "Фраза больше 15 символов"