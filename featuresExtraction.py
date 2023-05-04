from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from functions import *
from os import listdir

TRAIN = False
TEST = True

arff = ARFF("tenLanguages" + (TRAIN and "TRAIN" or TEST and "TEST" or ""))
firstAudio = TEST and 50 or 0
LastAudio = TRAIN and 50 or 61

FRAME_DIMENSION = 2 * SAMPLE_FREQUENCY
FRAME_STEP = 1 * SAMPLE_FREQUENCY

for audioLanguage in LANGUAGES:	
	print(LANGUAGES_COMPLETE[audioLanguage], end=" ")	
	languagePath = f"dataset/{audioLanguage}/"
	for index, audioName in enumerate(listdir(languagePath)[firstAudio:LastAudio]):
		sf, audio = read(languagePath+audioName)
		extractedFeatures, extractedFeaturesNames = stf.feature_extraction(audio, sf, FRAME_DIMENSION, FRAME_STEP)

		selectedFeatures = [feature for i,feature in enumerate(extractedFeatures)\
														if extractedFeaturesNames[i] in FEATURES]

		arff.storeAudioFeatures(audioLanguage, index, selectedFeatures)

		if index%5==0: print(index, end=" / ")
		#if index>12: break

	print()
	arff.exportARFF()
	

