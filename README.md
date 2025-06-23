# Persistent Bing Wallpapers

A python (3.12.3) script that gets the daily bing image, adds some sauce, and sets it as the desktop background.

## Why?

I have used the Daily Bing Wallpaper utility for a while now - it automatically changes my wallpaper every day and I like having something fresh on my desktop.
That said, I also like my desktop to have some *sauce* (a timetable widget, or some boxes to organise my folders in).
This (very amateur) script lets me have my cake and eat it too - an image that refreshes daily with some extra features.

## How it works

* The script makes a call to the API here -> `https://peapix.com/api` using the requests library to get the daily bing image.
* Then, it uses the PIL/Pillow module to paste a timetable onto the bing image and add three blurred boxes to act as bins for folders
* Finally, it sets the sauced image as the desktop background

## Usage

If you would like to use this yourself (for whatever reason):
* You must be using Windows (unfortunately the wallpaper setting command is Windows-specific)
* Just save the python script to your machine and modify the `save_path` and `set_path` variables right at the very bottom (it's probably best to use absolute paths for both)
* If you would like to add a timetable (or any other image) just save your image in the same folder as the python script and update the `image_path` variable in the script.
* I'm in the process of trying to automate the script using batch files and Windows Task Scheduler (see `https://www.makeuseof.com/tag/use-windows-batch-file-commands-automate-repetitive-tasks/`) - feel free to try this if you'd like the script to update your wallpaper daily (you may have more luck than me!!!)

### Thanks!
Any tips/advice/recommendations are very welcome :)
