#zju 1006 python 2.6+
import sys
fp, bp = '_abcdefghijklmnopqrstuvwxyz.', {}
for i, ch in enumerate(fp):
  bp[ch] = i
def decode(key, ciphertext):
  key , n = int(key), len(ciphertext)
  plaincode = [0]*n
  for i, ch in enumerate(ciphertext):
    plaincode[ (key*i) % n] = (bp[ch] + i) % 28
  plaintext = [fp[x] for x in plaincode]
  print(''.join(plaintext))

for line in sys.stdin:
  line = line.strip()
  if line == "0": break;
  key , ciphertext= line.split()
  decode(key, ciphertext)

