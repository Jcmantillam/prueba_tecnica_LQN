import re

def poke_names(file_name):

	with open(file_name, 'r') as f:
		names = re.findall(r'\w+', f.read())

	longest_series, current_series = [], []

	def name_starts_with(lastletter, names):
		for index, name in enumerate(names):
			if name.startswith(lastletter):
				return index
		return False

	for name in names:
		current_name = name
		current_series.append(current_name)

		namelist = names[:]
		namelist.pop(namelist.index(current_name))

		index = name_starts_with(current_name[-1], namelist)

		while index is not False:
			current_name = namelist[index]
			current_series.append(current_name)
			namelist.pop(index)
			index = name_starts_with(current_name[-1], namelist)

		if len(current_series) > len(longest_series):
			longest_series = current_series

		current_series = []

	print(longest_series)

poke_names('poke_names.txt')