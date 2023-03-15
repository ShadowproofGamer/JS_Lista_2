def line_filter(line):
    data = line.split(" ")
    if( data.count()!=10 or data[1]!="-" or data[2]!="-" or data[5]!='"GET' or data[7]!='HTTP/1.0"' ): Exception("wrong format")
    else: return data

def input_filter():
    data = []
    while True:
        try:
            line = input()
            data.append(line_filter(line))
        except EOFError:
            break
        except Exception:
            continue
    return data

def file_filter(file):
    data = []
    while True:
        try:
            line = input
            data.append(line_filter(line))
        except EOFError:
            break
    return data