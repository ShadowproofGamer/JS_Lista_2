#[01/Jul/1995:00:00:11
def lab2g():
    import lab_2_line_filter as lf
    import datetime as dt
    while True:
        try:
            line = input()
            temp = lf.line_filter(line)[3][1:12:]
            #print(temp)
            #print(dt.datetime.strptime(temp, '%d/%b/%Y').strftime('%a'))
            if(dt.datetime.strptime(temp, '%d/%b/%Y').strftime('%a')=="Fri"): 
                print(line)
        except EOFError:
            break
        except Exception:
            continue
if __name__ == "__main__": lab2g()