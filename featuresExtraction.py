from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from functions import *
from os import listdir

arff = ARFF("fiveLanguages")

FRAME_DIMENSION = 1000
FRAME_STEP = 500

for audioLanguage in [LANGUAGES[i] for i in range(5)]:	
	print(LANGUAGES_COMPLETE[audioLanguage], end=" ")	
	languagePath = f"dataset/{audioLanguage}/"
	for index, audioName in enumerate(listdir(languagePath)):
		sf, audio = read(languagePath+audioName)
		extractedFeatures, extractedFeaturesNames = stf.feature_extraction(audio, sf, FRAME_DIMENSION, FRAME_STEP)
		# extractedFeatures = [[feature for i, feature in enumerate(frame) \
		# 									if extractedFeaturesNames[i] in FEATURES]\
		# 										for frame in extractedFeatures]
		extractedFeatures = [feature for i,feature in enumerate(extractedFeatures)\
														if extractedFeaturesNames[i] in FEATURES]

		arff.storeAudioFeatures(audioLanguage, index, extractedFeatures)

		if index%5==0: print(index, end=" / ")
		if index>12: break

	print()
	arff.exportARFF()
	

