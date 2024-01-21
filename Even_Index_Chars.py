# Print characters from a string that are present at an even index number

# pseudocode

# Define the function to display even indices vertically
def display_even_indices_vertically(input_str):
    even_indices_chars=input_str[::2]
    for char in even_indices_chars:
        print(char)

# Print and display the result
user_input=input("Enter a word: ")
print(f"Original word is {user_input}")
print("Printing only even index chars")
display_even_indices_vertically(user_input)