Author: Andrew Le
Email: andrewle19@csu.fullerton.edu

Encodes/Decodes images with text

Example:
  python3 textInImage.py -e testImage.jpg -o outputfile -t "Hide this msg"
  python3 textInImage.py -d outputfile.png

Files Included:
  SourceCode.jpg - image before encoding of source code
  EsourceCode.png - image after encoding
  testImage.png - given test image
  textInImage.py - script


usage: textInImage.py [-h] [-e] [-d] [-o OUTPUT] [-t TEXT] image
  Hides message in image

  positional arguments:
    image                 Image to hide text in(jpg)

  optional arguments:
    -h, --help            show this help message and exit
    -e, --encode
    -d, --decode
    -o OUTPUT, --output OUTPUT
                          Name of Output File(no extension)
    -t TEXT, --text TEXT  Message to Encode in file
