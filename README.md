# IconGenerator
Uses SHA384 hashing algorithm to create a 450x450 png icon specific to your username.
You need https://pillow.readthedocs.io/en/5.3.x/ in order to use this
# What is SHA
SHA384 is a cryptographic hash functions.
This is a one way hashing algorithm that will produce a unique output meaning two different input values will not result in the same hash output.
Output will be 384 bits or 48 bytes.
# How it works
## Step one: Array of 48 decimals
Takes user input and passes it into SHA384 hashing function
Converts the returned value into an array of decimal values where for every two hexadecimal values returned
A hexdecimal value is 4 bits so it equals  1 byte, 2 hexadecimal values equal 2 bytes, Two bytes equal 255 in decimal
The returned array of decimal values is a max value of 255 and can represent 48 bytes
## Step two: How the image is represented
The image is a 450 x 450 image which is made a collection of blocks each 50 x 50 in size
The blocks are grouped so that there 9x9 total blocks in the 450x450 Image
So there are a total of 81 blocks in the Image
Each row in the image looks like this:
x x x x - 0 0 0 0
Each of these is a blocks
The x is represented by one of the decimals in the decimal array
The - is also a decimal in the array
The 0 is the mirror of the x values so they are represented by one of the x values
## Step three: How to make the Image
If the decimal in x is even then x will be colored
If the decimal in x is odd then x will not be colored
The same rule applies to -
The image is then mirrored over
The last 3 digits in the array of digits give the color that all blocks will represent
Since the last three digits are {255, 255, 255} this can represent RGB or red, green, and blue.
The image is then saved to Icon directory using the users given input
