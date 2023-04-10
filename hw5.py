d=int(input("세 자리 정수 입력:"))
def read_single_digit(d):
    R=["영","일","이","삼","사","오","육","칠","팔","구"]
    return R[d]
def read_number(d):
    if d<10:
        return read_single_digit(d)
    elif d<100:
        t=d//10
        o=d%10
        return read_single_digit(t)+read_single_digit(o)
    elif d>100 and d<1000:
        th=d//100
        t=(d%100)//10
        o=(d%100)%10
        return read_single_digit(th)+read_single_digit(t)+read_single_digit(o)
print(read_number(d))