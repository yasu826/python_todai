import json
from sys import argv
                       
with open('all_'+argv[1], 'w') as f:
    
    classes=[]
    g=open(argv[1],'r')
    j=json.load(g)
    for num in range(len(j)):
        if '全教員' == j[num]['name_j']:
            classes.append(j[num])
    g.close()
    
    json.dump(classes,f)