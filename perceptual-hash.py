from PIL import Image
import imagehash

imageOne = Image.open('/Users/abc/Documents/Images/a-1.jpg');
imageTwo = Image.open('/Users/abc/Documents/Images/a-2.jpg');

hashOne = imagehash.average_hash(imageOne);
hashTwo = imagehash.average_hash(imageTwo);

if hashOne == hashTwo:
	print("The images are identical");
else:
	print("The image are different");

