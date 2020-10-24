
def write_something():
    with open("my.csv","at") as f:
        f.write("\n5.3,5.1,3.2")


if __name__=='__main__':
    write_something()