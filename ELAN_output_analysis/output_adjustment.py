from datetime import datetime
import math


def main():
    target_file = 'friend2'
    delta = 261.752
    min_delta = f'{math.floor(delta/60)}:{math.floor(delta)%60}.{delta-math.floor(delta)}'

    # read
    f_utter = []
    m_utter = []
    with open(f'D:\\SunYuting\\{target_file}.txt', encoding='utf-8_sig') as file:
        for line in file:
            line = line.split('\t')
            if line[0] == 'F_utterance':
                f_utter.append(line)
            elif line[0] == 'M_utterance':
                m_utter.append(line)
            else:
                pass

    # adjust
    # TODO milliseconds formation
    f_out = []
    m_out = []
    for el in f_utter:
        el[2] = datetime.strptime(el[2], '%H:%M:%S.%f') - datetime.strptime(min_delta, '%M:%S.%f')
        el[3] = float(el[3]) - delta
        el[4] = datetime.strptime(el[4], '%H:%M:%S.%f') - datetime.strptime(min_delta, '%M:%S.%f')
        el[5] = float(el[5]) - delta
        f_out.append([str(i) for i in el])
    for el in m_utter:
        el[2] = datetime.strptime(el[2], '%H:%M:%S.%f') - datetime.strptime(min_delta, '%M:%S.%f')
        el[3] = float(el[3]) - delta
        el[4] = datetime.strptime(el[4], '%H:%M:%S.%f') - datetime.strptime(min_delta, '%M:%S.%f')
        el[5] = float(el[5]) - delta
        m_out.append([str(i) for i in el])

    # write
    with open(f'D:\\SunYuting\\ELAN_outputs\\{target_file}.txt', 'w', encoding='utf-8_sig') as file:
        for el in f_out:
            file.write('\t'.join(el))
        for el in m_out:
            file.write('\t'.join(el))


if __name__ == '__main__':
    main()
