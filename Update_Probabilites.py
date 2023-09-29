import subprocess
import sys
import os
import csv

def callPAT(patPath, count):
  patOutputFile =  "./result.txt"
  mdpPredFile = "./MDP_pred.csv"

  f = open(patOutputFile, "w")
  f.close()
  mdpPredLines = [line for line in csv.reader(open(mdpPredFile, 'r'))]
  newMdpPredFp = open("./MDP_pred_new.csv", 'w')
  newMdpPred = csv.writer(newMdpPredFp)
  header = ["date","P1Name","P2Name","P1WinProb","P2WinProb","P1Hand","P2Hand","Gender"]
  newMdpPred.writerow(header)
  for i in range(1, count + 1):
    args = [patPath + "/PAT3.Console.exe", "-pcsp", f"./pcsp_files/{i}.pcsp", patOutputFile]
    subprocess.call(args)
    
    p1Win = 0
    p2Win = 0
    fp = open(patOutputFile, 'r')
    for j, line in enumerate(fp):
      if j == 3:
        probability = line.split("Probability")[1].strip()
        lowerBound, upperBound = probability[1:-2].split(',')
        p1Win = (float(lowerBound) + float(upperBound)) / 2
        p2Win = 1 - p1Win
    
    curLine = mdpPredLines[i]
    curLine[3], curLine[4] = p1Win, p2Win
    newMdpPred.writerow(curLine)

args = sys.argv
if len(args) != 3:
  raise Exception("python3 Update_Probabilities.py <patPath> <count>")
patPath, count = args[1:]
callPAT(patPath, int(count))