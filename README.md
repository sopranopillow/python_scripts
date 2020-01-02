# Python scripts
These are random python scripts that I work on as they are needed. Here is a little description for each one:
***
## ./imageTools/imageToSprite
This was a fun project to convert a normal image to a pixel art. The Idea came while working on my portfolio and not being able to draw any decent pixel art. This project uses:
* OpenCV 2
* Numpy
* SKlearn's KMeans cluster

NOTE: SKleanr's KMeans cluster is needed since it is used to calculate the dominant color of the area to convert to one pixel.

Examples:

Autum leaves - ( 1 pixel = 6 pixels from original ):

![Alt text](/imageTools/originalImages/fall-leaves.jpg?raw=true "Autum Leaves Original")

Original

![Alt text](/imageTools/resultingImages/fixedLeaves.png?raw=true "Autum Leaves Pixelated")

Result

Link Image - ( 1 pixel = 16 pixels from original ):

![Alt text](/imageTools/originalImages/link.jpg?raw=true "Link Original")

Original

![Alt text](/imageTools/resultingImages/linkSprite.png?raw=true "Link Pixelated")

Result
***
## ./deansListExcelToHTML
This script was made for a job I was working on. This script uses xlWings to handle the excel file.

NOTE: I do not recommend using this one since it was specifically made for a website and the excel file requires a specific format.
