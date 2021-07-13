import os
import sys


def convert(dir_name, output):
  l = os.listdir(dir_name)
  l.sort()

  files_to_pdf = []
  for path in l:
    if (os.path.isfile(dir_name + "/" + path)):
      files_to_pdf.append('"'+dir_name + '/' + path+'"')

  cmd = 'convert '+" ".join(files_to_pdf)+' '+dir_name+'/'+output
  print(cmd)
  os.system(cmd)

def main():
  print(len(sys.argv))
  if len(sys.argv) != 2:
    return 1
  dir_name = sys.argv[1]
  output = dir_name.split('/')[-1]+'.pdf'
  convert(dir_name, output)
  return 0

if __name__ == "__main__":
  main()
