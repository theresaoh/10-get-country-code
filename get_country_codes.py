def get_country_codes(param):
    split = prices.split(' ')
    code_list = []
    for val in split:
        code_list.append(val[:2])
    glue = ", "
    codes = glue.join(code_list)
    return codes
