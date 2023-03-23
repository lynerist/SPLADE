from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from functions import *
from os import listdir

arff = ARFF("treLingue")

FRAME_DIMENSION = 3000
FRAME_STEP = 1500

STEP_PRINT = 50
LIMIT = 1500

for audioLanguage in [LANGUAGES[i] for i in range(3)]:	
	print(LANGUAGES_COMPLETE[audioLanguage], end=" ")	
	filepath = f"dataset/{audioLanguage}/"
	for index, audioName in enumerate(listdir(filepath)):
		sf, audio = read(filepath+audioName)
		features, featuresNames = stf.feature_extraction(audio, sf, FRAME_DIMENSION, FRAME_STEP)

		arff.storeAudioFeatures(audioLanguage, index, features, featuresNames)

		if index%(LIMIT/10)==0: print(int(100*index/LIMIT), end=" / ")
		if index >LIMIT: break
	print()
	

arff.exportARFF()