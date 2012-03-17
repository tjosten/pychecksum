#!/usr/bin/env python

from string import digits as string_digits

class ChecksumError(Exception):

	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class Checksum:

	_letterdict = {
		'A': 10,
		'B': 11,
		'C': 12,
		'D': 13,
		'E': 14,
		'F': 15,
		'G': 16,
		'H': 17,
		'I': 18,
		'J': 19,
		'K': 20,
		'L': 21,
		'M': 22,
		'N': 23,
		'O': 24,
		'P': 25,
		'Q': 26,
		'R': 27,
		'S': 28,
		'T': 29,
		'U': 30,
		'V': 31,
		'W': 32,
		'X': 33,
		'Y': 34,
		'Z': 35,
	}

	def _get_digit(self, i):
		if i in string_digits:
			return int(i)
		else:
			try:
				return self._letterdict[i.upper()]
			except TypeError:
				raise ChecksumError("Unable to get digit from letter")

	def _get_value_from_iteration(self, i): 
		if i%3 == 1:
			return 7
		elif i%3 == 2:
			return 3
		else:
			return 1

	def identity_card(self, checksum):
		if len(checksum) != 10:
			raise ChecksumError("Checksum needs to be 10 digits long")

		_sum = 0
		_iteration = 1
		for i in checksum[:9]:
			digit = self._get_digit(i)
			value = self._get_value_from_iteration(_iteration)
			_sum+= digit*value
			_iteration+=1

		if checksum[9:] == str(_sum)[2:]:
			return True
		else:
			raise ChecksumError("Checksum is not valid")

unit_test = Checksum()
unit_test.identity_card('T220001293') # Frau Erika Mustermann