import base64

def convertFile(filepath):
    with open(filepath,"rb") as img_file:
        b64Img=base64.b64encode(img_file.read())
    output=open("base64-img-output.txt","w")
    output.write(str(b64Img)) #Base64 can only be written to files as a string.
    print(str(b64Img))

print("Insert file link:")
link=str(input()) #Looks for input in command prompt.
convertFile(link)
print("Done!")
input() #Press enter to exit command prompt.