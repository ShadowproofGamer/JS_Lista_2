def lab2ab():
    import lab_2_line_filter as lf
    i=0
    while True:
        try:
            line = input()
            if(lf.line_filter(line)[8] == "302"): i+=1
        except EOFError:
            break
        except Exception:
            continue
    print(i)
if __name__ == "__main__": lab2ab()