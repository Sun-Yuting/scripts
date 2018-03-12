import json
import os
import matplotlib.pyplot as plt


path = 'C:\\Users\\android-ML\\Documents\\GitHub\\openpose\\output\\'
file_list = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]


def main():
    # read files
    dict_list = []
    for file in file_list:
        with open(path+file, 'r') as current_file:
            dict_list.append(json.load(current_file))

    # get joint values
    person_a = []
    person_b = []
    for value in dict_list:
        # ignore unless both subjects are detected
        if len(value['people']) == 2:
            person_a.append(value['people'][0]['pose_keypoints_2d'])
            person_b.append(value['people'][1]['pose_keypoints_2d'])

    # look motion
    # to get head direction, use 16 & 17 to calculate
    joint0_a = [coord[3:5] for coord in person_a]

    #plt.plot([values[0] for values in joint0_a], [values[1] for values in joint0_a], 'ro')
    #plt.show()


if __name__ == '__main__':
    main()
