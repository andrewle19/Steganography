from PIL import Image

def decode():
    # open and rotate the image
    img = Image.open("Secret.png")
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
    #print(msgLengthBits)
    msgLength = int("".join(map(str,msgLengthBits)),2)
    print("The text is",msgLength,"bits long")
    print("Or",msgLength/8,"characters long")

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
            print(byte)

            del byte[:]
            count = 0

    msg = "".join(msg)
    print(msg)

    return

def encode():
    img = Image.open("TestImage.jpg")
    img = img.rotate(180)
    encodedImg = Image.new('RGB',(img.width,img.height))

    # make an rgba copy of the image
    rgbImg = img.convert("RGB")

    msg = "security sucks"

    # find the length of the msg
    msgLength = len(msg)*8
    # convert the length to binary
    msgLength = '{0:032b}'.format(msgLength)
    msgLength += '0'

    # convert message to char list
    msg = list(msg)

    # convert msg into a binary list of characeters
    binMsg = []

    # loop through the list of characters
    # converts each character into the byte value
    # makes the byte value into a list of bits
    # append the bits to the bin msg list
    for i in range(len(msg)):
        byteValue = '{0:08b}'.format(ord(msg[i]))
        byteValue = list(byteValue)

        for j in range(len(byteValue)):
            binMsg.append(byteValue[j])

    index = 0

    binMsg = list(msgLength) + binMsg
    print(binMsg)

    # loop through entire image placing the msg
    #in the least Sig Bit of the image

    for i in range(img.height):
        for j in range(img.width):
            # get the rgba value of each pixel
            (r,g,b) = rgbImg.getpixel((j,i))

            # convert rgb into 8 bit format
            r = '{0:08b}'.format(r)
            g = '{0:08b}'.format(g)
            b = '{0:08b}'.format(b)

            for k in range(0,3):
                if(index < len(binMsg)):

                    if((k+1)% 3 == 1):
                        r = r[:7]
                        r += binMsg[index]
                        index += 1


                    if((k+1)%3 == 2):
                        g = g[:7]
                        g += binMsg[index]
                        index += 1

                    if((k+1)%3 == 0):
                        b = b[:7]
                        b += binMsg[index]
                        index += 1






            r = int(r,2)
            g = int(g,2)
            b = int(b,2)

            encodedImg.putpixel((j,i),(r,g,b))

    # reflip the image
    encodedImg = encodedImg.rotate(180)

    encodedImg.save('Secret.png',"PNG")




    print(len(binMsg))

    # r = '{0:08b}'.format(r)
    # r = r[:7]
    # # r += binMsg[0][1]
    # print(int(r,2))
    # for i in range(img.height):
    #     for j in range(img.width):
    #         if(count < len(msgLength)):
    #             (r,g,b,a) = rgbImg.getpixel((j,i))
    #             r = '{0:08b}'.format(r)
    #             g = '{0:08b}'.format(g)
    #             b = '{0:08b}'.format(b)







encode()
decode()
