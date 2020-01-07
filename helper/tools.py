def convert2list(param) -> list:
    poem = list()
    for i in param.split('。'):
        for j in i.split('，'):
            poem.append(j)
    return poem