from generate_pcsp_helpers.setup import get_args
from generate_pcsp_helpers.read_file import read_data_from_csv
from generate_pcsp_helpers.get_params import get_params
from tqdm import tqdm as tqdm
import warnings
warnings.simplefilter("ignore")


# generate pcsp file
def generate_pcsp(data, date, ply1_name, ply2_name, ply1_hand, ply2_hand, pcsp_filename):
    params = get_params(
        data, date, ply1_name, ply2_name, ply1_hand, ply2_hand
    )
    VAR = 'var.txt'
    HAND = '%s_%s.txt' % (ply1_hand, ply2_hand)
    # Keeping it here in case its needed
    # file_name = '%s_%s_' % (hand1, hand2)
    # file_name += '%s_%s_%s.pcsp' % (date, ply1_name.replace(' ',
    #                                '-'), ply2_name.replace(' ', '-'))
    # write to file
    lines = []
    with open(VAR) as f:
        lines_1 = f.readlines()
    lines_2 = []
    for i, p in enumerate(params):
        lines_2.append('#define p%d %d;\n' % (i, p))
    with open(HAND) as f:
        lines_3 = f.readlines()
    lines = lines_1 + lines_2 + lines_3
    with open(pcsp_filename, 'w') as f:
        for line in lines:
            f.write(line)


# date, ply1_name, ply2_name, ply1_hand, ply2_hand, gender, pcsp_filename = get_args()


# generate_pcsp(date, ply1_name, ply2_name, ply1_hand, ply2_hand, pcsp_filename)
