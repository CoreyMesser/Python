def answer(n, b):
    global k
    k = len(str(n))
    cycle_l = []
    cycle_re = []

    while True:
        x_list = list(str(n))
        x = "".join(sorted(x_list, reverse=True))
        y = "".join(sorted(x_list))

        xx = convert_to_base10_int(x, b)
        yy = convert_to_base10_int(y, b)
        z_int = xx - yy
        z_str = convert_from_base10_str(z_int, b)

        if z_str not in cycle_l:
            cycle_l.append(z_str)
            n = z_str
        else:
            if z_str in cycle_re:
                cycle_end = len(cycle_re)
                break
            cycle_l.append(z_str)
            cycle_re.append(z_str)
            n = z_str
    return cycle_end


def convert_from_base10_str(num, base):
    n_int = num
    cycle_bl = []
    nbi = 99
    while nbi != 0:
        cb = n_int % base
        cbi = int(cb)
        cycle_bl.append(cbi)
        nb = n_int / base
        n_int = int(nb)
    base_num = ''.join(str(b_int) for b_int in cycle_bl)[::-1]

    return base_num


def convert_to_base10_int(num_str, base):
    n_len = len(num_str)
    d_list = list(num_str)

    nbt = []
    base10 = 0

    for dig_it in d_list:
        n_len -= 1
        nb_i = int(dig_it)*(base**n_len)
        nbt.append(nb_i)

    for digi_t in nbt:
        base10 = digi_t + base10

    return base10


def base_pad(b_pad):
    b_pad = str(b_pad)
    b_len = len(b_pad)
    if b_len < k:
        badd_list = list(b_pad)
        b_add = k - b_len
        while b_add > 0:
            badd_list.insert(0, '0')
            b_add -= 1
        b_pad = "".join(badd_list)
    elif b_len > k:
        bdel_list = list(b_pad)
        del bdel_list[0]
        b_pad = "".join(bdel_list)
    else:
        pass
    return b_pad
