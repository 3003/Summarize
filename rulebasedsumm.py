# coding: utf-8
from re import split

def get_words(text):
	return text.split()

def get_word_counts(text):
	word_counts = {}
	words = get_words(text)
	for word in words:
		word = word.lower()
		word_counts.setdefault(word,0)
		word_counts[word]+=1
	return word_counts

def create_sentences(text):
	text = text.replace('\n', '').replace('\r', '').replace('\t', '')
	sentences = split(r' *[\.\?!][\'"\)\]]* *', text)
	sentences = filter(None, sentences)
	return sentences

def scores(title, sentences, word_counts):
	title_scores = get_word_counts(title)
	first_sentence_scores = get_word_counts(sentences[0])
	second_sentence_scores = get_word_counts(sentences[1])
	score = 0
	i = 0
	scores = []
	for sentence in sentences:
		i += 1
		words = get_words(sentence)
		for word in words:
			score += (5 * word_counts.setdefault(word.lower(), 0))
			score += (23 * title_scores.setdefault(word.lower(), 0))
			score += (23 * first_sentence_scores.setdefault(word.lower(), 0))
			score += (1 * second_sentence_scores.setdefault(word.lower(), 0))
		scores.append((sentence, score, score/float(len(sentence)), i, len(sentence)))
		score = 0
	return sorted(scores, key=lambda x: x[2], reverse=True)

title = "Endangered Asian 'unicorn' captured, first sighting in decade"

text = '''
(CNN) -- Scientists have confirmed the first sighting in more than a decade of one of the world's rarest animals -- the saola, sometimes called the Asian "unicorn."

The animal was captured by villagers in Laos in August, according to the International Union for the Conservation of Nature.

The villagers took the saola back to their village in Bolikhamxay province and Laotian conservation authorities sent a team to check on the animal. The creature, likely weakened from its time in captivity, died shortly after that team arrived.

"The death of this saola is unfortunate," the Provincial Conservation Unit of Bolikhamxay province said in the IUCN statement. "But at least it confirms an area where it still occurs and the government will immediately move to strengthen conservation efforts there."

This was the first confirmed sighting of a saola since 1999, when remotely triggered cameras took images of one in Laos.

First discovered in 1992, the saola is considered critically endangered, its numbers so few that biologists have never witnessed one in the wild. Fewer than a few hundred saolas are believed to roam the Annamite Mountains of Laos and Vietnam. There are none in captivity.

The rarity of the saola, which resembles an African antelope but it more closely related genetically to wild cattle, gives it mythical status in some circles, according to the IUCN.

The saola, although it has two horns, may be the basis of the mythical Chinese unicorn, the qilin, although it is unknown if saolas ever existed in China.

The carcass of the saola recovered in the Laotian village was being preserved for study, officials said.

"Study of the carcass can yield some good from this unfortunate incident. Our lack of knowledge of Saola biology is a major constraint to efforts to conserve it," says Dr. Pierre Comizzoli, a veterinarian with the Smithsonian Conservation Biology Institute and a member of the IUCN Saola Working Group.

"This can be a major step forward in understanding this remarkable and mysterious species."'''

# Returns title and dictionary of word counts for an RSS feed

scores = scores(title, create_sentences(text), get_word_counts(text))
reorder = []
for score in scores[0:5]:
	reorder.append((score[0], score[3]))
reordered = sorted(reorder, key=lambda x: x[1])
print title.upper()
for sentence in reordered:
	print sentence[0] + "."