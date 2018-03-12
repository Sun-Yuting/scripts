from datetime import datetime


def main():
    delta = 31.335

    # read
    f_utter = []
    m_utter = []
    with open('D:\\SunYuting\\couple.txt', encoding='utf-8_sig') as file:
        for line in file:
            line = line.split('\t')
            if line[0] == 'F_Utterance':
                f_utter.append(line)
            elif line[0] == 'M_Utterance':
                m_utter.append(line)
            else:
                pass

    # adjust
    # TODO milliseconds formation
    f_out = []
    m_out = []
    for el in f_utter:
        el[2] = datetime.strptime(el[2], '%H:%M:%S.%f') - datetime.strptime(str(delta), '%S.%f')
        el[3] = float(el[3]) - delta
        el[4] = datetime.strptime(el[4], '%H:%M:%S.%f') - datetime.strptime(str(delta), '%S.%f')
        el[5] = float(el[5]) - delta
        f_out.append([str(i) for i in el])
    for el in m_utter:
        el[2] = datetime.strptime(el[2], '%H:%M:%S.%f') - datetime.strptime(str(delta), '%S.%f')
        el[3] = float(el[3]) - delta
        el[4] = datetime.strptime(el[4], '%H:%M:%S.%f') - datetime.strptime(str(delta), '%S.%f')
        el[5] = float(el[5]) - delta
        m_out.append([str(i) for i in el])

    # write
    with open('D:\\SunYuting\\ELAN_outputs\\couples.txt', 'w', encoding='utf-8_sig') as file:
        for el in f_out:
            file.write('\t'.join(el))
        for el in m_out:
            file.write('\t'.join(el))


if __name__ == '__main__':
    main()
