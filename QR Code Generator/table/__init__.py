def line(simb='-', scale=70):
    return simb * scale


def header(message='Empty', simb='-', scale=70):
    print(line(simb, scale))
    print(message.center(scale))
    print(line(simb, scale))