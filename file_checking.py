import psutil
from pathlib import Path

PATH = psutil.disk_partitions()
clear_path = []

exclude_items = [
    '.exe', '.dll', '.sys', '.iso', '.bin',
    'pagefile.sys', 'hiberfil.sys',
    'Steam', 'Epic Games', 'Battle.net',
    'Riot Games', 'Ubisoft', 'Windows',
    'Program Files', 'Program Files (x86)',
]

for i in range(len(PATH)):
    clear_path.append(PATH[i][0])
    
for i in range(len(clear_path)):
    p = Path(clear_path[i])
    for j in p.rglob('*'):
        print(j)
        
    
