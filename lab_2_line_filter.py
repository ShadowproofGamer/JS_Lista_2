def line_filter(line):
    data = line.split(" ")
    if( len(data)!=10 or data[1]!="-" or data[2]!="-" or data[5]!='"GET' or data[7]!='HTTP/1.0"' or ["200", "302", "404"].count(data[8])==0): raise Exception("wrong format")
    #or ["200", "302", "404"].count(data[8])==0
    else: return data

"""
output:
[0]: //website
[1]: '-'
[2]: '-'
[3]: '[//data'
[4]: '-//code]'
[5]: '"GET'
[6]: //resource
[7]: 'HTTP/1.0"'
[8]: //code HTTP
[9]: //number of B

"""