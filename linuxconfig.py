# still need to deal with the case LSCOLORS alredy exists in .bashrc

import os
import os.path
import sys

n = len(sys.argv)
print(n)
font = sys.argv[1]
color = sys.argv[2]

path='~/.bashrc'
full_path = os.path.expanduser(path)
print(full_path)

font_dict = {
    "bold": "1",
    "underlined": "4",
}

color_dict = { # change
    "red": "31",
    "green": "32",
    "orange": "33",
    "blue": "34",
    "purple": "35",
    "cyan": "36",
    "grey": "37",
}

color_code = color_dict[color]
font_code = font_dict[font]
curr_colors = os.popen('echo $LS_COLORS').read()
print(curr_colors)
config_string = "di="+font_code+";"+color_code
print(config_string)
#if curr_colors = "": # undefined or whatever it is
    #add line to end of .bashrc file
#else:
search_text = "LS_COLORS="+curr_colors
print(search_text)
replace_text = "LS_COLORS="+ config_string
print(replace_text)

bashrc = open(full_path, 'r')
data = bashrc.read()
#data = data.replace(search_text, replace_text)
data = data + "\n" + "LS_COLORS=" + '"{}"'.format(config_string)

with open(full_path, 'w') as file:
    file.write(data)

