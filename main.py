print("slinkais astrologs")
import random

zodiac = ["Aunus", "Dvini", "Jaunava", "Lauva", "Mazazis", "Skorpions", "Strelnieks", "Svari", "Udensvirs", "Versis", "Vezis", "Zivis"]
horoskopi = ["prieks", "nauda", "skumjas", "milestiba", "veiksme", "jaunas iepazisanas", "naudas samazisanas", "liela zaudesana", "laime", "bagatiba", "iespejams daudz stressa", "laime"]

random.shuffle(horoskopi)

for i in range(12):
  print(zodiac[i])
  print(horoskopi[i])
  print("-----")