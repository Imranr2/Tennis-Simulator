import sys


def get_args():
    date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender, pcsp_filename = '2021-02-21', 'Novak Djokovic', 'Daniil Medvedev', 'RH', 'RH', 'M', '1.pcsp'
    program_name = sys.argv[0]

    # Read arguments date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender from CLI
    if len(sys.argv) != 8:
        print("------------------------------------------------------------------------------------------------------------------------")
        print(
            f"Usage: python3 {program_name} <date> <ply1_name> <ply2_name> <ply1_hand> ply2_hand> <gender> <pcsp_filename>")
        print("------------------------------------------------------------------------------------------------------------------------")
        print(
            f"Falling back to default values:\n  date: {date}\n  ply1_name: {ply1_name}\n  ply2_name: {ply2_name}\n  ply1_hand: {ply1_hand}\n  ply2_hand: {ply2_hand}\n  gender: {gender}\n  pcsp_filename: {pcsp_filename}"
        )
        print("------------------------------------------------------------------------------------------------------------------------")
    else:
        date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender, pcsp_filename = sys.argv[1:]
        print("------------------------------------------------------------------------------------------------------------------------")
        print(
            f"Using values:\n  date: {date}\n  ply1_name: {ply1_name}\n  ply2_name: {ply2_name}\n  ply1_hand: {ply1_hand}\n  ply2_hand: {ply2_hand}\n  gender: {gender}\n  pcsp_filename: {pcsp_filename}"
        )
        print("------------------------------------------------------------------------------------------------------------------------")

    return date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender, pcsp_filename
