from PIL import Image

def decode():
    # open and rotate the image
    img = Image.open("testImage.png")
    img = img.rotate(180)

    # rgb copy of the image
    rgbImg = img.convert("RGB")

    # grab least significant bits of every rgb value of pixel
    leastSigBits = []

    # extract each least significant bit in the image
    #starting from top left to bottom right
    for i in range(img.height):
        for j in range(img.width):
            (r,g,b) = rgbImg.getpixel((j,i))
            leastSigBits.append(r & 1)
            leastSigBits.append(g & 1)
            leastSigBits.append(b & 1)

    # get the integer length by getting the first 32 leastSigBits
    msgLengthBits = []
    for i in range(0,32):
        msgLengthBits.append(leastSigBits[i])

    # convert the 32 bits into an integer
    msgLength = int("".join(map(str,msgLengthBits)),2)
    print("The text is",msgLength,"bits long")

    byte = []
    msg = []
    count = 0

    # loop through rest of bits starting at bit right after
    # the lengths are stored
    for i in range(33, 34 + msgLength):

        # append the least significant bits to the byte
        # list and icrement the count
        byte.append(leastSigBits[i])
        count += 1

        # when count is 0 means a byte is formed
        # we join the bits to form an integer
        # then we convert the byte to char and append it to msg
        # we also reset the count and clear the bits in byte list
        if (count == 8):
            msgIntValue = int("".join(map(str,byte)), 2)
            msg.append(chr(msgIntValue))
            del byte[:]
            count = 0


    msg = "".join(msg)
    print(msg)

    return


decode()
