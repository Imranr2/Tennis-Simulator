from generate_pcsp_helpers_extra_shots.get_params import get_params
from tqdm import tqdm as tqdm
import warnings
warnings.simplefilter("ignore")


# generate pcsp file
def generate_pcsp_extra_shots(data, date, ply1_name, ply2_name, ply1_hand, ply2_hand, pcsp_filename):
    params = get_params(
        data, date, ply1_name, ply2_name, ply1_hand, ply2_hand
    )
    VAR = 'generate_pcsp_helpers_extra_shots/var.txt'
    HAND = 'generate_pcsp_helpers_extra_shots/%s_%s.txt' % (ply1_hand, ply2_hand)
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
