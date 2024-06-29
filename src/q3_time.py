import time
from typing import List, Tuple
import json
from collections import Counter
import re

#Función para obtener las 10 menciones (@usuario) más comunes y sus conteos.
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_pattern = re.compile(r'@\w+') # Patrón para encontrar menciones (@usuario)
    
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file] # Leer y cargar los datos del archivo JSON
    
    mentions = Counter() #Contador para las menciones
    for tweet in data:
        mentions.update(mention[1:] for mention in mention_pattern.findall(tweet['content']))
    # Encontrar todas las menciones en un tweet y actualizar el contador
    return mentions.most_common(10) #10 menciones más comunes y su conteos

# Medir tiempo de ejecución y ver resultados
start_time = time.time()
result_q3_time = q3_time('farmers-protest-tweets-2021-2-4.json')
end_time = time.time()
print(f"Tiempo de ejecución de q3_time: {end_time - start_time} segundos")
print("Top 10 usuarios con mas menciones:")
for mentions, count in result_q3_time:
    print(f"{mentions}: {count}")

print(result_q3_time) #Salida solicitada por LATAM
