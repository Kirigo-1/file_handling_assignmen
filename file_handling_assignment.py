#opening my file in write mode.
try:
    with open ("my_file.txt", "w") as file:
        
        #writting <3 lines of code to the text file.
        file.write ("this is a string variable.\n")
        file.write ("12345\n")
        file.write ("Hello, World!!\n")
except Exception as e:
    print("An error occurred:", e)

# Open file again in read mode.
try:
    with open("my_file.txt", "r") as file:
        # we stored the variables in content then print the contents of the file.
        contents = file.read()
        print("Contents of my_file.txt:")
        print(contents)
# use except blocks to handle errors that may occur and give custom print error messages        
except FileNotFoundError:
    print("File not found.")
except PermissionError:
    print("Permission denied.")
except Exception as e:
    print("An error occurred:", e)


    #opening file in append mode.
try:
    with open("my_file.txt", "a") as file:
        # Append three additional lines of text to the existing content
        file.write("This is line 4.\n")
        file.write("6789\n")
        file.write("Appending more text.\n")
except Exception as e:
    print("An error occurred:", e)

    #Task 4 is error handling that ensures the file closes after the except function is run
finally:
    print("File handling completed.")

    #step 2 & 3 not printed in console as except function was run and file was not found.

