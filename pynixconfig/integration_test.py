from linuxconfig import get_full_path, config, get_color_code, get_font_code, main

color = "red"
font = "bold"

test_config = config(get_color_code(color), get_font_code(font))
main(color, font)

# command = "echo $LS_COLORS"
# output = os.popen(command).read()
# print(output)

config_format = "LS_COLORS=" + '"{}"'.format(test_config)

with open(get_full_path('~/.bashrc')) as f:
    for line in f:
        pass
    last_line = line

if last_line == config_format:
    print("TRUE")
else:
    print("test config: " + config_format)
    print("echo output: " + last_line)
    print("FALSE")
