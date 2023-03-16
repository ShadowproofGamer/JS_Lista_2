#[01/Jul/1995:00:00:11
def lab2f():
    import lab_2_line_filter as lf
    while True:
        try:
            line = input()
            temp = lf.line_filter(line)[3][-8:-6:]
            #print(temp)
            if(int(temp)<6 or int(temp)>=22): 
                print(line)
        except EOFError:
            break
        except Exception:
            continue

if __name__ == "__main__": lab2f()