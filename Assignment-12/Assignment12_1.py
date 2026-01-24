def main():
    character=input("Enter a character: ").lower()
    if character in 'aeiou':
        print("vowel")
    else:
        print("consonent")

if __name__ == "__main__":
    main()