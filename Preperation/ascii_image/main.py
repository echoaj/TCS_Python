from PIL import Image

img = Image.open("home.png")
pixels = list(img.getdata())


ascii = ['"', '-', '*', '=', '#']

file = open("house.txt", "w")

for i in range(len(pixels)):
    num = (pixels[i][1])
    if num <= 51:
        val = 0
    elif num <= 102:
        val = 1
    elif num <= 153:
        val = 2
    elif num <= 204:
        val = 3
    elif num <= 255:
        val = 4
    
    file.write(ascii[val])
    # print(ascii[val], end='')
    if i % img.size[0] == 0:
        file.write('\n')
        # print('')

file.close()
# image = [[0,0,0,0,0,0,1,0,0,0],
#          [0,1,2,0,1,0,2,0,0,0],
#          [0,1,1,4,0,0,3,0,4,0],
#          [0,0,0,2,1,0,4,0,4,0],
#          [0,0,1,0,4,0,3,0,0,0],
#          [0,0,0,0,3,0,0,0,0,0],]


# for row in image:
#     for i in row:
#         print(ascii[i], end="")
#     print()