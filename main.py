def main():
    with open("books/frankenstein.txt") as f:
        global file_contents
        file_contents = f.read()
        print(file_contents)
main()

def wordcount():
    words = len(file_contents.split())
    print(f"there are {words} words inside of this book")
    
wordcount()

def lowercase():
    # Start with an empty dictionary to count characters
    character_count = {}
    # Convert text to lowercase
    lowercaseletters = file_contents.lower()
    # Iterate over each character
    for lowercaseletter in lowercaseletters:
        # Update the count for each character
        character_count[lowercaseletter] = character_count.get(lowercaseletter, 0) + 1

    return character_count
character_counts = lowercase()
print(character_counts)

def sort_on(character_count):
    return character_count["num"]

lettercount = []
for char in character_counts:
    if char.isalpha():
        char_info = {"char": char, "num": character_counts[char]}
        lettercount.append(char_info)

   
lettercount.sort(reverse=True, key=sort_on)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{len(file_contents.split())} words found in the document\n")

for letter_data in lettercount:
    print(f"The '{letter_data['char']}' character was found {letter_data['num']} times")
print("--- End report ---")










