from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from functions import *
from os import listdir

arff = ARFF("testTreLingue")

FRAME_DIMENSION = 1000
FRAME_STEP = 500

for audioLanguage in [LANGUAGES[i] for i in range(3)]:	
	print(LANGUAGES_COMPLETE[audioLanguage], end=" ")	
	languagePath = f"dataset/{audioLanguage}/"
	for index, audioName in enumerate(listdir(languagePath)):
		sf, audio = read(languagePath+audioName)
		features, featuresNames = stf.feature_extraction(audio, sf, FRAME_DIMENSION, FRAME_STEP)

		arff.storeAudioFeatures(audioLanguage, index, features, featuresNames)

		if index%5==0: print(index, end=" / ")
		if index>5:break

	print()
	arff.exportARFF()
	

