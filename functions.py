from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read
from pyAudioAnalysis.audioSegmentation import silence_removal
from scipy.io import wavfile
from numpy import array
from numpy import concatenate
from os import path, mkdir
from numpy import int16

with open("parameters/languages.txt") as f:
	lines = [line[:-1].split() for line in f.readlines()]
	LANGUAGES = [acronymAndLanguage[0] for acronymAndLanguage in lines]
	LANGUAGES_COMPLETE = {acronymAndLanguage[0]:acronymAndLanguage[1] for acronymAndLanguage in lines}

with open("parameters/features.txt") as f:
	FEATURES = [feature[:-1] for feature in f.readlines()]

SAMPLE_FREQUENCY = 16000

#TODO CAPIRE PERCHé I FILE INIZIANO CON 0.0 0.0 0.0 etc.

class ARFF:
	def __init__(self, name):
		self.__storedFeatures = []
		self.name = name
		
		self.__outputFile = open(f"arff/{self.name}.arff", "w")
		self.__outputFile.write(self.headingARFF())
		self.closeFile()

	def headingARFF(self):
		sf, fooAudio = read("dataset/af/0.wav")
		
		return	f"@relation audio\n\n" + \
				"@attribute language {" + ', '.join(LANGUAGES) + "}\n" + \
				"\n".join([f'@attribute {n.replace(" ", "_")} real' for n in FEATURES]) + \
				"\n\n@data\n"
	
	def storeAudioFeatures(self, audioLanguage, songNumber, features):
		self.__storedFeatures.append("\n".join([f"{audioLanguage},"+",".join([f'{features[feature][frame]}' \
									for feature in range(len(FEATURES))])\
										for frame in range(len(features[0]))])+"\n")

	def freeStoredFeatures(self):
		self.__storedFeatures = []

	def exportARFF(self):
		self.openFile()
		self.__outputFile.write("".join(self.__storedFeatures))
		self.freeStoredFeatures()
		self.closeFile()

	def openFile(self):
		self.__outputFile = open(f"arff/{self.name}.arff", "a")

	def closeFile(self):
		self.__outputFile.close()

class Logger:
	def __init__(self, function, logStep=100):
		self.__logCount = 0	
		self.wrapped = function
		self.logStep = logStep

	def __call__(self, *args):
		self.__logCount += 1
		if self.__logCount % self.logStep == 0:
			print(self.__logCount, end=" /")
		return self.wrapped(*args)
		
def trimSilences(sampling_rate, signalIn, audioName):
	segmentLimits = silence_removal(signalIn, sampling_rate, 0.05, 0.05)
	signalOut = concatenate([signalIn[int(sampling_rate * s[0]):int(sampling_rate * s[1])] \
								for i, s in enumerate(segmentLimits)]) if segmentLimits else array([], dtype=int16)
	return signalOut

if __name__ == "__main__":
	# audioPath = "dataset/af/__test.wav"
	# sampling_rate, signal = read(audioPath)

	# outputPath, name = "/".join(audioPath.split("/")[:-1]) + "/trimmed/", audioPath.split("/")[-1]
	# if not path.exists(outputPath):
	# 	mkdir(outputPath)

	# wavfile.write(outputPath+name, sampling_rate, trimSilences(sampling_rate, signal))

	audioPath = "dataset/af/zzvHKmkFzeQ__U__S55---0634.630-0643.790.wav"
	sampling_rate, signal = read(audioPath)
	print(signal)
