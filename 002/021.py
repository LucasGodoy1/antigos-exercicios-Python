def notas (*outros, sit=False):
    
    r = dict()
    r['total'] = len(outros)
    r['maior'] = max(outros)
    r['menor'] = min(outros)
    r['media'] = sum(outros) / len(outros)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'Boa'
    elif r['media'] >=5:
        r['situação'] = 'RAZOAVEL'
    else:
        r['situação'] = 'Ruim'
    
    return r


resp = notas(10, 5, 7, 6.5, sit=True)
print (resp)
    