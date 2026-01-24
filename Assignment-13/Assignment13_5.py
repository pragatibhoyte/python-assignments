def main():
    print("Enter Marks: ")
    marks=int(input())

    if(marks>=74):
        print("Distinction")
    elif(marks>=60):
        print("First Class")
    elif(marks>=50):
        print("Second Class")
    elif(marks<50):
        print("Fail")

if __name__ == "__main__":
    main()
