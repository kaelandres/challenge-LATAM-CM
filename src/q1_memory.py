from memory_profiler import memory_usage
from collections import defaultdict, Counter
from datetime import datetime
from typing import List, Tuple

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_user_count = defaultdict(Counter)
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'], '%Y-%m-%dT%H:%M:%S%z').date()
            user = tweet.get('user', {}).get('username', 'unknown')  # Ajustar clave según inspección
            date_user_count[date][user] += 1
    
    top_dates = Counter({date: sum(users.values()) for date, users in date_user_count.items()})
    top_10_dates = top_dates.most_common(10)
    
    result = [(date, date_user_count[date].most_common(1)[0][0]) for date, _ in top_10_dates]
    
    return result