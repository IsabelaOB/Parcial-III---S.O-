Nota inicial: Modifiqué "cma.py" para solo manejar worst_fit ya que es lo que me compete. Además en caso de no ser necesario todo el codigo anterior, mi archivo "worst_fit.py" está en cont_mem_algos


Gestión de Memoria – Algoritmo Worst-Fit
Este proyecto implementa un algoritmo de asignación de memoria basado en la estrategia Worst-Fit con búsqueda circular. El objetivo es asignar bloques de memoria a solicitudes, buscando siempre el bloque con mayor espacio disponible que cumpla con la solicitud. La asignación se realiza a partir de un índice inicial en la lista de bloques de memoria, lo que permite recorrer la lista de forma circular.

Estructura del Proyecto
cma.py: Script principal que utiliza el algoritmo Worst-Fit para asignar memoria a procesos.
cont_mem_algos.py: Contiene la implementación del algoritmo worstfit.
resources/: Directorio que incluye archivos de ejemplo:
memmap_1.txt: Archivo con la descripción de los bloques de memoria (base y tamaño).
reqs_1.txt: Archivo con las solicitudes de memoria.
tests/: Directorio que contiene los tests unitarios para validar el correcto funcionamiento del algoritmo.

FUNCIONAMIENTO DEL ALGORITMO
La función worstfit(memory, req, index) recibe tres parámetros:

- memory: Lista de tuplas (base, size) que representan los bloques de memoria disponibles.
- req: Cantidad de memoria requerida.
- index: Índice desde el cual se inicia el recorrido circular de la lista.


La función realiza lo siguiente:

1.Recorre la lista de memoria de forma circular, a partir del índice dado.
2.Selecciona el bloque que tenga suficiente espacio y sea el que tenga mayor tamaño (Worst-Fit).
3.Si encuentra un bloque:
  - Si el bloque queda con memoria remanente, se actualiza el bloque restando el espacio asignado y se mantiene en la lista.
  - Si el bloque se consume por completo, se elimina de la lista.
4.Devuelve una tupla con:
  - La lista de bloques actualizada.
  - La base del bloque asignado.
  - El tamaño remanente (si lo hay).
  - El índice en la lista donde terminó la asignación (para continuar búsquedas futuras).
Nota: Aunque la función retorna un valor adicional (el tamaño remanente), se cumple con lo requerido: se obtiene la nueva base donde se asignó la memoria, la memoria actualizada y el índice para la próxima asignación.


REQUISITOS:
Python 3.x (versión preferiblemente actualizada)
Click: Versión >= 8.1.8 para manejar la línea de comandos.


USO:
Ejecuta el script principal especificando el archivo de mapeo de memoria y el archivo de requerimientos:

python cma.py --memmap resources/memmap_1.txt --reqs resources/reqs_1.txt --pos 0

Esto leerá la memoria y las solicitudes, asignará la memoria utilizando Worst-Fit y mostrará por consola la asignación y el estado actualizado de la memoria.


EJECUCIÓN DE TESTS:
Para verificar el correcto funcionamiento del algoritmo, se han desarrollado tests unitarios que cubren diversos escenarios y casos límite. Estos tests aseguran que:

  - La función retorne None cuando la memoria está vacía o cuando la solicitud supera el tamaño de cualquier bloque disponible.
  - Se seleccione correctamente el bloque que tenga mayor espacio disponible, de acuerdo con la estrategia Worst-Fit.
  - La lista de memoria se actualice adecuadamente al consumir un bloque (parcial o completamente).
  - La búsqueda circular funcione correctamente, devolviendo el índice esperado para continuar con futuras asignaciones.


Ejecuta los tests con el siguiente comando desde la raíz del proyecto:

python -m unittest discover -s tests

Si todos los tests pasan, significa que el algoritmo se comporta conforme a lo esperado.

NOTAS ADICIONALES:
  - La estrategia de búsqueda circular permite distribuir las asignaciones a lo largo de la lista de memoria, evitando favorecer siempre los primeros bloques.
  - La implementación maneja correctamente tanto la actualización de bloques parciales como la eliminación de bloques que se consumen por completo.
