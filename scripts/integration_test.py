from linuxconfig import get_full_path, config, get_color_code, get_font_code, main
import os

color = "red"
font = "bold"

test_config = config(get_color_code(color), get_font_code(font))
main(color, font)

command = "echo $LS_COLORS"
output = os.system(command)
print(output)

assert output == test_config

