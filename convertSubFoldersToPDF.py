import sys
import os

from convertToPDF import convert

def main():
  if len(sys.argv) != 2:
    return 1
  package = sys.argv[1]
  dirs = os.listdir(package)
  for dir in dirs:
    dir_name = package+'/'+dir
    output = dir+'.pdf'
    convert(dir_name, output)
  return 0

if __name__ == "__main__":
  main()