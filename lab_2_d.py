def lab2d():
    import lab_2_line_filter as lf
    all=0
    graphics=0
    while True:
        try:
            line = input()
            temp = lf.line_filter(line)
            all+=1
            if [".gif", ".jpg", "jpeg",".xbm"].count(temp[6][-4::])!=0:
                graphics+=1
            #print(temp[6][-4::])
        except EOFError:
            break
        except Exception:
            continue
    print(graphics,"/", all)
if __name__ == "__main__": lab2d()