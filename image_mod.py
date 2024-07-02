# ---------------------------------- Imports --------------------------------- #

from PIL import Image, ImageShow, ImageFilter
from matplotlib import pyplot as plt
from matplotlib import image as mpimg
import requests
from datetime import datetime
import ctypes


# --------------------------- Function Definitions --------------------------- #

# show images in vscode (for pest control)
def showim(image):
    plt.imshow(image)
    plt.show()
    return None

# api call to get image url
def get_bing_url():
    # former api - new one has better resolution
    # url = 'https://bing.biturl.top'
    # headers = {'resolution': '1920',
    #            'format': 'json',
    #            'index': '0',
    #            'mkt': 'en-AU'}

    url = 'https://peapix.com/bing/feed?country=au'
    headers = {}

    try:
        response = requests.get(url, params=headers)

        if response.status_code == 200:
            posts = response.json()[0]['fullUrl']
            return posts
        else:
            print('Error: ', response.status_code)

    except requests.exceptions.RequestException as e:
        print('Error: ', e)
        return None

# call to download image from url
def get_bing_image(url):
    response = requests.get(url)
    with open('bing_image.jpg', 'wb') as file:
        file.write(response.content)
    return None


# create bin regions on desktop image
def paste_bin(image, box):
    region = image.crop(box)
    blurred_region = region.filter(ImageFilter.GaussianBlur(20))
    image.paste(blurred_region, box)



# --------------------------------- API Call --------------------------------- #

# get and load bing image
url = get_bing_url()
get_bing_image(url)

with Image.open('bing_image.jpg') as bingim:
    bingim.load()

# bingim = bingim.convert('RGBA')
# bingim.format = 'PNG'



# ---------------------------- Image Customization --------------------------- #

# load timetable image
with Image.open('timetable.png') as timetable:
    timetable.load()


column_width = 250          # CHANGES THE WIDTH OF THE BLURRED COLUMNS
tt_height = 400             # CHANGES THE HEIGHT OF THE TIMETABLE IMAGE


# paste timetable image onto bing image
small_timetable = timetable.resize((column_width, tt_height))
width, height = bingim.size

tb_padding = 50
int_padding = 20
lr_padding = 20

tt_left = width - (column_width + lr_padding)
tt_top = height - (tt_height + tb_padding) - 15
tt_right = width - lr_padding
tt_bottom = height - tb_padding - 15

tt_box = (tt_left, tt_top, tt_right, tt_bottom)
bingim.paste(small_timetable, tt_box)


# paste bin 1
b1_left = tt_left
b1_top = tb_padding
b1_right = tt_right
b1_bottom = tt_top - int_padding

b1_box = (b1_left, b1_top, b1_right, b1_bottom)

paste_bin(bingim, b1_box)

# paste bin 2
b2_left = lr_padding
b2_top = tb_padding
b2_right = column_width + lr_padding
b2_bottom = 250 + tb_padding

b2_box = (b2_left, b2_top, b2_right, b2_bottom)

paste_bin(bingim, b2_box)

# paste bin 3
b3_left = lr_padding
b3_top = b2_bottom + int_padding
b3_right = column_width + lr_padding
b3_bottom = tt_bottom

b3_box = (b3_left, b3_top, b3_right, b3_bottom)

paste_bin(bingim, b3_box)



# -------------------------------- Save & Set -------------------------------- #

# save wallpaper
# date = datetime.today().strftime('%Y-%m-%d')

# ---------------------------------------------------------------------------- #
#                         WALLPAPER SAVES TO THIS PATH:                        #
# ---------------------------------------------------------------------------- #

save_path = '**YOUR PATH HERE**'
bingim.save(save_path)

# set wallpaper

# ---------------------------------------------------------------------------- #
#                         WALLPAPER SETS TO THIS PATH:                         #
# ---------------------------------------------------------------------------- #

set_path = r'**YOUR PATH HERE**'
ctypes.windll.user32.SystemParametersInfoW(20, 0, set_path, 0)
