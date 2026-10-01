def vowels_consonants(text):
    vowels = "aeiou"
    vowels_count = 0
    consonants_count = 0

    for char in text.lower():
        if char in vowels:
            vowels_count += 1
        elif char.isalpha():
            consonants_count += 1

    return vowels_count, consonants_count


if __name__ == "__main__":
    text = input("Enter a string: ")
    vowels, consonants = vowels_consonants(text)

    print("Vowels:", vowels)
    print("Consonants:", consonants)
