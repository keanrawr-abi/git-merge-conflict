from time import sleep
from random import randint

class MagicModel:

	def train(self):
		print('Training model really hard...')
		print('Bip boop bop')
		secs = randint(1, 5)
		sleep(secs)
		print('Model has been trained')

	def predict(self, *args):
		pred = randint(0, 100)
		print(f'My prediction is: {pred}')
