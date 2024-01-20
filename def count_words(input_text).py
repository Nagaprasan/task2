def count_words(input_text):
    """
    Count the number of words in the given input text.

    Parameters:
    - input_text (str): The input text to be processed.

    Returns:
    - int: The word count.
    """
    words = input_text.split()
    return len(words)

def main():
    # Prompt the user to enter a sentence or paragraph
    user_input = input("Please enter a sentence or paragraph: ")

    try:
        # Word Counting Logic: Call the function to count words
        word_count = count_words(user_input)

        # Output Display: Print the word count to the console
        print(f"Word Count: {word_count}")

    except ValueError:
        # Error Handling: Handle potential errors, such as empty input
        print("Error: Please enter a valid sentence or paragraph.")

if __name__ == "__main__":
    # User-Friendly Interface: Ensure a clear and user-friendly interface for input and output
    print("=== Word Counter ===")
    main()
