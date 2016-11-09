for line in open("ELECTION_ID"):



total = 0
for l in open("salaries.csv"):
if "FIRE" not in l: continue
sl = l.strip (). split(",")
total += float(sl[4][1:])
print("Total fire salaries:")
print(" $ {:.2f}".format(total ))

file_name = year +".csv" with open(file_name, "w") as out: out.write(resp.text)
