def worst_fit(mem_avail, req_size, index):
    if not mem_avail:
        return None
    n = len(mem_avail)
    worst_index = -1
    worst_size = -1
    for i in range(n):
        j = (index + i) % n
        base, size = mem_avail[j]
        if size >= req_size and size > worst_size:
            worst_size = size
            worst_index = j
    if worst_index == -1:
        return None
    base, size = mem_avail[worst_index]
    new_memory = mem_avail[:]  
    remaining_size = size - req_size
    if remaining_size > 0:
        new_memory[worst_index] = (base + req_size, remaining_size)
        out_index = worst_index
    else:
        new_memory.pop(worst_index)
        if worst_index >= index:
            out_index = 0
        else:
            out_index = worst_index
    return (new_memory, base, remaining_size, out_index)
