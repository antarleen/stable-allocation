def group_strength_checker_pref():
    for i in range(1, 31):
        while True:
            try:
                gs = int(input(f'Hi ! Group {i}, Please enter your group strength:'))
                if gs <= 3 and gs != 0:
                    print('Your group has been accepted !')
                    print('Please enter 5 mentor names as preference:')
                    for j in range(5):
                        while True:
                            try:
                                choice = int(
                                    input('Please enter a mentor Number:\n101 for A\n102 for B\n103 for C\n104 '
                                          'for '
                                          'D\n105 for E\n106 for F\n107 for G\n108 for H\n109 for I\n110 for '
                                          'I\n111 '
                                          'for J\n112 '
                                          'for K\n113 for L\n114 for M\n115 for N\n'))
                                if choice not in group_mentor_preference[i - 1]:
                                    group_mentor_preference[i - 1][j] = choice
                                    break
                                else:
                                    print('Mentor already selected, pick a different mentor !')
                            except ValueError:
                                print('Not a valid input !! Please enter again')

                    group_strength.append(gs)
                    break
                else:
                    print('Group must have between 1 and 3 people, please enter again !')
            except ValueError:
                print('Please enter a valid input !!')


def mentor_preference():
    for i in range(1, 16):
        print(f'Hi! Mentor {100 + i} !')
        for j in range(3):
            while True:
                try:
                    choice = int(input('Please enter a group Number as per preference:'))
                    if choice not in mentor_group_preference[i - 1]:
                        mentor_group_preference[i - 1][j] = choice
                        break
                    else:
                        print('Group already selected, pick a different group !')
                except ValueError:
                    print('Not a valid input !! Please enter again')


if __name__ == '__main__':
    group_mentor_preference = [[0] * 5 for _ in range(30)]
    mentor_group_preference = [[None] * 3 for _ in range(15)]
    mentor_dict = {101: [], 102: [], 103: [], 104: [], 105: [], 106: [], 107: [], 108: [], 109: [], 110: [], 111: [],
                   112: [], 113: [], 114: [], 115: []}
    group_strength = []
    group_strength_checker_pref()
    mentor_preference()
    # mentor assignment as per round and choice
    for a_round in range(5):
        for group in range(1, 31):
            if group not in mentor_dict:
                mentor_dict[group_mentor_preference[group - 1][a_round]].append(group)
        # ranking the selected groups and deleting the ones not relevant
        for key in mentor_dict:
            diff = [i for i in set(mentor_dict[key]).difference(set(mentor_group_preference[int(key % 100) - 1]))]
            for value in diff:
                mentor_dict[key].remove(value)
            # removing all groups except the highest ranked
            while len(mentor_dict[key]) > 3:
                lowest_pref = mentor_dict[key][0]
                for group in mentor_dict[key]:
                    if mentor_group_preference[int(key % 100) - 1].index(lowest_pref) < mentor_group_preference[
                            int(key % 100) - 1].index(group):
                        lowest_pref = group
                    mentor_dict[key].remove(lowest_pref)

    # final mentor allocation status
    print(mentor_group_preference)
    print(group_mentor_preference)
    print('The final mentor allocations are:')
    for keys in mentor_dict:
        print(f'\nMENTOR {keys} HAS BEEN ALLOCATED THE FOLLOWING GROUPS:\n')
        for groups in keys:
            print(groups + '\n')
