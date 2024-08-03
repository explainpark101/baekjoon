import timeit


def using_map():
    a=('5', '3', '4', '1', '2')
    b= map(int, a)
    sorted(b)

def appending():
    a=('5', '3', '4', '1', '2')
    b=[]
    for _ in a:
        b.append(int(_))
    sorted(b)

def using_list_comprehension():
    a=('5', '3', '4', '1', '2')
    b= [int(_) for _ in a]
    sorted(b)

def using_list_comprehension_generator():
    a=('5', '3', '4', '1', '2')
    b= (int(_) for _ in a)
    sorted(b)

if __name__ == "__main__":
    l = {
        "using_map": using_map,
        "appending": appending,
        "using_list_comprehension": using_list_comprehension,
        "using_list_comprehension_generator": using_list_comprehension_generator,
    }
    for k, f in l.items():
        print(f"{k:34s}: {timeit.timeit(f, number=10_000_000)}s")