from functions import *
from os import listdir
from numpy import int16
from os import path, mkdir
from pyAudioAnalysis.audioBasicIO import read_audio_file as read

def aggregateLanguage(language):
	languagePath = f"dataset/{language}/"
	outputPath = f"dataset/{language}Aggregated/"
	if not path.exists(outputPath):
		mkdir(outputPath)

	loggedTrimSilences = Logger(trimSilences)

	languageBlock = concatenate([loggedTrimSilences(*read(languagePath+audioName),audioName )\
								for audioName in listdir(languagePath)])

	chunkIndex = 0
	FIVE_MINUTES_SAMPLES =  60 * 5 * SAMPLE_FREQUENCY
	while FIVE_MINUTES_SAMPLES * chunkIndex < len(languageBlock):
		wavfile.write(f"{outputPath}{chunkIndex}.wav", SAMPLE_FREQUENCY,\
				languageBlock[chunkIndex*FIVE_MINUTES_SAMPLES:\
								min((chunkIndex+1)*FIVE_MINUTES_SAMPLES, len(languageBlock))])
		chunkIndex+=1

if __name__ == "__main__":
	aggregateLanguage("ja")
