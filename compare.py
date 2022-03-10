def is_identical(list_a, list_b):
    if len(list_a) != len(list_b):
        print(f"la liste A contient {len(list_a)} element alors que la liste B contient {len(list_b)} elements\n")
    else:
        print("les deux liste font la même taille\n")
    print("les éléments suivants sont présents dans la liste A mais pas dans la B :")
    for i in list_a:
        if i not in list_b:
            print(f"{i}")
    print("")
    print("les éléments suivant sont présent dans la liste B mais pas dans la A : ")
    for i in list_b:
        if i not in list_a:
            print(f"{i}")
    print("")
    print("les éléments suivant sont présent dans les deux listes : ")
    for i in list_a:
        if i in list_b:
            print(f"{i}")


list_a = ['Share-ECAQ', 'Share-IXCI', 'Share-FWBE', 'Share-ZOFA', 'Share-PLLK',
                        'Share-MEQV', 'Share-LXZU', 'Share-YFVZ', 'Share-ANFX', 'Share-PATS', 'Share-SCWM',
                        'Share-ZLMC', 'Share-NDKR', 'Share-ALIY', 'Share-JWGF', 'Share-FAKH', 'Share-FAPS',
                        'Share-ZKSN', 'Share-IJFT', 'Share-LFXB', 'Share-DWSK', 'Share-BMHD', 'Share-XQII',
                        'Share-GEBJ']

list_b = ['Share-ECAQ', 'Share-IXCI', 'Share-FWBE', 'Share-ZOFA', 'Share-PLLK',
                        'Share-LXZU', 'Share-YFVZ', 'Share-ANFX', 'Share-PATS', 'Share-SCWM', 'Share-NDKR',
                        'Share-ALIY', 'Share-JWGF', 'Share-JGTW', 'Share-FAPS', 'Share-VCAX', 'Share-LFXB',
                        'Share-DWSK', 'Share-XQII', 'Share-ROOM']

is_identical(list_a, list_b)
