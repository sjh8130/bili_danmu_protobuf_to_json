#!/usr/bin/python3
import json
import sys
import re
import time

Start_Time = time.time()
jsonData = ""
try:
	input_PATH = sys.argv[1]
except IndexError:
	print("No Input")
	sys.exit(1)

PathSuffix = re.split("//", input_PATH)[-1]					# Unix,Linux,Windows
if len(re.split("//", input_PATH)) >1:
	PathSuffix = re.split("\\\\", input_PATH)[-1]			# Windows
PathPrefix = input_PATH.rstrip(PathSuffix)
outputFile = PathPrefix + PathSuffix.rstrip(".json")+".xml"

Split_SIZE = 2500

with open(input_PATH, "r", encoding="utf-8")as f:
	jsonData = f.read()

try: jsonData = json.loads(jsonData)
except json.decoder.JSONDecodeError:
	print("\033[41m==============================ERROR=============================\033[0m")
	if len(jsonData) <= 2:	print("\033[41m Empty File\033[0m")
	print("总计用时:", time.time()-Start_Time)
	sys.exit(1)
try:
	cid = re.split("_", PathSuffix)[4]							# publistTime_BV**_av**_P*_cid_Title_P-Title.json
except IndexError:
	pass
try:
	cid = re.split("\]",re.split("\]\[", PathSuffix)[3])[0]		# [BV**][av**][P*][cid]Title_P-Title.json
except IndexError:
	cid = "ERROR"
XML_item = ""

danmu_count = len(jsonData["elems"])
XML_Data_1st_Cache = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
XML_Data_2nd_Cache = ""

