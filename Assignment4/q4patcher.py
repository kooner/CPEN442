import argparse
import hashlib

from os.path import isfile

# The offset was found with f.read().find("\x30\x74\xFC\xCB\x85\x89\x95\xCA\x25\xB5\x04\x76\x45\xEB\x74\xAB\x7C\x26\x62\x10")
# since 3074FCCB858995CA25B5047645EB74AB7C266210 is my SHA-1 hash
# It is hard coded below so that we can repeatedly patch the exe since the byte string won't exist after a patch but
# the offset will still be the same.
offset = 75807

parser = argparse.ArgumentParser(description="Patch the file to accept a different password")
parser.add_argument("--exe", default="33263112.program2.exe", type=str, help="name of the exe file to patch")
parser.add_argument("-p", "--password", required=True, type=str, help="new password")
args = parser.parse_args()

if isfile(args.exe):
    sha1 = hashlib.sha1(args.password).digest()
    with open(args.exe, "r+b") as f:
        f.seek(offset)
        f.write(sha1)
else:
    print "The file %s doesn't exist!" % args.exe
