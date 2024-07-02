# saucy-bing-wallpapers

A python (3.12.3) script that gets the daily bing image, adds some sauce, and sets it as the desktop background.

## Why?

I have used the Daily Bing Wallpaper utility for a while now - it automatically changes my wallpaper every day and I like having something fresh on my desktop.
That said, I also like my desktop to have some *sauce* (a timetable widget, or some boxes to organise my folders in).
This (very amateur) script lets me have my cake and eat it too - an image that refreshes daily with that extra functionality.

## How it works

* The script makes a call to the API here -> `https://peapix.com/api` using the requests library to get the daily bing image.
* Then, it uses the PIL/Pillow module to paste a timetable onto the bing image and add three blurred boxes to act as bins for folders
* Finally, it sets the sauced image as the desktop background

## Usage

To 
