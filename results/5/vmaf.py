import json
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', default='vmaf.json')
args = parser.parse_args()

with open(args.input, "r") as f:
    result = json.load(f)
  
plt.figure(figsize=(10, 5))  
frames = result['frames']
keys = frames[0]['metrics'].keys()
print(keys)
x = [frame['frameNum'] for frame in frames]
y = [frame['metrics']["vmaf"] for frame in frames]

plt.plot(x,y)
    
plt.title("vmaf evaluation")
plt.xlabel("Frame")
plt.ylabel("vmaf")
        
plt.savefig('vmaf.png')
plt.show()