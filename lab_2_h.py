def lab2h():
    import lab_2_line_filter as lf
    while True:
        try:
            line = input()
            temp = lf.line_filter(line)[0][-3::]
            #print(temp)
            #print(dt.datetime.strptime(temp, '%d/%b/%Y').strftime('%a'))
            if(temp==".pl"): 
                print(line)
        except EOFError:
            break
        except Exception:
            continue
if __name__ == "__main__": lab2h()
#print(__name__)