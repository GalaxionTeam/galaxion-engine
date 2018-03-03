from inFile import Read
from update import Update
from output import Output

# Call update functions in a foreve loop
while True:
	Read.update()
	Update.update()
	Output.update()