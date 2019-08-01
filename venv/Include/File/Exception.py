'''
python exception handelling

'''

try:
    input_number = int(input("Enter the value for calculate:\n"))
    result_value = input_number / 0
    print("Result is:", result_value)

except ZeroDivisionError:
    print("Zerro cannot devided")

except NotADirectoryError:
    print("Cannot find directory")

except IndentationError:
    print("Indication error")

except FileExistsError:
    print("File exist error")

except FileNotFoundError:
    print("File not found error")




