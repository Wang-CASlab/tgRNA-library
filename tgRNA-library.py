import re
datafin = []

with open('./GCA_001700985.1_ASM170098v1_cds_from_genomic.txt')as file_object:
    data1 = file_object.read()
    data2 = data1.split('>')
    for data in data2:
        p = data.replace('\n', '')
        if len(p) > 0:
            i = p.rindex(']')
            c = p[i + 1:]
            m = len(c) - 20
            x = 'TTA'
            q = [x.start() for x in re.finditer(x, c[0:m])]
            n = len(q)
            if n > 4:
                i = q[2]
                r = c[i + 3:i + 23]
                datafin.append(r)
                datafin.append('\n')

                i = q[n - 1]
                r = c[i + 3:i + 23]
                datafin.append(r)
                datafin.append('\n')

                i = q[int((n + 1) / 2)]
                r = c[i + 3:i + 23]
                datafin.append(r)
                datafin.append('\n')

            else:
                for i in q[:3]:
                    r = c[i + 3:i + 23]
                    datafin.append(r)
                    datafin.append('\n')

f2 = ('./tgRNA_library.txt')
with open(f2, 'w')as file_object:
    file_object.writelines(datafin)
