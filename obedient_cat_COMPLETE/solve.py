from argparse import ArgumentParser
import codecs

parser = ArgumentParser()
parser.add_argument("-t", "--text", help="add the text to rot-13")
args = parser.parse_args()

print('You entered: {}'.format(args.text))
print('Applying rot-13 to the text...')
print(codecs.encode(args.text, "rot-13"))
