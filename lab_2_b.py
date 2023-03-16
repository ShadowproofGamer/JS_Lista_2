def lab2b():
    import lab_2_line_filter as lf
    i=0
    while True:
        try:
            line = input()
            i += int(lf.line_filter(line)[9])
            #print(line)
        except EOFError:
            break
        except Exception:
            continue
    print(i/(1024*1024*1024))
if __name__ == "__main__": lab2b()