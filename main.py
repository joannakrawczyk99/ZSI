def main():
    f = open("test.txt", "r")

    lines = f.readlines()
    for line in lines:
        for c in line:
            if c.isdigit() == True:
                print(format(c))

    f.close()

if __name__ == "__main__":
    main()