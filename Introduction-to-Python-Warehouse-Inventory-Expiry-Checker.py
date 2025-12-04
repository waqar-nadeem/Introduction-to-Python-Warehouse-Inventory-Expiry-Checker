rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

for i in range(0, rows):
    expired = 0
    not_expired = 0
    print("\nRow", i + 1)
    
    for j in range(0, columns):
        status = input(f"Enter status for Shelf[{i+1},{j+1}] (Y/N): ")
        if status.upper() == "Y":
            expired += 1
        else:
            not_expired += 1

    print(f"Row {i + 1} Summary: Expired = {expired}, Not expired = {not_expired}")
