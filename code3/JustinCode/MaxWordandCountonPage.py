import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://cmgpartners.com/case-study/marketing-strategy-institute/')
counts = dict()

for line in fhand:
	words = line.decode().split()
	for word in words:
		counts[word] = counts.get(word, 0) + 1

maxword = max(counts, key=counts.get)
print('word -', maxword)

maxcount = counts[max(counts, key=counts.get)]
print('count -', maxcount)



	