for i in range(danmu_count):
	Sub_Item = jsonData["elems"][i]

	try: content = Sub_Item["content"]		# string content = 7;
	except KeyError: continue
	content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\x08","")

	string_attr = [
		"<!-- 。。 。。 。。 。。 。。 。。 。。 -->",				# 0000000
		"<!-- 保护 。。 。。 。。 。。 。。 。。 -->",				# 0000001
		"<!-- 。。 直播 。。 。。 。。 。。 。。 -->",				# 0000010
		"<!-- 保护 直播 。。 。。 。。 。。 。。 -->",				# 0000011
		"<!-- 。。 。。 高赞 。。 。。 。。 。。 -->",				# 0000100
		"<!-- 保护 。。 高赞 。。 。。 。。 。。 -->",				# 0000101
		"<!-- 。。 直播 高赞 。。 。。 。。 。。 -->",				# 0000110
		"<!-- 保护 直播 高赞 。。 。。 。。 。。 -->",				# 0000111
		"<!-- 。。 。。 。。 未一 。。 。。 。。 -->",				# 0001000
		"<!-- 保护 。。 。。 未一 。。 。。 。。 -->",				# 0001001
		"<!-- 。。 直播 。。 未一 。。 。。 。。 -->",				# 0001010
		"<!-- 保护 直播 。。 未一 。。 。。 。。 -->",				# 0001011
		"<!-- 。。 。。 高赞 未一 。。 。。 。。 -->",				# 0001100
		"<!-- 保护 。。 高赞 未一 。。 。。 。。 -->",				# 0001101
		"<!-- 。。 直播 高赞 未一 。。 。。 。。 -->",				# 0001110
		"<!-- 保护 直播 高赞 未一 。。 。。 。。 -->",				# 0001111
		"<!-- 。。 。。 。。 。。 未二 。。 。。 -->",				# 0010000
		"<!-- 保护 。。 。。 。。 未二 。。 。。 -->",				# 0010001
		"<!-- 。。 直播 。。 。。 未二 。。 。。 -->",				# 0010010
		"<!-- 保护 直播 。。 。。 未二 。。 。。 -->",				# 0010011
		"<!-- 。。 。。 高赞 。。 未二 。。 。。 -->",				# 0010100
		"<!-- 保护 。。 高赞 。。 未二 。。 。。 -->",				# 0010101
		"<!-- 。。 直播 高赞 。。 未二 。。 。。 -->",				# 0010110
		"<!-- 保护 直播 高赞 。。 未二 。。 。。 -->",				# 0010111
		"<!-- 。。 。。 。。 未一 未二 。。 。。 -->",				# 0011000
		"<!-- 保护 。。 。。 未一 未二 。。 。。 -->",				# 0011001
		"<!-- 。。 直播 。。 未一 未二 。。 。。 -->",				# 0011010
		"<!-- 保护 直播 。。 未一 未二 。。 。。 -->",				# 0011011
		"<!-- 。。 。。 高赞 未一 未二 。。 。。 -->",				# 0011100
		"<!-- 保护 。。 高赞 未一 未二 。。 。。 -->",				# 0011101
		"<!-- 。。 直播 高赞 未一 未二 。。 。。 -->",				# 0011110
		"<!-- 保护 直播 高赞 未一 未二 。。 。。 -->",				# 0011111
		"<!-- 。。 。。 。。 。。 。。 未三 。。 -->",				# 0100000
		"<!-- 保护 。。 。。 。。 。。 未三 。。 -->",				# 0100001
		"<!-- 。。 直播 。。 。。 。。 未三 。。 -->",				# 0100010
		"<!-- 保护 直播 。。 。。 。。 未三 。。 -->",				# 0100011
		"<!-- 。。 。。 高赞 。。 。。 未三 。。 -->",				# 0100100
		"<!-- 保护 。。 高赞 。。 。。 未三 。。 -->",				# 0100101
		"<!-- 。。 直播 高赞 。。 。。 未三 。。 -->",				# 0100110
		"<!-- 保护 直播 高赞 。。 。。 未三 。。 -->",				# 0100111
		"<!-- 。。 。。 。。 未一 。。 未三 。。 -->",				# 0101000
		"<!-- 保护 。。 。。 未一 。。 未三 。。 -->",				# 0101001
		"<!-- 。。 直播 。。 未一 。。 未三 。。 -->",				# 0101010
		"<!-- 保护 直播 。。 未一 。。 未三 。。 -->",				# 0101011
		"<!-- 。。 。。 高赞 未一 。。 未三 。。 -->",				# 0101100
		"<!-- 保护 。。 高赞 未一 。。 未三 。。 -->",				# 0101101
		"<!-- 。。 直播 高赞 未一 。。 未三 。。 -->",				# 0101110
		"<!-- 保护 直播 高赞 未一 。。 未三 。。 -->",				# 0101111
		"<!-- 。。 。。 。。 。。 未二 未三 。。 -->",				# 0110000
		"<!-- 保护 。。 。。 。。 未二 未三 。。 -->",				# 0110001
		"<!-- 。。 直播 。。 。。 未二 未三 。。 -->",				# 0110010
		"<!-- 保护 直播 。。 。。 未二 未三 。。 -->",				# 0110011
		"<!-- 。。 。。 高赞 。。 未二 未三 。。 -->",				# 0110100
		"<!-- 保护 。。 高赞 。。 未二 未三 。。 -->",				# 0110101
		"<!-- 。。 直播 高赞 。。 未二 未三 。。 -->",				# 0110110
		"<!-- 保护 直播 高赞 。。 未二 未三 。。 -->",				# 0110111
		"<!-- 。。 。。 。。 未一 未二 未三 。。 -->",				# 0111000
		"<!-- 保护 。。 。。 未一 未二 未三 。。 -->",				# 0111001
		"<!-- 。。 直播 。。 未一 未二 未三 。。 -->",				# 0111010
		"<!-- 保护 直播 。。 未一 未二 未三 。。 -->",				# 0111011
		"<!-- 。。 。。 高赞 未一 未二 未三 。。 -->",				# 0111100
		"<!-- 保护 。。 高赞 未一 未二 未三 。。 -->",				# 0111101
		"<!-- 。。 直播 高赞 未一 未二 未三 。。 -->",				# 0111110
		"<!-- 保护 直播 高赞 未一 未二 未三 。。 -->",				# 0111111
		"<!-- 。。 。。 。。 。。 。。 。。 未四 -->",				# 1000000
		"<!-- 保护 。。 。。 。。 。。 。。 未四 -->",				# 1000001
		"<!-- 。。 直播 。。 。。 。。 。。 未四 -->",				# 1000010
		"<!-- 保护 直播 。。 。。 。。 。。 未四 -->",				# 1000011
		"<!-- 。。 。。 高赞 。。 。。 。。 未四 -->",				# 1000100
		"<!-- 保护 。。 高赞 。。 。。 。。 未四 -->",				# 1000101
		"<!-- 。。 直播 高赞 。。 。。 。。 未四 -->",				# 1000110
		"<!-- 保护 直播 高赞 。。 。。 。。 未四 -->",				# 1000111
		"<!-- 。。 。。 。。 未一 。。 。。 未四 -->",				# 1001000
		"<!-- 保护 。。 。。 未一 。。 。。 未四 -->",				# 1001001
		"<!-- 。。 直播 。。 未一 。。 。。 未四 -->",				# 1001010
		"<!-- 保护 直播 。。 未一 。。 。。 未四 -->",				# 1001011
		"<!-- 。。 。。 高赞 未一 。。 。。 未四 -->",				# 1001100
		"<!-- 保护 。。 高赞 未一 。。 。。 未四 -->",				# 1001101
		"<!-- 。。 直播 高赞 未一 。。 。。 未四 -->",				# 1001110
		"<!-- 保护 直播 高赞 未一 。。 。。 未四 -->",				# 1001111
		"<!-- 。。 。。 。。 。。 未二 。。 未四 -->",				# 1010000
		"<!-- 保护 。。 。。 。。 未二 。。 未四 -->",				# 1010001
		"<!-- 。。 直播 。。 。。 未二 。。 未四 -->",				# 1010010
		"<!-- 保护 直播 。。 。。 未二 。。 未四 -->",				# 1010011
		"<!-- 。。 。。 高赞 。。 未二 。。 未四 -->",				# 1010100
		"<!-- 保护 。。 高赞 。。 未二 。。 未四 -->",				# 1010101
		"<!-- 。。 直播 高赞 。。 未二 。。 未四 -->",				# 1010110
		"<!-- 保护 直播 高赞 。。 未二 。。 未四 -->",				# 1010111
		"<!-- 。。 。。 。。 未一 未二 。。 未四 -->",				# 1011000
		"<!-- 保护 。。 。。 未一 未二 。。 未四 -->",				# 1011001
		"<!-- 。。 直播 。。 未一 未二 。。 未四 -->",				# 1011010
		"<!-- 保护 直播 。。 未一 未二 。。 未四 -->",				# 1011011
		"<!-- 。。 。。 高赞 未一 未二 。。 未四 -->",				# 1011100
		"<!-- 保护 。。 高赞 未一 未二 。。 未四 -->",				# 1011101
		"<!-- 。。 直播 高赞 未一 未二 。。 未四 -->",				# 1011110
		"<!-- 保护 直播 高赞 未一 未二 。。 未四 -->",				# 1011111
		"<!-- 。。 。。 。。 。。 。。 未三 未四 -->",				# 1100000
		"<!-- 保护 。。 。。 。。 。。 未三 未四 -->",				# 1100001
		"<!-- 。。 直播 。。 。。 。。 未三 未四 -->",				# 1100010
		"<!-- 保护 直播 。。 。。 。。 未三 未四 -->",				# 1100011
		"<!-- 。。 。。 高赞 。。 。。 未三 未四 -->",				# 1100100
		"<!-- 保护 。。 高赞 。。 。。 未三 未四 -->",				# 1100101
		"<!-- 。。 直播 高赞 。。 。。 未三 未四 -->",				# 1100110
		"<!-- 保护 直播 高赞 。。 。。 未三 未四 -->",				# 1100111
		"<!-- 。。 。。 。。 未一 。。 未三 未四 -->",				# 1101000
		"<!-- 保护 。。 。。 未一 。。 未三 未四 -->",				# 1101001
		"<!-- 。。 直播 。。 未一 。。 未三 未四 -->",				# 1101010
		"<!-- 保护 直播 。。 未一 。。 未三 未四 -->",				# 1101011
		"<!-- 。。 。。 高赞 未一 。。 未三 未四 -->",				# 1101100
		"<!-- 保护 。。 高赞 未一 。。 未三 未四 -->",				# 1101101
		"<!-- 。。 直播 高赞 未一 。。 未三 未四 -->",				# 1101110
		"<!-- 保护 直播 高赞 未一 。。 未三 未四 -->",				# 1101111
		"<!-- 。。 。。 。。 。。 未二 未三 未四 -->",				# 1110000
		"<!-- 保护 。。 。。 。。 未二 未三 未四 -->",				# 1110001
		"<!-- 。。 直播 。。 。。 未二 未三 未四 -->",				# 1110010
		"<!-- 保护 直播 。。 。。 未二 未三 未四 -->",				# 1110011
		"<!-- 。。 。。 高赞 。。 未二 未三 未四 -->",				# 1110100
		"<!-- 保护 。。 高赞 。。 未二 未三 未四 -->",				# 1110101
		"<!-- 。。 直播 高赞 。。 未二 未三 未四 -->",				# 1110110
		"<!-- 保护 直播 高赞 。。 未二 未三 未四 -->",				# 1110111
		"<!-- 。。 。。 。。 未一 未二 未三 未四 -->",				# 1111000
		"<!-- 保护 。。 。。 未一 未二 未三 未四 -->",				# 1111001
		"<!-- 。。 直播 。。 未一 未二 未三 未四 -->",				# 1111010
		"<!-- 保护 直播 。。 未一 未二 未三 未四 -->",				# 1111011
		"<!-- 。。 。。 高赞 未一 未二 未三 未四 -->",				# 1111100
		"<!-- 保护 。。 高赞 未一 未二 未三 未四 -->",				# 1111101
		"<!-- 。。 直播 高赞 未一 未二 未三 未四 -->",				# 1111110
		"<!-- 保护 直播 高赞 未一 未二 未三 未四 -->",				# 1111111
	]
	string_not_used_2 = ""
	string_not_used_3 = ""

	try: progress = Sub_Item["progress"]	# int32 progress = 2;
	except KeyError: progress = 0.0

	progress = format(progress/1000, ".5f")	# int32 progress = 2;
	mode = Sub_Item["mode"]					# int32 mode = 3;
	fontsize = Sub_Item["fontsize"]			# int32 fontsize = 4;

	try: color = Sub_Item["color"]			# uint32 color = 5;
	except KeyError: color = 0

	midHash = Sub_Item["midHash"]			# string midHash = 6;
	ctime = Sub_Item["ctime"]				# int64 ctime = 8;

	try: weight = Sub_Item["weight"]		# int32 weight = 9;
	except KeyError: weight = 11

	try: attr = Sub_Item["attr"]			# int32 attr = 13;
	except KeyError: attr = 0

	try: action = Sub_Item["action"]		# string action = 10;
	except KeyError: pass

	try: animation = Sub_Item["animation"]	# string animation = 22;
	except KeyError: pass

	try: idstr = Sub_Item["idstr"]			# string idStr = 12;
	except KeyError: idstr = "0" # ,print("\n idstr    ERROR", 1)

	try: id_ = Sub_Item["id"]				# int64 id = 1;
	except KeyError: pass

	# if id_ != idstr:print("\n id idstr mismatch:", id_, idstr)

	try: pool = Sub_Item["pool"]			# int32 pool = 11;
	except KeyError: pool = 0
	if pool == 2: content = content.replace("\n", "\\n").replace("\r\n", "\\n")

	XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}\n".format(progress, mode, fontsize, color, ctime, pool, midHash, id_, weight, content, string_attr[attr])
	XML_Data_2nd_Cache += XML_item
	if i % Split_SIZE == 0:
		XML_Data_1st_Cache += XML_Data_2nd_Cache
		XML_Data_2nd_Cache = ""
		print(f"\r进度：{i}/{danmu_count}，用时：{round(time.time()-Start_Time,4 )}",end="")

XML_Data_1st_Cache += XML_Data_2nd_Cache
XML_Data_1st_Cache += "</i>\n"
with open(outputFile, "w", encoding="utf-8")as Final_Write:
	Final_Write.write(XML_Data_1st_Cache)
	Final_Write.close()
End_Time = time.time()
print(f"\r总计用时：{round(End_Time-Start_Time, 6)}                   ")
