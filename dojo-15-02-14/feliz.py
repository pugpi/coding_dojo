def feliz(n, results=None):
    if results is None:
        results = []
    numero = str(n)
    aux = 0
    for i in numero:
        aux += int(i) ** 2
    print aux,
    if aux == 1:
        print(True)
        return True
    else:
        if aux in results:
            print(False)
            return False
        else:
            results.append(aux)
            return feliz(aux, results)