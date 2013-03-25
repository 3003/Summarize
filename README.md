#Summarize#
A collection of Python scripts to research automated summarization.

##Rule Based##

###rulebasedsumm.py###
Rules:
- Keywords in article titles are highly important
- The first sentence of an article is highly important
- The second sentence of an article is important
- Sentences are important when they contain keywords from the article title.

Input:

	ENDANGERED ASIAN 'UNICORN' CAPTURED, FIRST SIGHTING IN DECADE
	(CNN) -- Scientists have confirmed the first sighting in more 
	than a decade of one of the world's rarest animals -- the saola, 
	sometimes called the Asian "unicorn." The animal was captured 
	by villagers in Laos in August, according to the International 
	Union for the Conservation of Nature.

	The villagers took the saola back to their village in 
	Bolikhamxay province and Laotian conservation authorities 
	sent a team to check on the animal. The creature, likely 
	weakened from its time in captivity, died shortly after that 
	team arrived.

	"The death of this saola is unfortunate," the Provincial 
	Conservation Unit of Bolikhamxay province said in the IUCN 
	statement. "But at least it confirms an area where it still 
	occurs and the government will immediately move to strengthen 
	conservation efforts there."

	This was the first confirmed sighting of a saola since 1999, 
	when remotely triggered cameras took images of one in Laos.

	First discovered in 1992, the saola is considered critically 
	endangered, its numbers so few that biologists have never 
	witnessed one in the wild. Fewer than a few hundred saolas 
	are believed to roam the Annamite Mountains of Laos and 
	Vietnam. There are none in captivity.

	The rarity of the saola, which resembles an African antelope 
	but it more closely related genetically to wild cattle, gives 
	it mythical status in some circles, according to the IUCN.

	The saola, although it has two horns, may be the basis of 
	the mythical Chinese unicorn, the qilin, although it is unknown 
	if saolas ever existed in China.

	The carcass of the saola recovered in the Laotian village was 
	being preserved for study, officials said.

	"Study of the carcass can yield some good from this unfortunate 
	incident. Our lack of knowledge of Saola biology is a major 
	constraint to efforts to conserve it," says Dr. Pierre Comizzoli, 
	a veterinarian with the Smithsonian Conservation Biology 
	Institute and a member of the IUCN Saola Working Group.

	"This can be a major step forward in understanding this remarkable 
	and mysterious species.


Output:

	ENDANGERED ASIAN 'UNICORN' CAPTURED, FIRST SIGHTING IN DECADE
	(CNN) -- Scientists have confirmed the first sighting in more 
	than a decade of one of the world's rarest animals -- the saola, 
	sometimes called the Asian "unicorn. The animal was captured by 
	villagers in Laos in August, according to the International 
	Union for the Conservation of Nature. 

	"The death of this saola is unfortunate," the Provincial Conservation 
	Unit of Bolikhamxay province said in the IUCN statement.

	The saola, although it has two horns, may be the basis of the mythical 
	Chinese unicorn, the qilin, although it is unknown if saolas ever 
	existed in China. The carcass of the saola recovered in the Laotian 
	village was being preserved for study, officials said.
	
Todo: extract important news derivatives like:

	This was the first confirmed sighting of a saola since 1999, 
	when remotely triggered cameras took images of one in Laos.