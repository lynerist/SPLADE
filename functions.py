from pyAudioAnalysis import ShortTermFeatures as stf
from pyAudioAnalysis.audioBasicIO import read_audio_file as read

LANGUAGES = "af ar bg bn bo cs da de el en".split()

#TODO CAPIRE PERCHé I FILE INIZIANO CON 0.0 0.0 0.0 etc.

class ARFF:
	def __init__(self, name):
		self.storedFeatures = []
		self.outputFile = open(f"{name}.arff", "w")
		self.outputFile.write(self.headingARFF())

	def headingARFF(self):
		sf, fooAudio = read("dataset/af/_0nH46-zSA0__U__S27---0222.650-0227.830.wav")
		f, featuresNames = stf.feature_extraction(fooAudio, sf, 1000, 500)

		return	f"@relation audio\n\n@attribute name string\n" + \
				"@attribute language {" + ', '.join(LANGUAGES) + "}\n" + \
				"\n".join([f'@attribute {n.replace(" ", "_")} real' for n in featuresNames]) + \
				"\n\n@data\n"
	
	def storeAudioFeatures(self, audioLanguage, songNumber, features, featuresNames):
		self.storedFeatures.append("\n".join([f"{audioLanguage}_{songNumber}_{frame},{audioLanguage}," +\
								",".join([f'{features[feature][frame]}' \
									for feature in range(len(featuresNames))])\
										for frame in range(len(features[0]))])+"\n")

	def exportARFF(self):
		self.outputFile.write("".join(self.storedFeatures))

if __name__ == "__main__":
	inizializeARFF(["a","b","c"])