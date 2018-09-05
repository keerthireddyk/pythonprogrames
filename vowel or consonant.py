sample=str(raw_input())
if (sample.isalpha()):
	if (sample=='a'or sample=='e'or sample=='i'or sample=='o'or sample=='u'or sample=='A'or sample=='E'or sample=='I'or sample=='O'or sample=='U'):
		print("Vowel")
	else:
		print("Consonant")
else:
	print("Invalid")
