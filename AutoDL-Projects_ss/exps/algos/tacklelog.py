import re, argparse, os
from pathlib import Path
import numpy as np

parser = argparse.ArgumentParser("DARTS first order")
parser.add_argument('-f',type=str,help='Path to dataset')
args = parser.parse_args()
#Path('/root/dir/sub/file.ext').stem
#seed=os.path.splitext(os.path.basename(args.f))[0].split('-')[1]

archParaTensorList=[]
with open(args.f,'r') as logFile:
    pattern = r'tensor\(([^\)]+)\)'
    regex = re.compile(pattern, flags=re.IGNORECASE)
    fileContent=logFile.read()
    archParaList=regex.findall(fileContent)
    for archPara in archParaList:
        archParaTensorList.append(np.array(eval(archPara.replace('\n',''))))

archParaTensor=np.stack(archParaTensorList)
print(archParaTensor[0])
print(archParaTensor[-1])
