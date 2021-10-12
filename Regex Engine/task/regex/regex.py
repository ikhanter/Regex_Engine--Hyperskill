import sys

sys.setrecursionlimit(10000)


def check_symbol(regex_char, string_char):
    # print('--', regex_char)
    # print('--', string_char)

    if regex_char == '.':
        regex_char = string_char
    if not regex_char:
        return True
    elif not string_char:
        return False
    elif regex_char == string_char:
        return True
    else:
        return False


def check_literal(regex_char, string_char):
    if not regex_char:
        return True
    elif not string_char:
        return False
    elif regex_char == string_char:
        return True
    else:
        return False


def check_equal(regex_string, line_string):
    # print(regex_string, ' - ', line_string)
    if not regex_string:
        return True
    if line_string:
        if regex_string[0] == '\\':
            if check_literal(regex_string[1], line_string[0]):
                return check_equal(regex_string[2:], line_string[1:])
            else:
                return check_equal(regex_string, line_string[1:])
        if len(regex_string) >= 2:
            if regex_string[1] == '?':
                return check_equal(regex_string[:1] + regex_string[2:], line_string) or check_equal(regex_string[2:],
                                                                                                      line_string)
            elif regex_string[1] == '*':
                return check_equal(regex_string[2:], line_string) or check_equal(regex_string, line_string[1:])
            elif regex_string[1] == '+':
                return check_equal(regex_string[0] + regex_string[2:], line_string) or check_equal(regex_string,
                                                                                                   line_string[1:])

        if check_symbol(regex_string[0], line_string[0]):
            return check_equal(regex_string[1:], line_string[1:])
        return False

    else:
        if regex_string[0] == '$':
            return True
        else:
            return False


def check_different(regx, ln):
    if not regx:
        return True
    if ln:
        if check_equal(regx, ln[:len(regx)]):
            return True
        else:
            return check_different(regx, ln[1:])
    else:
        return False


def check_borders(line1, line2):
    if not line1:
        return True
    elif not line2:
        return False
    if line1[0] == '^':
        return check_equal(line1[1:], line2)
    if line1[-1] == '$':
        return check_equal(line1, line2[len(line2) - len(line1) + 1:])
    else:
        return check_different(line1, line2)


s = input()
regex, line = s.split('|')

print(check_borders(regex, line))
