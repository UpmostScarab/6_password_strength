from blacklist import BLACKLIST
import getpass
import re


def get_password_strength(password):
    if password in BLACKLIST:
        return '1 - Пароль входит в список частых паролей'
    if len(password) < 8:
        return '1 - Пароль слишком короткий'
    score = 2
    length = len(password)
    if length > 26:
        score += 3
    elif length > 15:
        score += 2
    elif length > 10:
        score += 1
    chars_in_pass = re.findall(r'(\W)', password)
    if chars_in_pass:
        if len(chars_in_pass) > 1:
            score += 2
        else:
            score += 1
    if password.lower() != password:
        score += 3
    if score >= 2 and score < 6:
        return '%d - Неплохой пароль, но всё ещё слабый' % score
    elif score < 9:
        return '%d - Хороший пароль, но можно лучше' % score
    elif score >= 9:
        return '%d - Сильный пароль' % score


if __name__ == '__main__':
    #input_password = input('password')
    input_password = getpass.getpass('Введите пароль: ')
    print(get_password_strength(input_password))
