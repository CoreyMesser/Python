def convert_from_base10(num_str, base):
    n_int = int(num_str)
    cycle_bl = []
    cycle_bb = []
    nb_c = 99
    while nb_c > 0:
        cb = n_int % base
        cbi = int(cb)
        cycle_bl.append(cbi)
        nb = n_int / base
        nbi = int(nb)
        cycle_bb.append(nbi)
        n_int = nbi
        nb_c -= 1
    base_num = ''.join(str(b_int) for b_int in cycle_bl)[::-1]
    base_num = int(base_num)

    return base_num


def convert_to_base10(num, base):
    n_len = len(str(num))
    d_list = list(str(num))
    nbt = []
    base10 = 0

    for dig_it in d_list:
        n_len -= 1
        nb_i = int(dig_it)*(base**n_len)
        nbt.append(nb_i)

    for digi_t in nbt:
        base10 = digi_t + base10

    base10 = str(base10)
    base_n = base_pad(base10)
    return base_n


def base_pad(b_pad):
    k = len(n)
    b_pad = str(b_pad)
    b_len = len(b_pad)
    if b_len < k:
        badd_list = list(b_pad)
        b_add = k - b_len
        while b_add > 0:
            badd_list.insert(0, '0')
            b_add -= 1
        b_pad = "".join(badd_list)
        # '{base10:0>{k}}'.format(k=k, base10=base10)
    elif b_len > k:
        bdel_list = list(b_pad)
        del bdel_list[0]
        b_pad = "".join(bdel_list)
    else:
        pass
    return b_pad

b = 3
n = "210022"
k = len(n)

int_test = convert_from_base10(n,b)
str_test = convert_to_base10(int_test, b)

print(int_test)
print(str_test)