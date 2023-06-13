#!/usr/bin/python3
from google.protobuf.json_format import MessageToJson

import os
import json
import sys
import time

try: import zzzz as dm_pb2
except ModuleNotFoundError: import dm_pb2

from my_lib.file_writer import writeER

if __name__ == '__main__':
	tag_LiveRecording = False
	time1 = time.time()
	print("read")
	Danmaku_Binary = open(sys.argv[1], "rb").read()

	time2 = time.time()
	print("proto")
	Temp_Binary = dm_pb2.DmSegMobileReply()
	Temp_Binary.ParseFromString(Danmaku_Binary)

	if len(Temp_Binary.elems) == 0:
		print("No Data")
		sys.exit()
	time3 = time.time()
	print("json")
	j1 = json.loads(MessageToJson(Temp_Binary, indent=0))
	for this in Temp_Binary.elems:
		if this.attr == 2:
			tag_LiveRecording = True
			break
	for this in j1["elems"]:
		try:
			if this["test20"] == "0": del this["test20"]
		except KeyError: pass
		try:
			if this["test21"] == "0": del this["test21"]
		except KeyError: pass
		try:
			if this["attr"] == 2 and False:
				try: del this["likes"]
				except KeyError: pass
				try:
					if this["mode"] == 1: del this["mode"]
				except KeyError: pass
				try:
					if this["size"] == 25: del this["size"]
				except KeyError: pass
				try:
					if this["color"] == 16777215: del this["color"]
				except KeyError: pass
				try: del this["weight"]
				except KeyError: pass
		except KeyError: pass

	j1["commandDms"] = []
	j1["info"] = {}
	j1["info"]["Ver"] = "V6_20230601_P2J"
	j1["info"]["dmk_Ver"] = 4
	j1["info"]["owner"] = {"mid":0, "name":"Fake_Username", "face":"http://[::]/a.jpg"}
	j1["info"]["bvid"] = "Fake_BVID"
	j1["info"]["avid"] = 0
	j1["info"]["V_Name"] = "Fake_MainTitle"
	j1["info"]["pubdate"] = 0
	j1["info"]["ctime"] = 0
	j1["info"]["P_Name"] = "Fake_P_Title"
	j1["info"]["cid"] = 0
	j1["info"]["duration"] = 0
	j1["info"]["segment_count"] = 0
	j1["info"]["danmaku_count"] = len(j1["elems"])
	j1["info"]["danmaku_web_reported"] = 0
	j1["info"]["danmaku_proto_reported"] = 0
	j1["info"]["File_Create_Time"] = int(os.stat(sys.argv[1]).st_ctime)
	j1["info"]["File_Create_Time_Start"] = int(os.stat(sys.argv[1]).st_ctime)
	j1["info"]["is_live_record"] = tag_LiveRecording
	Write_Data = json.dumps(j1, ensure_ascii=False, separators=(',', ':'))

	Temp_Binary = None
	time4 = time.time()
	print("write")
	writeER(f"{sys.argv[1]}.json", Write_Data.replace("},{\"id\"", "},\x0a{\"id\"").replace(", \"test20\": \"0\", \"test21\": \"0\"", ""))
	# writeER(f"{sys.argv[1]}.json", Write_Data.replace("}, {\"id\"", "},\x0a{\"id\"").replace(", \"test20\": \"0\", \"test21\": \"0\"", ""), True)
	time5 = time.time()

	print(f"ALL:{time5-time1}, Write: {time5-time4}, Json: {time4-time3}, Proto: {time3-time2}, Read: {time2-time1}")
