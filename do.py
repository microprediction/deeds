import time

def write_something():
    stamp = time.time.now()
    print('writing '+stamp)
    with open("my.csv","at") as f:
        f.write("\n5.3,5.1,"+str(stamp))


if __name__=='__main__':
    write_something()