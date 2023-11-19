import subprocess
import sys
import os
import csv

def callPAT(patPath):
  patOutputFile =  "./result_2018.txt"
  
  for model in ["APPROACH", "BASELINE", "EXTRA_SHOTS", "PREV_SHOTS", "DEPTH"]:
    mdpPredFile = f"./MDP_pred_2018.csv"

    f = open(patOutputFile, "w")
    f.close()
    mdpPredLines = [line for line in csv.reader(open(mdpPredFile, 'r'))]
    newMdpPredFp = open(f"./MDP_pred_with_prob/2018/MDP_pred_new_{model}.csv", 'w')
    newMdpPred = csv.writer(newMdpPredFp)
    header = ["date","P1Name","P2Name","P1WinProb","P2WinProb","P1Hand","P2Hand","Gender"]
    newMdpPred.writerow(header)
    for i in range(1, len(mdpPredLines)):
      args = [patPath + "/PAT3.Console.exe", "-pcsp", f"./pcsp_files_2018/{i}_{model}.pcsp", os.getcwd() + patOutputFile]
      subprocess.call(args)
      
      p1Win = 0
      p2Win = 0
      fp = open(patOutputFile, 'r')
      for j, line in enumerate(fp):
        if j == 3:
          if "NOT valid" in line:
            continue
          probability = line.split("Probability")[1].strip()
          lowerBound, upperBound = probability[1:-2].split(',')
          p1Win = (float(lowerBound) + float(upperBound)) / 2
          p2Win = 1 - p1Win
      
      curLine = mdpPredLines[i]
      curLine[3], curLine[4] = p1Win, p2Win
      if p1Win == 0 or p2Win == 0:
        continue
      newMdpPred.writerow(curLine)

args = sys.argv
if len(args) != 2:
  raise Exception("python3 Update_Probabilities.py <patPath>")
patPath = args[1]
callPAT(patPath)
