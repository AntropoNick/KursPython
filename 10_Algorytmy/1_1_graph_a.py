graph={
    'dom':['kościół','bar','szkoła'],
    'kościół':['dom','bar','kino'],
    'kino':['kościół','szpital','teatr'],
    'teatr':['kino','szpital'],
    'szpital':['bar','kino','teatr','szkoła'],
    'bar':['kościół','dom','szpital'],
    'szkoła':['dom','szpital']
}

for start,building_list in graph.items():
    for building in building_list:
        print (f"{start}--->{building}")
