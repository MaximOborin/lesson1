def get_summ(one, two, delimiter='&'):
    mom = str(one).upper()
    pop = str(two).upper()
    delimiter = "&"
    return mom + delimiter + pop
print(get_summ("lern", "python", delimiter='&'))