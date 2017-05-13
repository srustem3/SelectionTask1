f = open("Multiplication table.html", 'w')
f.write('<html>\n')
f.write('<link rel="stylesheet" type="text/css" href="styles.css" />\n')

f.write('<table border="1"\n')

for i in range(0, 11):
    f.write('\t<tr>\n')
    for j in range(0, 11):
        if j == 0:
            f.write('\t\t<th>' + str(i) + '</th>\n')
        elif i == 0:
            f.write('\t\t<th>' + str(j) + '</th>\n')
        else:
            f.write('\t\t<td>' + str(i * j) + '</td>\n')
    f.write('\t</tr>\n')

f.write('</table>\n</html>')
f.close()
