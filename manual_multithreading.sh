#!/bin/bash

python3 ./Multi_PCSP_Generator.py 1 100 &
python3 ./Multi_PCSP_Generator.py 101 200 &
python3 ./Multi_PCSP_Generator.py 201 300 &
python3 ./Multi_PCSP_Generator.py 301 400 &
python3 ./Multi_PCSP_Generator.py 401 600 &

# Wait for all background processes to finish
wait

echo "All processes have completed."
