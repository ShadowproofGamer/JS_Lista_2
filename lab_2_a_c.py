def lab2ac():
    import lab_2_line_filter as lf
    i=0
    while True:
        try:
            line = input()
            if(lf.line_filter(line)[8] == "404"): i+=1
            #print(line)
        except EOFError:
            break
        except Exception:
            continue
    print(i)
if __name__ == "__main__": lab2ac()