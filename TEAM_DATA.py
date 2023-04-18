import pandas as pd
import os
os.getcwd()
os.chdir("D:\\BZAN556\\TEAM")
I = 17
N = 98

d = pd.read_excel("18.Data_Teams.xlsx", "Sheet2", index_col="Student_Id")

#g = pd.read_excel("18.Data_Teams.xlsx", "Sheet1", index_col="Race")

f = open("teams.dat", "w")
end = "; \n"
f.write("param f:= \n")
d.Female.to_csv(f, sep = ' ', header = False, index = True)
f.write(end)

f.write("param a:= \n")
d.Race.to_csv(f, sep = ' ', header = False, index = True)
f.write(end)

f.write("param s:= \n")
for i in range(1,I+1):
    for t in range(1,I+1):
        for n in range(1,N+1):
            if t > 1:
                s = d.iloc[i-1,n+3]
            else:
                s = 0
            line = [i,t,n,s]
            line1 = ' '.join(str(e) for e in line)
            f.write(line1)
            f.write("\n")
f.write(end)

f.write("param gpa:= \n")
for i in range(1,I+1):
    for t in range(1,I+1):
            if t > i:
                gpa = abs(d.GPA[i]-d.GPA[t])
            else:
                gpa = 0
            line = [i,t,gpa]
            line2 = ' '.join(str(e) for e in line)
            f.write(line2)
            f.write("\n")
f.write(end)

f.write("param m:= \n")
for i in range(1,I+1):
    for t in range(1,I+1):
            if t > i:
                if d.Major[i]-d.Major[t] == 0:
                    m = 1
                else: 
                    m = 0                     
            else:
                m = 0
            line = [i,t,m]
            line3 = ' '.join(str(e) for e in line)
            f.write(line3)
            f.write("\n")
f.write(end)
f.close()