from blacklist import BLACKLIST
special_chars = list("!@#$%^&*()_+-=`~\'\"\\/№;:?.,")


def get_password_strength(password):
    if password in BLACKLIST:
        return '1 - Пароль входит в список частых паролей'
    if len(password) < 8:
        return '1 - Пароль слишком короткий'
    score = 2
    length = len(password)
    if length > 10:
        if length > 15:
            if length > 26:
                score += 3
            else:
                score += 2
        else:
            score += 1
    chars_in_pass = [char in password for char in special_chars]
    if any(chars_in_pass):
        if len(chars_in_pass) > 1:
            score += 2
        else:
            score += 1
    if password.lower() != password:
        score += 3
    if score >= 2 and score < 6:
        return str(score) + ' - Неплохой пароль, но всё ещё слабый'
    elif score < 9:
        return str(score) + ' - Хороший пароль, но можно лучше'
    elif score >= 9:
        return str(score) + ' - Сильный пароль'


if __name__ == '__main__':
    input_password = input('Введите пароль: ')
    print(get_password_strength(input_password))
