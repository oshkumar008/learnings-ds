import json
import re

import scipy.stats as stats
alpha = 5
loc = 100.5
beta = 22
data = stats.gamma.rvs(alpha, loc=loc, scale=beta, size=10000)
print(data)
# [ 202.36035683  297.23906376  249.53831795 ...,  271.85204096  180.75026301
#   364.60240242]

import openturns as ot
import openturns.viewer as otv

gammaDistribution = ot.Gamma()
sample = gammaDistribution.getSample(100)
distribution = ot.GammaFactory().build(sample)
otv.View(distribution.drawPDF())
'''Rename all files of directory'''
import os
import shutil
file = '/home/santosh/Desktop/no-image-cuisines.jpg'
jso = '/home/santosh/Desktop/not_found copy.json'
f = open(jso)

data = json.load(f)
print(len(data))
print(len([name for name in os.listdir('/home/santosh/Desktop/dish_img') if os.path.isfile(os.path.join('/home/santosh/Desktop/dish_img', name))]))
# for dish in data_gmt:
#     shutil.copy2(file, '/home/santosh/Desktop/' + dish['Dish'] + '.jpg')

# for index, file in enumerate(files):
#     print(file.split('_')[0], index)
#     os.rename(os.path.join(path, file), os.path.join(path, ''.join([file.split('_')[0], '.jpg'])))


m = re.match(r"(\d+)\.?(\d+)?", "24.35")
print(m.groups())

m = re.match(r"(?P<first_name>\w+) (?P<last_name>\w+)", "Malcolm Reynolds")
print(m.groupdict())

email = "santosh@ramremove_thissingh.in"

m = re.search("remove_this", email)

newemail = email[:m.start()] + email[m.end():]

print(newemail)

valid = re.compile(r"^[a2-9tjqk]{5}$")
print(valid.match("kkdkk")) #invald
print(valid.match("aaaaa")) #valid
print(valid.match("aaafa")) #invalid

compmatch = re.match("c", "abcdef")    # No match
print(compmatch)
checkin = re.search("\w+d\w+", "abcdef")    #match
print(checkin)
fullymatch = re.fullmatch("p.*n", "python") # Match - fulmatch whole word with start p and end n
print(fullymatch)
fullnomatch = re.fullmatch("r.*n", "rython") # No Match - fulmatch whole word with start p and end n
print(fullnomatch)
text = "He was carefully disguised but captured quickly by police."
adv = re.findall(r"\w+ly\b", text) #Find adverbs
print(adv)

for m in re.finditer(r"\w+ly\b", text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0))) #check positions(start & and) of all adverbs

#Raw String Notation
rawstr = re.match(r"\W(.)\1\W", " rr ")
print(rawstr)
