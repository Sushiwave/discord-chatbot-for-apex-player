def delm(list, indices):
    return [e for i,e in enumerate(list) if i not in indices]