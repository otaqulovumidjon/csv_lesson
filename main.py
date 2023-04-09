def get_country_column(file_name):
    """
    This function takes a filename as input and returns a list of countries
    Args:
        file_name: string
    Returns:
        list
    """
    ls = []
    f = open(file_name).read()
    n = f.split("\n")
    n.pop(0)
    for i in n:
        if len(i) != 0:
            a = i.split(",")
            ls.append(a[3])
    return ls
print(get_country_column("data.csv"))