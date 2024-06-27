import time
from memory_profiler import memory_usage
from typing import List, Tuple
import json
from collections import Counter
import re

def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    
    #Función para obtener los 10 emojis más comunes y sus conteos.
       emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F300-\U0001F5FF"  # Símbolos y pictogramas misceláneos
        u"\U0001F680-\U0001F6FF"  # Transporte y símbolos de mapas
        u"\U0001F1E0-\U0001F1FF"  # Banderas de países
        "]+", flags=re.UNICODE)

    emojis = Counter()

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            tweet_emojis = emoji_pattern.findall(tweet['content'])

            # Contar la cantidad de veces que cada emoji aparece en el tweet
            for emoji in tweet_emojis:
                emojis[emoji] += len(re.findall(emoji, tweet['content']))

    return emojis.most_common(10)
    
