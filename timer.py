# this program is supposed to allow the user to compare function speeds across other programs

# Import files here, note you don't need to add ending '.py'
## Of course they don't have to be strictly Python files, anything Python can improt and run should work
## Also note that the main contents of the file will be run on import
import Euler17

# add all the function names that you want to time here
## make sure to include the filename, eg. 'myfile.myfunc'
## also make sure to not add trailing parenthesis
functions = [Euler17.wordbuilder, Euler17.wordAccumulator]


# set args flag to 1 for unique arguments, 0 for arguments, and -1 for no arguments
args = 0

# add arguments to this list
## for unique arguments, enter each set of new arguments as a seperate list, eg. arguments = [['first', 'set'], ['second', 'set'], ['and', 'so', 'on']]
## make sure the unique arguments match their functions, eg. function[0] matches to argument[0] and function[1] to argument[1], etc.
arguments = []

# put the number of runs you would like to do here
## note that more runs increases accuracy and consistency but will also take longer to finish
runs = 15




# You shouldn't need to edit anything beyond this, but you can if you want to
def timeTest3(funcs, args, runs):
	import time

	exTimes = [0] * len(funcs)							# make a list with an entry for each function

	for i in range(runs):								# do timing process for **run** times
		for j in range(len(funcs)):						# do every function
			for k in range(runs):						# and do it for **run** number of times;; note that this means runtime is runs^2 * funcs
				start = time.time()						# mark start time
				funcs[j](args)							# run function in list, passing arguments;; functions must accept one argument as a list
				exTimes[j] += time.time() - start		# add run time to function entry

	for i in range(len(exTimes)):
		exTimes[i] = exTimes[i] / (runs * runs)			# average run times, did runs^2 so divide by runs^2
	return exTimes

def timeTest3_noArg(funcs, runs):
	import time

	exTimes = [0] * len(funcs)							# make a list with an entry for each function

	for i in range(runs):								# do timing process for **run** times
		for j in range(len(funcs)):						# do every function
			for k in range(runs):						# and do it for **run** number of times;; note that this means runtime is runs^2 * funcs
				start = time.time()						# mark start time
				funcs[j]()								# run function in list
				exTimes[j] += time.time() - start		# add run time to function entry

	for i in range(len(exTimes)):
		exTimes[i] = exTimes[i] / (runs * runs)			# average run times, did runs^2 so divide by runs^2
	return exTimes

def timeTest3_uniqueArgs(funcs, args, runs):
	import time

	exTimes = [0] * len(funcs)							# make a list with an entry for each function

	for i in range(runs):								# do timing process for **run** times
		for j in range(len(funcs)):						# do every function
			for k in range(runs):						# and do it for **run** number of times;; note that this means runtime is runs^2 * funcs
				start = time.time()						# mark start time
				funcs[j](args[j])							# run function in list, passing arguments;; functions must accept one argument as a list
				exTimes[j] += time.time() - start		# add run time to function entry

	for i in range(len(exTimes)):
		exTimes[i] = exTimes[i] / (runs * runs)			# average run times, did runs^2 so divide by runs^2
	return exTimes


def displayTimes(funcs, args, runs, timeTester):
	timeList = timeTester(funcs, args, runs)																									# get a list of average times for the functions
	for i in range(len(timeList)):
		if i == 0:
			print("Function 1:", timeList[i], "s")
		else:
			print("Function ", i + 1, ": ", timeList[i], " s; ", ((timeList[0] / timeList[i]) * 100) - 100, " % change from ", 1, sep="")		# print out times, compares each one's time to first


if args == 0:
	displayTimes(functions, arguments, runs, timeTest3)
elif args == -1:
	displayTimes(functions, arguments, runs, timeTest3_noArg)
elif args == 1:
	displayTimes(functions, arguments, runs, timeTest3_uniqueArgs)
else:
	print("It looks like the args flag is set to a number that is not allowed")

# Ways to improve this:
## DONE: accomodate functions that don't take arguments
## DONE: accomodate functions that take different arguments
## accomodate functions that don't take a list as an argument
## choose reference function
## dynamically set reference function
## add command line interface
## add error checking