# Tennis-Simulator

## Testing Locally

Note that the steps to create the PCSP files and update the probabilities are not necessary if you are only testing locally. **The files are already generated and included in the repository, so the steps bellow are just for verification purposes only.**

### Creating the PCSP files

To create the PCSP files, run the following commands:

```bash
python3 Multi_PCSP_Generator_2018.py
python3 Multi_PCSP_Generator_2020.py
python3 Multi_PCSP_Generator_2022.py
```

These commands will create the PCSP files for the 2018, 2020, and 2022 years. They will be located in the directories `pcsp_files_2018`, `pcsp_files_2020`, and `pcsp_files_2022` respectively. Note that the generation takes a long time, so it is recommended to run these commands in parallel in different terminal sessions.

Note that for the year 2018, we have 5 models:

1. Approach
1. Depth
1. Extra Shots
1. Previous Shots
1. Baseline

For the years 2020 and 2022, we have 2 models:

1. Approach
1. Baseline

### Updating probabilities

To update the probabilities using the newly generated PCSP files, run the following commands:

```bash
python3 Update_Probabilities_2018.py <PATH_TO_DIR_THAT_CONTAINS_PAT_EXE>
python3 Update_Probabilities_2020.py <PATH_TO_DIR_THAT_CONTAINS_PAT_EXE>
python3 Update_Probabilities_2022.py <PATH_TO_DIR_THAT_CONTAINS_PAT_EXE>
```

If you are using windows, it is best to run this in WSL and provide the path to the PAT executable in the WSL environment. For example:

```bash
python3 Update_Probabilites_2022.py "/mnt/c/Program Files/Process Analysis Toolkit/Process Analysis Toolkit 3.5.1"
```

These commands will update the probabilities for the 2018, 2020, and 2022 years. They will be located in the directories `MDP_pred_with_prob/2018`, `MDP_pred_with_prob/2020`, and `MDP_pred_with_prob/2022` respectively. Note that the generation takes a long time, so it is recommended to run these commands in parallel in different terminal sessions.

### Running the betting simulation

To run the betting simulation, run the following command:

```bash
python3 Betting_Simulation.py
```

This command will run the betting simulation for the 2018, 2020, and 2022 years. The results will be printed out in the terminal.
