import sys


def get_args():
    date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender = '2021-02-21', 'Novak Djokovic', 'Daniil Medvedev', 'RH', 'RH', 'M'
    program_name = sys.argv[0]

    # Read arguments date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender from CLI
    if len(sys.argv) != 7:
        print("------------------------------------------------------------------------------------------------------------------------")
        print(
            f"Usage: python3 {program_name} <date> <ply1_name> <ply2_name> <ply1_hand> ply2_hand> <gender>")
        print("------------------------------------------------------------------------------------------------------------------------")
        print(
            f"Falling back to default values:\n  date: {date}\n  ply1_name: {ply1_name}\n  ply2_name: {ply2_name}\n  ply1_hand: {ply1_hand}\n  ply2_hand: {ply2_hand}\n  gender: {gender}"
        )
        print("------------------------------------------------------------------------------------------------------------------------")
    else:
        date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender = sys.argv[1:]
        print("------------------------------------------------------------------------------------------------------------------------")
        print(
            f"Using values:\n  date: {date}\n  ply1_name: {ply1_name}\n  ply2_name: {ply2_name}\n  ply1_hand: {ply1_hand}\n  ply2_hand: {ply2_hand}\n  gender: {gender}"
        )
        print("------------------------------------------------------------------------------------------------------------------------")

    return date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender
