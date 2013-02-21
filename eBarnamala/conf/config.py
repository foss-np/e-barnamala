from os.path import join

baseImagePath = 'Images'
iconsPath = 'icons'
coreImagesPath = join(baseImagePath, 'coreImages')
buttonsPath = join(coreImagesPath, 'buttons')
cursorPath = join(coreImagesPath, 'cursor')
letterImagesPath = join(baseImagePath, 'letterImages')
byanjanImagesPath = join(letterImagesPath, 'byanjan')
sworImagesPath = join(letterImagesPath, 'swor')
numberImagesPath = join(baseImagePath,'numberImages')
timeImagesPath = join(baseImagePath, 'time')
trafficSignImagesPath = join(baseImagePath, 'trafficSigns')
animalBasePath = join(baseImagePath, 'animals')
animalImagesPath = join(animalBasePath, 'animal')
birdImagesPath = join(animalBasePath, 'bird')
insectImagesPath = join(animalBasePath, 'insect')
colourImagesPath = join(baseImagePath, 'colour')
moneyBasePath = join(baseImagePath, 'money')
notesImagesPath = join(moneyBasePath, 'notes')
coinsImagesPath = join(moneyBasePath, 'coins')

fontName = "Aalekh"
fontNameEnglish = "Times New Roman"
fontSizesForAalekh = [30, 40, 50, 80, 100, 140, 180]
fontSizeForBarakhari = [30]


fontSize = fontSizesForAalekh
###Please make sure that the below two colours are different. Otherwise
###there will be problems in numbersAboveNine and basicArithmetic
###also these are used for highlights in activities
backgroundColour = 'WHITE'
fillColour = 'RED'

fontNameArithmetic = "Kalimati"
fontSizeArithmetic = [30, 40, 50, 80, 100, 140, 180]

splashImage = join(coreImagesPath, 'splash.png')

###below files are req for memoryPairs activities
cardFrontFace = "cardFront.png"
cardBackFace = "cardBack.png"
bckgndColour = 'WHITE'
textColour = 'BLACK'
fontSizeForCard = 25
