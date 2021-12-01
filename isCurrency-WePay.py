def isCurrency(strAmount):
    # Write your code here
    # check invalid
    # two pointers l and r to iterate characters
    # check leading or trailing whitespce
    l, r = 0, len(strAmount)
    DOLLARS = '$'
    EUROS = '€'
    WESTERN = {DOLLARS, EUROS}
    YENS = '¥'
    valid_currency_symbols = WESTERN | {YENS}
    if strAmount != strAmount.strip():
        return False
    # check complete parentheses, matches or doesn't include at same time
    if (strAmount[0] == '(') != (strAmount[-1] == ')'):
        return False
    # after validation, remove parenthese if exsit
    if strAmount[0] == '(':
        l += 1
        r -= 1
        if strAmount[0] == '-':
            return False
    # remove negative symbol
    if strAmount[0] == '-':
        l += 1
    if strAmount[l] not in valid_currency_symbols:
        return False
    # store yens
    is_yen = strAmount[l] == YENS
    l += 1
    # if ',' in the string
    contain_comma = ',' in strAmount[l:r]
    # counts for every three digits
    counts = 0
    while l < r:
        if strAmount[l] == '.':
            if not valid_decimals(strAmount[l+1:], is_yen):
                return False
            l += 1
            continue
        if strAmount[l] == ',':
            if not valid_thousands(strAmount[l+1:l+4]):
                return False
            l += 3
            counts = 0
            continue
        if not strAmount[l].isdigit():
            return False
        if contain_comma and counts >= 3:
            return False
        l += 1
        counts += 1
    return True


def valid_thousands(s):
    # valid thousands must be 3 digits
    return len(s) == 3 and s.isdigit()


def valid_decimals(s, is_yen):
    # valid decimals must be 2 digits, and not ￥
    return not is_yen and len(s) == 2 and s.isdigit()


if __name__ == '__main__':
    inputs = ['$0.35', '¥1200,000', '$65.', '(¥2400)', '¥120.00']
    for strAmount in inputs:
        print(strAmount)
        print(isCurrency(strAmount))
