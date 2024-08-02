words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
vowels = 'aeiou'

vowel_counts = [(word, sum(1 for letter in word if letter in vowels)) for word in words]

print(vowel_counts)
