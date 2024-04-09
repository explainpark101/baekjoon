import math
one = "+!![]"

FUCK = {
    0:"+![]",
    1:"+!![]",
    2:"+!![]+!![]",
    3:"+!![]+!![]+!![]",
    4:"+!![]+!![]+!![]+!![]",
    5:"[+!![]+!![]]*[+!![]+!![]]+!![]",
    6:f"[{one}{one}]*[{one}{one}{one}]",
    7:f"[{one}{one}]**[{one}{one}{one}]-{one}"
}

def prime_factorization(number:int, factorized={}):
    _num = number
    res = {}
    i = 2
    while number != 1:
        if factorized.get(number):
            for key, val in factorized.get(number).items():
                res[key] = res.get(key, 0) + val
            factorized[_num] = res
            return res
        
        r = number % i
        if r!=0:
            i += 1
        else:
            number //= i
            res[i] = res.get(i,0) + 1
            
    factorized[_num] = res
    return res
            
        

def main():
    for i in range(2, 1001):
        print(f"{i:4d} ", "*".join([f"{key}**{val}" for key, val in prime_factorization(i).items()]))
        
main()