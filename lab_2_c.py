def lab2c():
    import lab_2_line_filter as lf
    maxB=0
    maxSource=''
    while True:
        try:
            line = input()
            temp = lf.line_filter(line)
            if int( temp[9]) > maxB:
                maxB = int(temp[9])
                maxSource = temp[6]
            #print(line)
        except EOFError:
            break
        except Exception:
            continue
    print(maxSource, maxB)
if __name__ == "__main__": lab2c()