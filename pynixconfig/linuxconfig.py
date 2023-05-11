# still need to deal with the case LSCOLORS alredy exists in .bashrc
import os
import os.path

font_dict = {
    "bold": "1",
    "underlined": "4",
}

color_dict = {  # change
    "red": "31",
    "green": "32",
    "orange": "33",
    "blue": "34",
    "purple": "35",
    "cyan": "36",
    "grey": "37",
}


def get_color_code(color_string):
    """
        Gets the color code from color string.

        Parameters
        ----------
        color_string : str
            color name

        Returns
        -------
        color_code: int
            color code
        """
    return color_dict[color_string]


def get_font_code(font_string):
    """
        Gets the font code from font string.

        Parameters
        ----------
        font_string : str
            font name

        Returns
        -------
        font_code: int
            font code
        """
    return font_dict[font_string]


def get_full_path(curr_path):
    """
        Gets the path of the current user

        Parameters
        ----------
        curr_path : str
            directory path of current directory

        Returns
        -------
        user_path: str
            user path
        """
    return os.path.expanduser(curr_path)


def config(color_c, font_c):
    """
        Gets the font code from font string.

        Parameters
        ----------
        color_code : str
            color code

        font_code: str
            font code

        Returns
        -------
        config: str
            config string to be inputted in .bashrc
        """
    return "di=" + font_c + ";" + color_c


def add_ls_colors(curr_text, text_add):
    """
        Add LS_COLORS configuration to .bashrc file.

        Parameters
        ----------
        curr_text : str
            current content of .bashrc file

        text_add: str
            config to add for LS_COLORS

        Returns
        -------
        output: str
            final version of .bashrc file
        """
    output = curr_text + "\n" + "LS_COLORS=" + '"{}"'.format(text_add)
    return output


def replace_ls_colors(config_string):
    """
        Replace current LS_COLORS configuration in .bashrc file

        Parameters
        ----------
        config_string : str
            new configuration to replace current LS_COLORS config

        Returns
        -------
        new_line: str
            line to add to .bashrc file
        """
    new_line = "LS_COLORS=" + '"{}"'.format(config_string)
    return new_line


def bash_shell(color_code):
    """
        Replace current PS1 configuration in .bashrc file

        Parameters
        ----------
        color_code : str
            code of color wanted for command line prompt

        Returns
        -------
        ps1: str
            PS1 configuration with color specified
        """
    ps1 = r'PS1="\e[0;' + color_code + r'm[\u@\h \W]\$ \e[m "'
    return ps1


def main(color, font, prompt):
    """
        Main function to modify content of .bashrc file

        Parameters
        ----------
        color : str
            name of color wanted for files

        font: str
            name of font wanted for files

        prompt: str
            name of color wanted for command line prompt

        Returns
        -------
        config_string: str
            configuration that was added to .bashrc file
        """
    path = "~/.bashrc"

    full_path = get_full_path(path)
    color_code = get_color_code(color)
    font_code = get_font_code(font)
    prompt_code = get_color_code(prompt)

    curr_colors = os.popen("echo $LS_COLORS").read()  # make into function?
    print(curr_colors)
    config_string = config(color_code, font_code)
    print(config_string)

    bashrc = open(full_path, "r")
    data = bashrc.read()

    search_line = 'LS_COLORS='
    exists = False
    with open(full_path, 'r') as file:
        lines = file.readlines()
    with open(full_path, 'w') as file:
        for line in lines:
            if search_line in line:
                exists = True
                file.write(replace_ls_colors(config_string))
            else:
                file.write(line)

    if exists is False:
        print("does not exist")
        fin_data = add_ls_colors(data, config_string)
        with open(full_path, "w") as file:
            file.write(fin_data)

        return fin_data.splitlines()[-1]
    if prompt != "":
        with open(full_path, 'a') as file:
            file.write("\n" + bash_shell(prompt_code))

    return replace_ls_colors(config_string)


if __name__ == "__main__":
    '''
    Possible colors:
    red
    green
    orange
    blue
    purple
    cyan
    grey

    Possible fonts:
    bold
    underlined

    NOTE: To see the changes in the terminal,
    you will need to restart the terminal
    '''

    color = "cyan"
    font = "bold"
    prompt = "red"
    main(color, font, prompt)
