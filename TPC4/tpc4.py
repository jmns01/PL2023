import re
import sys

def parcer(ficheiro):
    text = []
    with open(ficheiro, "r") as file:
        first_line = file.readline().strip()

        pattern = r',(?![^{}]*\})'
        fields =  re.split(pattern, first_line)

        for line in file:
            lines = line.strip().split(",")
            text.append(lines)
    return fields,text

def tpc4(first_line, lines):
    regex = r"^(.+)\{(\d+)(?:,(\d+))?\}(?:::(sum|media))?$"

    for campos in first_line:
        match = re.match(regex, campos)

        if match:
            prefixo = match.group(1)
            min_val = int(match.group(2))
            max_val = int(match.group(3)) if match.group(3) else None
            operacao = match.group(4)

            if max_val == None:
                mylista(first_line, lines)
            elif operacao == None:
                myintervalo(first_line, lines)
            elif operacao == "sum":
                mysum(first_line, lines)
            elif operacao == "media":
                mymedia(first_line, lines)

            return [prefixo, min_val, max_val, operacao] # eleminar estes return dps (apenas para teste)

    return [first_line, lines]

def mylista(first_line, lines):
    pass

def myintervalo(first_line, lines):
    pass

def mysum(first_line, lines):
    pass

def mymedia(first_line, lines):
    pass


if __name__ == "__main__":
    ficheiro = sys.argv[1]

    fst, lines = parcer(ficheiro)
    print(fst)
    print(lines)

    if len(tpc4(fst, lines)) > 2:
        pre, min, max, op = tpc4(fst, lines)
        print(pre)
        print(min)
        print(max)
        print(op)
    else:
        fst1, lines1 = tpc4(fst, lines)
        print(fst1)
        print(lines1)
