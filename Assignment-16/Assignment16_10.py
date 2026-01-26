def StringLength(name):
    count=0
    for i in name:
        count+=1
    return count

def main():
    String = input("Enter name : ")
    print(StringLength(String))

if __name__ == "__main__":
    main()