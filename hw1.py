import argparse
import os, time
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--mtime", help="modification time", action="store_true")
parser.add_argument("-s", "--size", help="file size", action="store_true")
parser.add_argument("--rename", help= "rename a file", action="store_true")
args = parser.parse_args()
file = "hw1.py"
st = os.stat(file)
if args.mtime:
    print("last modified: %s" % time.ctime(st.st_mtime))
if args.size:
    print("file size: %s" % (st.st_size / 2**10))
if args.rename:
    os.rename("hw1.py", "B.py")



