import cPickle
import gzip

def main():
	""" Make Flat file
	This is a short program to save the serialized data as a flat file.
	This is to be read into C# code since pickled data is not conducive
	to the .NET framework.		
	"""

	# Unpickle stuff	
	dataset = '../data/mnist.pkl.gz'
	f = gzip.open(dataset, 'rb')
	train_set, valid_set, test_set = cPickle.load(f)
	f.close()

	classification = train_set[0]
	tags = train_set[1]		

	# Get the actual mnist pictures
	fo = open('file', 'rw+')

	for i in range(len(classification)):
		for value in list(classification[i]):
			fo.write("%s " % value)
		fo.write("\n")
	
	fo.close()

	# Get the tags
	fo = open('file2', 'rw+')

	for value in list(tags):
		fo.write("%s \n" % value)

	fo.close()

if __name__ == '__main__':
	main()
