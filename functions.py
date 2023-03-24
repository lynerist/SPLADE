from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from pyAudioAnalysis.audioSegmentation import silence_removal
from scipy.io import wavfile
from numpy import array
from numpy import concatenate
from os import path, mkdir

LANGUAGES = "af ar bg bn bo cs da de el en".split()
LANGUAGES_COMPLETE = {abbreviation:name for abbreviation, name in zip(LANGUAGES, \
"Afrikaans Arabic Bulgarian Bengali Tibetan Czech Danish German Greek English".split())}

#TODO CAPIRE PERCHé I FILE INIZIANO CON 0.0 0.0 0.0 etc.

class ARFF:
	def __init__(self, name):
		self.__storedFeatures = []
		self.name = name
		
		self.__outputFile = open(f"{self.name}.arff", "w")
		self.__outputFile.write(self.headingARFF())
		self.closeFile()

	def headingARFF(self):
		sf, fooAudio = read("dataset/af/_0nH46-zSA0__U__S27---0222.650-0227.830.wav")
		f, featuresNames = stf.feature_extraction(fooAudio, sf, 1000, 500)

		return	f"@relation audio\n\n@attribute name string\n" + \
				"@attribute language {" + ', '.join(LANGUAGES) + "}\n" + \
				"\n".join([f'@attribute {n.replace(" ", "_")} real' for n in featuresNames]) + \
				"\n\n@data\n"
	
	def storeAudioFeatures(self, audioLanguage, songNumber, features, featuresNames):
		self.__storedFeatures.append("\n".join([f"{audioLanguage}_{songNumber}_{frame},{audioLanguage}," +\
								",".join([f'{features[feature][frame]}' \
									for feature in range(len(featuresNames))])\
										for frame in range(len(features[0]))])+"\n")

	def freeStoredFeatures(self):
		self.__storedFeatures = []

	def exportARFF(self):
		self.openFile()
		self.__outputFile.write("".join(self.__storedFeatures))
		self.freeStoredFeatures()
		self.closeFile()

	def openFile(self):
		self.__outputFile = open(f"{self.name}.arff", "a")

	def closeFile(self):
		self.__outputFile.close()



def trimSilences(audioPath):
	sampling_rate, signal = read(audioPath)
	segmentLimits = silence_removal(signal, sampling_rate, 0.05, 0.05)

	outputPath, name = "/".join(audioPath.split("/")[:-1]) + "/trimmed/", audioPath.split("/")[-1]

	finalSignal = signal[0:1]
	
	for i, s in enumerate(segmentLimits):
		finalSignal = concatenate([finalSignal, signal[int(sampling_rate * s[0]):int(sampling_rate * s[1])]])
		print(finalSignal)
		
	if not path.exists(outputPath):
		mkdir(outputPath)

	wavfile.write(outputPath+name, sampling_rate, finalSignal)
	return finalSignal

if __name__ == "__main__":
	trimSilences("dataset/af/__test.wav")