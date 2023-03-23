from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from functions import *
from os import listdir

arff = ARFF("treLingue")

for audioLanguage in [LANGUAGES[i] for i in range(3)]:		
	filepath = f"dataset/{audioLanguage}/"
	for index, audioName in enumerate(listdir(filepath)):
		sf, audio = read(filepath+audioName)
		features, featuresNames = stf.feature_extraction(audio, sf, 1000, 500)

		arff.storeAudioFeatures(audioLanguage, index, features, featuresNames)

		if index%10==0: print(index)
		if index >500: break

arff.exportARFF()