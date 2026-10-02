def word_frequency(sentence):
    words = sentence.split()
    frequency = {}

    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1

    return frequency


if __name__ == "__main__":
    sentence = input("Enter a sentence: ")

    print("Word frequency:", word_frequency(sentence))
