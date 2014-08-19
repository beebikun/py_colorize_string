COLORS = dict(
    gray=('\033[1;30m', '\033[1;m'),
    red=('\033[1;31m', '\033[1;m'),
    green=('\033[1;32m', '\033[1;m'),
    yellow=('\033[1;33m', '\033[1;m'),
    blue=('\033[1;34m', '\033[1;m'),
    magenta=('\033[1;35m', '\033[1;m'),
    cyan=('\033[1;36m', '\033[1;m'),
    white=('\033[1;37m', '\033[1;m'),
    crimson=('\033[1;38m', '\033[1;m'),
    highlighted_red=('\033[1;41m', '\033[1;m'),
    highlighted_green=('\033[1;42m', '\033[1;m'),
    highlighted_brown=('\033[1;43m', '\033[1;m'),
    highlighted_blue=('\033[1;44m', '\033[1;m'),
    highlighted_magenta=('\033[1;45m', '\033[1;m'),
    highlighted_cyan=('\033[1;46m', '\033[1;m'),
    highlighted_gray=('\033[1;47m', '\033[1;m'),
    highlighted_crimson=('\033[1;48m', '\033[1;m')
)


def colorize(clr, s):
    color = COLORS[clr]
    return color[0] + s + color[1]
