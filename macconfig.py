# still need to deal with the case LSCOLORS does not exist yet in bash_profile

import os
import os.path
import sys

n = len(sys.argv)
color = sys.argv[1]
print(color)

path='~/.bash_profile'
full_path = os.path.expanduser(path)

color_dict = {
    "black": "a",
    "red": "b",
    "green": "c",
    "brown": "d",
    "blue": "e",
    "magenta": "f",
    "cyan": "g",
    "gray": "h",
    "bold-red": "B",
    "bold-green": "C",
    "bold-brown": "D",
    "bold-blue": "E",
    "bold-magenta": "F",
    "bold-cyan": "G",
    "bold-gray": "H",
}

color_code = color_dict[color]
curr_colors = os.popen('printenv LSCOLORS').read()
search_text = "export LSCOLORS="+curr_colors
print(search_text)
replace_text = "export LSCOLORS="+ color_code + "xfxcxdxbxegedabagacad\n"
print(replace_text)

bash_profile = open(full_path, 'r')
data = bash_profile.read()
data = data.replace(search_text, replace_text)
#print(data)

with open(full_path, 'w') as file:
    file.write(data)

source_command = "source " + full_path
print(source_command)
os.system(source_command)