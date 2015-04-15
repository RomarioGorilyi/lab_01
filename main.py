__author__ = "Roman Gorilyi"

__version__ = "1.0.0"
__maintainer__ = "Roman Gorilyi"
__email__ = "rom4ik-007@yandex.ua"

from functions import *

index = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
         '11', '12', '13', '14', '15', "16", '17', '18', '19', '20',
         '21', '22', '23', '24', '25', '26', '27']

region = ["Cherkasy", "Chernihiv", "Chernivci", "Crimea", "Dnipropetrovs'k", "Donets'k", "Ivano-Frankivs'k", "Kharkiv",
          "Kherson", "Khmel'nyts'kyy", "Kiev", "Kiev City", "Kirovohrad", "Luhans'k", " L'viv", "Mykolayiv", "Odessa",
          "Poltava", " Rivne", "Sevastopol'", "Sumy", "Ternopil'", "Transcarpathia", "Vinnytsya", "Volyn",
          "Zaporizhzhya", "Zhytomyr"]

download_queue = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                  '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                  '21', '22', '23', '24', '25', '26', '27']

region.sort()
delete()

i = 0
while i < len(index):
    download_queue[i] = download(index[i], region[i])
    i += 1

i = 0
while i < len(index):
    print(region[i] + ":")
    print(str(max_value("%s.csv" % (index[i] + " " + region[i] + " " + download_queue[i]), 2015)) + os.linesep)
    i += 1

i = 0
while i < len(index):
    print(region[i] + ":")
    print(str(min_value("%s.csv" % (index[i] + " " + region[i] + " " + download_queue[i]), 2015)) + os.linesep)
    i += 1

i = 0
while i < len(index):
    print(region[i] + ":")
    print(str(extreme_drought("%s.csv" % (index[i] + " " + region[i] + " " + download_queue[i]))) + os.linesep)
    i += 1

i = 0
while i < len(index):
    print(region[i] + ":")
    print(str(moderate_drought("%s.csv" % (index[i] + " " + region[i] + " " + download_queue[i]))) + os.linesep)
    i += 1

print(region[2] + ":")
print(str(years_drought_more_than_third_year("%s.csv" % (index[2] + " " + region[2] + " " + download_queue[2]))))