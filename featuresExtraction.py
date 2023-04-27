from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from functions import *
from os import listdir

arff = ARFF("threeLanguages")

FRAME_DIMENSION = 2 * SAMPLE_FREQUENCY
FRAME_STEP = 1 * SAMPLE_FREQUENCY

for audioLanguage in LANGUAGES:	
	print(LANGUAGES_COMPLETE[audioLanguage], end=" ")	
	languagePath = f"dataset/{audioLanguage}/"
	for index, audioName in enumerate(listdir(languagePath)):
		sf, audio = read(languagePath+audioName)
		extractedFeatures, extractedFeaturesNames = stf.feature_extraction(audio, sf, FRAME_DIMENSION, FRAME_STEP)

		selectedFeatures = [feature for i,feature in enumerate(extractedFeatures)\
														if extractedFeaturesNames[i] in FEATURES]

		arff.storeAudioFeatures(audioLanguage, index, selectedFeatures)

		if index%5==0: print(index, end=" / ")
		#if index>12: break

	print()
	arff.exportARFF()
	

