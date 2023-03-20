import re


def tpc5():
    er_levantar = re.compile(r"LEVANTAR")
    er_pousar = re.compile(r"POUSAR")
    er_moeda = re.compile(r"MOEDA (\d+(c|e), )*(\d+(c|e))+")
    er_numero = re.compile(r"T=\d+")
    er_abortar = re.compile(r"ABORTAR")

    while True:
        user_input = input()
        m = er_moeda.match(user_input)
        print(m.group())

tpc5()
