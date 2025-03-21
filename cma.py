#!/usr/bin/python3
import click
import sys
from cont_mem_algos import worst_fit

def print_memory_map(memory_map):
    for memory in memory_map:
        print(f"({memory[0]:#0{8}x}, {memory[1]:#0{8}x})")

def read_reqs_file(reqs_filename):
    result = []
    try:
        with open(reqs_filename, 'r') as reqsfile:
            for line in reqsfile:
                req = int(line.strip(), 16)
                result.append(req)
    except FileNotFoundError:
        print(f'File not found {reqs_filename}', file=sys.stderr)
        return None
    return result

def read_memmap_file(memmap_filename):
    result = []
    try:
        with open(memmap_filename, 'r') as mmfile:
            for line in mmfile:
                elems = line.strip().split()
                result.append((int(elems[0], 16), int(elems[1], 16)))
    except FileNotFoundError:
        print(f'File not found {memmap_filename}', file=sys.stderr)
        return None
    return result

@click.command()
@click.option('--memmap', help='file with the memory description')
@click.option('--reqs', help='requirement file')
@click.option('--pos', default=0, help='initial position')
def process(memmap, reqs, pos):
    memory = read_memmap_file(memmap)
    requirements = read_reqs_file(reqs)
    
    if memory is None or requirements is None:
        return
    
    index = pos
    work_memory = memory[:]
    print("Worst Fit")
    print_memory_map(work_memory)
    
    for req in requirements:
        result = worst_fit(work_memory, req, index)
        
        if result is None:
            print(f"Not found: {req:#0{8}x}")
        else:
            # Desempaquetamos el resultado correctamente:
            work_memory, base, _, new_index = result
            print(f"Assigned to the process base: {base:#0{8}x}")
            print(f"Index: {new_index}")
            print_memory_map(work_memory)
            index = new_index  # Actualizar índice según nueva asignación

if __name__ == '__main__':
    process()
