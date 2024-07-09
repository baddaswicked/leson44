from random import randint

def rand_gen(start, stop,qount):
    count=0
    while count<qount:
        yield randint(start,stop)
        count+=1

if __name__ == '__main__':
    for n in rand_gen(1,20,5):
        print(n,end=" ")


