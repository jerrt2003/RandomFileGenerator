#!/usr/local/bin/python2.7
import shutil
import argparse
import random, string
import zipfile
import os

__author__ = 'David Cheng'

arg_parser = argparse.ArgumentParser(description="A random sample generator which support: apk16a/apk16x/office 2007+ files(docx,xlsx,pptx)", formatter_class=argparse.RawTextHelpFormatter)
arg_parser.add_argument('ftype', metavar='file_type', type=str, help='src file type (options: docx/pptx/xlsx/apk16x/apk16a)')
arg_parser.add_argument('src_path', metavar='src', type=str, help='provide src office file path')

args = arg_parser.parse_args()
src = args.src_path
ftype = args.ftype

r_string = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))

if ftype == "apk16x" or ftype == "apk16a" or ftype == "jar":
	if ftype == "apk16a":
		dst = 'apk16a_%s.apk' % r_string
	elif ftype == "apk16x":
		dst = 'apk16x_%s.apk' % r_string
	else:
		dst = '%s.jar' % r_string
	shutil.copy(src, dst)
	apk_path = os.path.abspath(dst)
	with zipfile.ZipFile(apk_path,'a') as testzip:
		testzip.comment = r_string
elif ftype in ["docx", "xlsx", "pptx"]:
	if ftype == "docx":
		dst = "%s.docx" % r_string
	elif ftype == "xlsx":
		dst = "%s.xlsx" % r_string
	elif ftype == "pptx":
		dst = "%s.pptx" % r_string
	else:
		pass
	shutil.copy(src, dst)
	random_file = open(r_string, 'w')
	random_file.write(r_string)
	random_file.close()
	z = zipfile.ZipFile(dst,'a')
	z.write(r_string)
	os.remove(r_string)
else:
	print "%s is not currently supported. please check again" % ftype
	exit(1)

print dst
