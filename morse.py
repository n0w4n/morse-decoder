# Created by n0w4n
# This python script is created for solving the morse code puzzle
# of challenge CaptureTheFlag at TryHackMe.com

# MorseTable comes from http://www.morsecodeclassnet.com/files/MorseAlphabetCheatSheet-Timing-RST-CW-Abbr.pdf


morseTable = {
	'di-dah':'a',
	'dah-di-di-dit':'b',
	'dah-di-dah-dit':'c',
	'dah-di-dit':'d',
	'dit':'e',
	'di-di-dah-dit':'f',
	'dah-dah-dit':'g',
	'di-di-di-dit':'h',
	'di-dit':'i',
	'di-dah-dah-dah':'j',
	'dah-di-dah':'k',
	'di-dah-di-dit':'l',
	'dah-dah':'m',
	'dah-dit':'n',
	'dah-dah-dah':'o',
	'di-dah-dah-dit':'p',
	'dah-dah-di-dah':'q',
	'di-dah-dit':'r',
	'di-di-dit':'s',
	'dah':'t',
	'di-di-dah':'u',
	'di-di-di-dah':'v',
	'di-dah-dah':'w',
	'dah-di-di-dah':'x',
	'dah-di-dah-dah':'y',
	'dah-dah-di-dit':'z',
	'di-dah-dah-dah-dah':'1',
	'di-di-dah-dah-dah':'2',
	'di-di-di-dah-dah':'3',
	'di-di-di-di-dah':'4',
	'di-di-di-di-dit':'5',
	'dah-di-di-di-dit':'6',
	'dah-dah-di-di-dit':'7',
	'dah-dah-dah-di-dit':'8',
	'dah-dah-dah-dah-dit':'9',
	'dah-dah-dah-dah-dah':'0',
	'di-di-dah-dah-di-dit':'?',
	'dah-di-di-dah-dit':'/',
	'dah-dah-di-di-dah-dah':',',
	'di-dah-di-dah-di-dah':'.',
}

cipherText = "dah dah-dah-dah di-dah-di-dit dah-di-dit dah-di-dah-dah dah-dah-dah di-di-dah dah di-di-di-dit dit dah-di-dah-dah di-dah di-dah-dit dit di-di-dah di-di-dit di-dit dah-dit dah-dah-dit di-dah dah-dit dah-di-dah-dah dah di-di-di-dit di-dit dah-dit dah-dah-dit dah dah-dah-dah dit dah-dit dah-di-dah-dit di-dah-dit dah-di-dah-dah di-dah-dah-dit dah dah di-di-di-dit dit di-di-dit dit dah-di-dit di-dah dah-di-dah-dah di-di-dit di-dah-di-dah-di-dah di-di-dah-dit di-dah-di-dit di-dah dah-dah-dit di-dit di-di-dit di-dit dah-dit dah di-di-di-dah-dah di-dah-dit dah-dit di-di-di-di-dah dah di-dit dah-dah-dah-dah-dah dah-dit di-di-di-di-dah di-dah-di-dit dah-dah dah-dah-dah-dah-dah di-dah-dit di-di-dit di-di-di-dah-dah dah-di-dah-dit dah-dah-dah-dah-dah dah-di-dit di-di-di-dah-dah"

for word in cipherText.split():
	if word in morseTable:
		print(morseTable[word], sep='', end='')
print()