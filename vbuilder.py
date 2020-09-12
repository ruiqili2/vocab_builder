def read_file():
    with open("gre3000.csv", "r") as fp:
        data = fp.readlines()
        lno, vdict = 1, {}
        for i in range(0, int(len(data) / 200)):
            vdict[lno] = [d.split(',')[0:2] for d in data[i * 200: i * 200 + 200]]
            lno += 1

        vdict[lno] = [d.split(',')[0:2] for d in data[int(len(data) / 200) * 200:]]
    return vdict, int(len(data) / 200) + 1


def run_vbuilder(lot):
    while len(lot) > 0:
        print("---------------------")
        v = lot.pop(0)
        print(f"? {v[0]}")
        if input("y/n: ") == "n":
            print(f"! {v[1]}")
            lot.append(v)
        else:
            print(f"! {v[1]}")
            if input("Remove? ") == "n":
                lot.append(v)

    print("List of today done! Good job!")


def main():
    vdict, total = read_file()
    lno = int(input(f"Please enter the list number you would like to work on (1-{total}): "))
    while lno > total or lno < 1:
        lno = int(input(f"Please enter the list number you would like to work on (1-{total}): "))

    lot = vdict[lno]
    run_vbuilder(lot)


if __name__ == '__main__':
    main()
