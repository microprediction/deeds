import datetime


def write_something():
    stamp = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    print('writing '+stamp)
    with open("timestamp2.py","at") as f:
        f.write("\n"+stamp)


if __name__=='__main__':
    write_something()
