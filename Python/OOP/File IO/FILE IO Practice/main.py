def main():
    file_name = input("Enter filename: ")
    infile = open(file_name,'r')
    data = infile.read()
    words = data.split()
    print("There are", len(words), "words in the file.")

main()