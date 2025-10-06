from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
id = 0
def main():
    global id
    entrada = stdin.readline().split()
    while entrada[0] != "END" and entrada[1] != "0":
        lista = []
        dict_var, dict_fun, = {}, {}
        cant = int(entrada[1])
        es_compatible = True
        i, id = 0, 0
        while i < cant:
            hash = stdin.readline().strip()
            if es_compatible: 
                leer(hash, lista, dict_fun, 0)
                if i > 0: 
                    val1 = valor_atomico(lista[i-1], dict_var)
                    val2 = valor_atomico(lista[i], dict_var)
                    es_compatible = verificar(val1, val2, dict_var, dict_fun)
            i += 1
        if es_compatible: print("analysis inconclusive on {}".format(entrada[0]))
        else: print("{} is a Starflyer agent".format(entrada[0]))

        entrada = stdin.readline().split()

def leer(entrada, lista, dict_fun, indice):
    global id
    buffer = []
    i = indice
    while i < len(entrada) and entrada[i] != ")":
        if entrada[i] == "(":
            dict_fun[id] = []
            val = ''.join(buffer)
            lista.append((1, val, id))
            id += 1
            i = leer(entrada, dict_fun[id-1], dict_fun, i+1)
            buffer = []

        if entrada[i] == ",":
            if len(buffer) > 0:
                val = ''.join(buffer)
                lista.append((var_cte(buffer), val, None))
                buffer = []
            i += 1
        if entrada[i] != ")": buffer.append(entrada[i])
        i += 1

    if len(buffer) > 0:
        val = ''.join(buffer)
        lista.append((var_cte(buffer), val, None))
    return i

def var_cte(buffer):
    if ord(buffer[0]) >= 65 and ord(buffer[0]) <= 90: tipo = 0
    else: tipo = 2
    return tipo

def phi(lista1, lista2, dict_var, dict_fun):
    ans = True
    if len(lista1) != len(lista2): ans = False
    else:
        i = 0
        while i < len(lista1) and ans:
            val1 = valor_atomico(lista1[i], dict_var)
            val2 = valor_atomico(lista2[i], dict_var)
            ans = verificar(val1, val2, dict_var, dict_fun)
            i += 1
    return ans

def verificar(val1, val2, dict_var, dict_fun):
    ans = True
    a, b= val1, val2
    if val1[0] == 0: a = dict_var[val1] 
    if val2[0] == 0: b = dict_var[val2]
    if val1 != val2 and ans:
        if b == None:
            if a != None and a[0] == 1: ans = verificar_ciclos(a[2], dict_var, dict_fun, val2)
            if ans: dict_var[val2] = val1
        elif a == None:
            if b != None and b[0] == 1: ans = verificar_ciclos(b[2], dict_var, dict_fun, val1)
            if ans: dict_var[val1] = val2
        elif b[0] != a[0] or b[0] == a[0] and b[1] != a[1]: ans = False
        elif b[0] == a[0] and b[1] == a[1] and a[2] != b[2]:
            ans = phi(dict_fun[a[2]], dict_fun[b[2]], dict_var, dict_fun)
    return ans

def verificar_ciclos(id, dict_var, dict_fun, variable):
    ans = True
    i = 0
    lista = dict_fun[id]
    while i < len(lista) and ans:
        val = lista[i]
        if val[0] == 0:
            var = valor_atomico(val, dict_var)
            if var[1] == variable[1]: ans = False
            val = dict_var[var]
        if ans and val != None and val[0] == 1: ans = verificar_ciclos(val[2], dict_var, dict_fun, variable)
        i += 1
    return ans

def valor_atomico(val, dict_var):
    ans = val
    if val[0] == 0:
        if val not in dict_var: dict_var[val] = None
        else: ans = encontrar_hojas(dict_var, val)
    return ans

def encontrar_hojas(dict_var, var):
    val = var
    if var in dict_var and dict_var[var] in dict_var:
        val = encontrar_hojas(dict_var, dict_var[var])
        dict_var[var] = val
    return val

main()