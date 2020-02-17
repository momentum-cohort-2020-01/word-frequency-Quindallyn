STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]
import string

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""
    # pass ("replace with my code")
    with open(file) as file:
        open_file = file.read()
        print(type(open_file))
    

    

# test_sentence = "I would love to learn to code in one day!" 
    open_file = open_file.lower()
    new_file= str.maketrans('', '', string.punctuation)

    punctuation_removed = open_file.translate(new_file)
    print(punctuation_removed)

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
