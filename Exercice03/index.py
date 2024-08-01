words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowel_counts = []

def count_vowels(word):
    vowels = 'aeiou'
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return count

vowel_counts = [(word, count_vowels(word)) for word in words]

print(vowel_counts)
