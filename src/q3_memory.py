from memory_profiler import memory_usage
from typing import List, Tuple
import json
from collections import Counter
import re

#Función para obtener las 10 menciones (@usuario) más comunes y sus conteos.

def q3_memory(file_path: str) -> List[Tuple[str, int]]:

    mentions = Counter() #Contador para las menciones
    mention_pattern = re.compile(r'@\w+') # Patrón para encontrar menciones (@usuario)
        
    with open(file_path, 'r') as file: # Leer y cargar los datos del archivo JSON
        for line in file:
            tweet = json.loads(line)
            mentions.update(mention[1:] for mention in mention_pattern.findall(tweet['content']))
    
    return mentions.most_common(10)


# Medir uso de memoria y ver resultados
mem_usage = memory_usage((q3_memory, ('farmers-protest-tweets-2021-2-4.json',)))
print(f"Uso de memoria de q3_memory: {max(mem_usage) - min(mem_usage)} MiB")
result_q3_memory = q3_memory('farmers-protest-tweets-2021-2-4.json')
print("Resultado de q3_memory:")
for mentions, count in result_q3_memory:
    print(f"{mentions}: {count}")

print(result_q3_memory) #Salida solicitada por LATAM