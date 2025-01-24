import dis
def multiply(x,y):
    for i in range (2,5):
        print(x*y)


if __name__ == "__main__":
    dis.dis(multiply)