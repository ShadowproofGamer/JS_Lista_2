def lab2e():
    import lab_2_line_filter as lf
    while True:
        try:
            line = input()
            if(lf.line_filter(line)[8] == "200"): 
                print(line)
        except EOFError:
            break
        except Exception:
            continue
if __name__ == "__main__": lab2e()