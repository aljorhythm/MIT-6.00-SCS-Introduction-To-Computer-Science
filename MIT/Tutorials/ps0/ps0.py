# qpy:console
import math
def run():
  lastName = raw_input('Enter your last name\n**')
  firstName = raw_input('Enter your date of birth:\n**')
  print lastName + ' ' + firstName
  return
# implementing square root algorithm
def root(num):
  return rootrec(num / (num / 2), num)

def rootrec(guess, num):
  guessRes = guess * guess 
  if(math.fabs((num - guessRes)) < 0.1):
    return guess
  else: 
    return rootrec((guess + (num / guess)) / 2, num)

def rootErrMar(num, error):
  return rootrecErrMar(num / (num / 2), num, error)

def rootrecErrMar(guess, num, error):
  guessRes = guess * guess 
  if (math.fabs((num - guessRes)) < error):
    return guess
  else:
    return rootrecErrMar((guess + (num / guess)) / 2, num, error)


num = float(raw_input('root() Enter rootnum: '))
while not num == 0:
  print "root: " + str(root(num)) + " math.sqrt: " + str(math.sqrt(num))
  num = float(raw_input('root() Enter rootnum: '))

print ("\ntesting root with error margin")
num = float(raw_input('rootErrMar() Enter rootnum: '))
err = float(raw_input('rootErrMar() Enter error margin: '))
while not num == 0:
  print "rootErrMar: " + str(rootErrMar(num, err)) + " math.sqrt: " + str(math.sqrt(num))
  num = float(raw_input('rootErrMar() Enter rootnum: '))
  err = float(raw_input('rootErrMar() Enter error margin: ')) 

print ("conclusion\nHero's square root algorithm is not very accurate. Check out http://www.codeproject.com/Articles/570700/SquareplusRootplusalgorithmplusforplusC")
print ("BYEEE")

