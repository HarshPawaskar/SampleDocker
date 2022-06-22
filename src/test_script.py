import pytest

class Testing:
	@pytest.mark.first
	def test_compare(self):
		path1 = "C:/Users/Harsh Pawaskar/SamplePython/source/file1.txt"
		path2 = "C:/Users/Harsh Pawaskar/SamplePython/destination/file2.txt"
		file_1 = open(path1, 'r')
		file_2 = open(path2, 'r')
		li = list()
		li.append("Comparing files " + " @ " + 'file1.txt' + " # " + 'file2.txt')

		file_1_line = file_1.readline()
		file_2_line = file_2.readline()

		# Use as a COunter
		line_no = 1

		print()

		with open(path1) as file1:
			with open(path2) as file2:
				same = set(file1).intersection(file2)

		li.append("Common Lines in Both Files")

		for line in same:
			li.append(line)

		#print('\n')
		li.append("Difference Lines in Both Files")
		while file_1_line != '' or file_2_line != '':

			# Removing whitespaces
			file_1_line = file_1_line.rstrip()
			file_2_line = file_2_line.rstrip()

			# Compare the lines from both file
			if file_1_line != file_2_line:
				
				# otherwise output the line on file1 and use @ sign
				if file_1_line == '':
					li.append("@" + "Line- " + str(line_no) +" "+ str(file_1_line))
				else:
					li.append("@-" + "Line- " + str(line_no) +" "+ str(file_1_line))
					
				# otherwise output the line on file2 and use # sign
				if file_2_line == '':
					li.append("#" + "Line- " + str(line_no) +" "+ str(file_2_line))
				else:
					li.append("#+" + "Line- " + str(line_no) +" "+ str(file_2_line))

			# Read the next line from the file
			file_1_line = file_1.readline()
			file_2_line = file_2.readline()

			line_no += 1
		with open(r'outputs.txt', 'w') as fp:
			fp.write('\n'.join(li))
		file_1.close()
		file_2.close()
