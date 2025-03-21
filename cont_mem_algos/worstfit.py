def worst_fit(memoria, requerimiento, index):
    if not memoria or requerimiento <= 0:
        return None

    n = len(memoria)
    peor_index = -1
    peor_base = -1
    peor_limite = -1

    for i in range(n):
        actual_index = (index + i) % n
        base, limite = memoria[actual_index]

        if limite >= requerimiento and limite > peor_limite:
            peor_index = actual_index
            peor_base = base
            peor_limite = limite

    if peor_index == -1:
        return None  

    nueva_memoria = memoria[:]

    if peor_limite == requerimiento:
        nueva_memoria.pop(peor_index)
    else:
        nueva_base = peor_base + requerimiento
        nuevo_limite = peor_limite - requerimiento
        nueva_memoria[peor_index] = (nueva_base, nuevo_limite)

    return nueva_memoria, peor_base, peor_limite, peor_index
