# python3


def build_heap(data):
    swaps = []
    gar = len(data)
    for i in range(gar//2-1,-1,-1):
        root = i 
        boo = True
        while boo:
            leftnode = 2*i+1
            rightnode = 2*i+2
            if  leftnode <= gar-1 and data[leftnode]<data[root]:
                root = leftnode
            if rightnode <= gar-1 and data[rightnode]<data[root]:
                root = rightnode
            if i!=root:
                swaps.append((i,root))
                data[i], data[root]=data[root],data[i]
                i = root
            else:
                boo = False
    return swaps

            
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)


    return swaps


def main():
    x = input()

    if 'F' in x:
        file_name = input()
        file_name = "test/" + file_name
        try:

            with open(file_name)as file:
                readl = int(file.readline())
                parents = np.array( list(map(int, file.readline().split())))
                print(compute_height(readl, parents))
        except IOError:
            print("no such file")
            return

    elif 'I' in x:
        n = int(input())
        data = list(map(int, input().split()))
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
