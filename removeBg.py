# http://stackoverflow.com/questions/765736/using-pil-to-make-all-white-pixels-transparent

# col to remove
col = [255, 255, 255] # 255 * 3 is white
# col = [0, 0, 0] #black

# +- 5 to above value
fuzzy = 5

from PIL import Image

# download from http://kingofwallpapers.com/random-image/random-image-005.jpg
img = Image.open('random-image-005.jpg')
img = img.convert("RGBA")
datas = img.getdata()

newData = []
for item in datas:
    if col[0] - fuzzy <= item[0] <= col[0] + fuzzy and col[1] - fuzzy <= item[1] <= col[1] + fuzzy and col[2] - fuzzy <= item[2] <= col[2] + fuzzy:
    # if sum([item[0] > 250, item[1] > 250, item[2] > 250]) == 3:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)

img.putdata(newData)
img.save("random-image-005.jpg.png", "PNG")
