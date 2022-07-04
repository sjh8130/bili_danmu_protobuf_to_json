#!/usr/bin/python3
# 系统十分稳定，所有代码不要随便动.JPG
import math
import time
from google.protobuf.json_format import MessageToJson
import requests
import json
import dm_pb2
import sys
from tqdm import tqdm

flag_Timer = flag_Zero_Stop = flag_Many_Logs = flag_Ext_XML_Data = flag_NO_Json = flag_NO_XML = flag8 = flag9 = is_ERROR = False
flag_Error_Stop = True
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}
SLEEP_TIME = 0.7
BV_AV_table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
BV_AV_base58_dic = {}
for BV_AV_base58_i in range(58):
	BV_AV_base58_dic[BV_AV_table[BV_AV_base58_i]] = BV_AV_base58_i
s = [11, 10, 3, 8, 4, 6]
BV_AV_xor = 177451812
BV_AV_add = 8728348608


def Program_FLAG(flag: str):
	if flag.find("0b") == 0: b = flag
	else: b = bin(int(flag))
	b = "0000000000" + b.lstrip("0b")
	b = b.lstrip("0")
	if b[-1] == "1":
		global flag_Timer
		flag_Timer = True
	if b[-2] == "1":
		global flag_Error_Stop
		flag_Error_Stop = False
	if b[-3] == "1":
		global flag_Zero_Stop
		flag_Zero_Stop = True
	if b[-4] == "1":
		global flag_Many_Logs
		flag_Many_Logs = True
	if b[-5] == "1":
		global flag_Ext_XML_Data
		flag_Ext_XML_Data = True
	if b[-6] == "1":
		global flag_NO_Json
		flag_NO_Json = True
	if b[-7] == "1":
		global flag_NO_XML
		flag_NO_XML = True
	if b[-8] == "1":
		global flag8
		flag8 = True
	if b[-9] == "1":
		global flag9
		flag9 = True
	print(f"[FLAG]: {b}", end="\t")


def danmaku_ATTR_TYPE(attr: int):
	o = ""
	b = "0000000000" + bin(attr).lstrip("0b")
	if b[-1] == "1": o += "保护 "
	if b[-2] == "1": o += "直播 "
	if b[-3] == "1": o += "高赞 "
	if b[-4] == "1": o += "壹 "
	if b[-5] == "1": o += "贰 "
	if b[-6] == "1": o += "叁 "
	if b[-7] == "1": o += "肆 "
	if b[-8] == "1": o += "伍 "
	if b[-9] == "1": o += "陆 "
	if b[-10] == "1": o += "柒 "
	if o == "": return "<!-- DM -->"
	o = "<!-- " + o + "-->"
	return o


def BV_to_AV(input_BV: str):
	result = 0
	for i in range(6):
		result += BV_AV_base58_dic[input_BV[s[i]]]*58**i
	out = (result-BV_AV_add) ^ BV_AV_xor
	if out <= 0:
		print("[BV_to_AV]: invaild avid")
		global is_ERROR
		is_ERROR = True
	return out


def AV_to_BV(input_AV: int):
	if input_AV > 2147483647:
		global is_ERROR
		is_ERROR = True
		print("[AV_to_BV]: avid is too big")
	input_AV = (input_AV ^ BV_AV_xor)+BV_AV_add
	result = list('BV1  4 1 7  ')
	for i in range(6):
		result[s[i]] = BV_AV_table[input_AV//58**i % 58]
	return ''.join(result)


def downloader(url):
	if flag_Many_Logs: print(f"[NET]: {url}",end = "\t")
	time.sleep(SLEEP_TIME)
	contents = requests.get(url, headers=headers).content
	try:
		status_code = json.loads(contents)["code"]
		if status_code != 0:
			global is_ERROR
			is_ERROR = True
		if flag_Many_Logs or status_code != 0:
			print(f"[NET]: Error Code {status_code}")
	except UnicodeDecodeError: pass
	return contents


def get_danmaku(cid: str, segment_index: str):
	url = f'https://api.bilibili.com/x/v2/dm/web/seg.so?type=1&oid={cid}&segment_index={segment_index}'
	content = downloader(url)
	if is_ERROR and flag_Error_Stop:
		return b""
	return content


def get_BAS_danmaku(avid: str, cid: str):
	url_1 = f'https://api.bilibili.com/x/v2/dm/web/view?type=1&oid={cid}&pid={avid}'
	data_1 = downloader(url_1)
	if flag_Many_Logs: print(f"[BAS_DL]: Info")
	if is_ERROR and flag_Error_Stop: return b""
	data_2 = dm_pb2.DmWebViewReply()
	data_2.ParseFromString(data_1)
	try:
		data_3 = json.loads(MessageToJson(data_2))["specialDms"]
	except KeyError:
		return b""
	if len(data_3) == 0:
		return b""
	BAS_Binary = b""
	for i in data_3:
		data = downloader(i)
		if flag_Many_Logs: print(f"[BAS_DL]: DL", end="\t")
		if is_ERROR and flag_Error_Stop: break
		BAS_Binary += data
	return BAS_Binary


def XML_Process(data):
	jsonData = json.loads(data)
	XML_Data_2nd = ""
	danmu_count = len(jsonData["elems"])
	for i in range(danmu_count):
		Sub_Item = jsonData["elems"][i]

		try: content = Sub_Item["content"]		# string content = 7;
		except KeyError: content = ""
		content = content.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace("\u0008", "").replace("\u0017", "")

		try: progress = Sub_Item["progress"]  # int32 progress = 2;
		except KeyError: progress = 0
		progress = format(progress/1000, ".5f")

		mode = Sub_Item["mode"]					# int32 mode = 3;
		fontsize = Sub_Item["fontsize"]			# int32 fontsize = 4;

		try: color = Sub_Item["color"]			# uint32 color = 5;
		except KeyError: color = 0

		midHash = Sub_Item["midHash"]			# string midHash = 6;
		ctime = Sub_Item["ctime"]				# int64 ctime = 8;

		try: weight = Sub_Item["weight"]		# int32 weight = 9;
		except KeyError: weight = 11
		if flag_Ext_XML_Data:
			try: attr = Sub_Item["attr"]			# int32 attr = 13;
			except KeyError: attr = 0

			try: action = Sub_Item["action"]		# string action = 10;
			except KeyError: pass

			try: animation = Sub_Item["animation"]	# string animation = 22;
			except KeyError: pass
		else:
			attr = 0
			action = ""
			animation = ""

		try: id_ = Sub_Item["id"]				# int64 id = 1;
		except KeyError: id_ = "0"

		try: idStr = Sub_Item["idStr"]			# string idStr = 12;
		except KeyError:
			idStr = "0"
			if flag_Many_Logs:
				print(f"idStr ERROR: {id_}")

		if id_ != idStr:print("\n id&idStr mismatch:", id_, idStr)

		try: pool = Sub_Item["pool"]			# int32 pool = 11;
		except KeyError: pool = 0
		if pool == 2: content = content.replace("\n", "\\n").replace("\r\n", "\\n")

		XML_item = "\t<d p=\"{0},{1},{2},{3},{4},{5},{6},{7},{8}\">{9}</d>{10}\n".format(progress, mode, fontsize, color, ctime, pool, midHash, id_, weight, content, danmaku_ATTR_TYPE(attr))
		XML_Data_2nd += XML_item
	return XML_Data_2nd


if __name__ == '__main__':
	开始时间 = time.time()
	# print(sys.argv)
	# try:
	# 	vid = sys.argv[2]
	# 	Program_FLAG(sys.argv[1])
	# except ValueError:
	# 	flag_Timer = flag_Zero_Stop = flag_Many_Logs = flag_Ext_XML_Data = flag_NO_Json = flag_NO_XML = flag8 = flag9 = False
	# 	flag_Error_Stop = True
	# 	vid = sys.argv[1]
	# except IndexError:
	# 	flag_Timer = flag_Zero_Stop = flag_Many_Logs = flag_Ext_XML_Data = flag_NO_Json = flag_NO_XML = flag8 = flag9 = False
	# 	flag_Error_Stop = True
	# 	vid = sys.argv[1]
	# if flag_NO_Json and flag_NO_XML:
	# 	print("?????????")
	# 	sys.exit(999)
	flag_Timer = False
	flag_Zero_Stop = False
	flag_Many_Logs = True
	flag_Ext_XML_Data = False
	flag_NO_Json = False
	flag_NO_XML = False
	flag8 = False
	flag9 = False
	flag_Error_Stop = True
	vid = sys.argv[1]
	if vid.find("https://www.bilibili.com/video/") == 0: vid = vid.lstrip("https://www.bilibili.com/video/")
	elif vid.find("http://www.bilibili.com/video/") == 0: vid = vid.lstrip("http://www.bilibili.com/video/")
	elif vid.find("https://b23.tv/BV1") == 0: vid = vid.lstrip("https://b23.tv/")
	vid = vid.split("?")[0].split("/")[0]
	if vid.find("av") == 0:
		avid = vid
		avid_in = int(avid.lstrip("av"))
		bvid = AV_to_BV(avid_in)
	else:
		bvid = vid
		avid_in = BV_to_AV(bvid)
		avid = "av" + str(avid_in)
	url = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
	if flag_Many_Logs: print(f"[Info]: {bvid}")
	json_Resp = downloader(url)
	json_List = json.loads(json_Resp)

	if is_ERROR and flag_Error_Stop:
		print(f"[{bvid}|{avid}]Error: {json_List['data']}")
		print("总计用时:", time.time()-开始时间)
		sys.exit(1)

	json_Data = json_List["data"]
	sub_Items = json_Data["pages"]
	mainTitle = json_Data["title"]
	publish_D = str(json_Data["pubdate"])

	if mainTitle == "": mainTitle = "Fake_MainTitle"
	mainTitle_escape = mainTitle.replace("_", "＿").replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜")  # \/:*?"<>|
	sub_Items_Len = len(sub_Items)

	if json_Data["stat"]["danmaku"] == 0 and flag_Zero_Stop:
		print("No danmaku")
		for i in range(sub_Items_Len):
			duration = int(sub_Items[i]["duration"])
			cid = str(sub_Items[i]["cid"])
			P_Title = str(sub_Items[i]["part"])
			show_string = publish_D+"|{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, i+1, sub_Items_Len, cid, duration, math.ceil(duration/360), mainTitle, P_Title)
			print(show_string)
		print("总计用时:", time.time()-开始时间)
		sys.exit(1)

	for i in range(sub_Items_Len):
		if is_ERROR and flag_Error_Stop: break
		分P开始时间 = time.time()
		if not flag_NO_Json: Danmaku_Binary = b""
		if not flag_NO_Json: Temp_Binary = dm_pb2.DmSegMobileReply()
		duration = int(sub_Items[i]["duration"])
		segment_count = math.ceil(duration/360)
		cid = str(sub_Items[i]["cid"])
		if not flag_NO_XML: XML_Write_Data = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n"
		if not flag_NO_XML: XML_Data_Empty = f"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<i>\n\t<chatserver>chat.bilibili.com</chatserver>\n\t<chatid>{cid}</chatid>\n\t<mission>0</mission>\n\t<maxlimit>8000</maxlimit>\n\t<state>0</state>\n\t<real_name>0</real_name>\n\t<source>k-v</source>\n</i>\n"
		P_Title = str(sub_Items[i]["part"])
		if mainTitle == P_Title: P_Title = ""
		P_Title_escape = P_Title.replace("_", "＿").replace("\\", "＼").replace("/", "／").replace(":", "：").replace("*", "＊").replace("?", "？").replace("<", "＜").replace(">", "＞").replace("|", "｜")
		show_string = "{0}|{1}|P{2}/{3}|{4}|{5}|{6}|{7}|{8}".format(bvid, avid, i+1, sub_Items_Len, cid, duration, segment_count, mainTitle, P_Title)
		print(show_string)
		File_Name = f"[{publish_D}][{bvid}][{avid}][P{i+1}][{cid}]{mainTitle_escape}_{P_Title_escape}".rstrip("_") # [1656432000][BV1**4*1*7*][av*********][P*]MainTitle_P-Title [1656432000][BV1**4*1*7*][av*********][P*]MainTitle
		XML_Time = 0
		BAS开始时间 = time.time()
		BAS_danmaku = get_BAS_danmaku(avid=avid_in, cid=cid)
		if not flag_NO_XML:
			XML_T1 = time.time()
			xml_t1 = dm_pb2.DmSegMobileReply()
			xml_t1.ParseFromString(BAS_danmaku)
			xml_t2 = MessageToJson(xml_t1)
			if len(xml_t2) <= 3:
				if flag_Many_Logs:
					print(f"[BAS P{i+1}]:\tNo BAS Danmaku")
			else: XML_Write_Data += XML_Process(xml_t2)
			XML_T2 = time.time()
			XML_Time += XML_T2 - XML_T1
		if is_ERROR or flag_Many_Logs: print(f"[BAS]:\t{bvid}|{avid}|{cid}")
		if not flag_NO_Json: Danmaku_Binary += BAS_danmaku
		BAS结束时间 = time.time()
		if not flag_Many_Logs: Progress_Bar = tqdm(total=segment_count, leave=False, unit='chunks')
		for segments in range(segment_count):
			if is_ERROR and flag_Error_Stop: break
			Danmaku_sub_Items = get_danmaku(cid, str(segments+1))
			if is_ERROR or flag_Many_Logs: print(f"[danmaku]: P{i+1}/{sub_Items_Len}::{segments}/{segment_count}")
			if not flag_NO_Json: Danmaku_Binary += Danmaku_sub_Items
			if not flag_NO_XML:
				XML_T1 = time.time()
				xml_t1 = dm_pb2.DmSegMobileReply()
				xml_t1.ParseFromString(Danmaku_sub_Items)
				XML_Write_Data += XML_Process(MessageToJson(xml_t1))
				XML_T2 = time.time()
				XML_Time += XML_T2 - XML_T1
			if not flag_Many_Logs:Progress_Bar.update(1)
		if not flag_Many_Logs:Progress_Bar.close()

		写入开始时间 = time.time()
		if not flag_NO_Json: Temp_Binary.ParseFromString(Danmaku_Binary)
		if not flag_NO_Json:
			with open(File_Name+".json", "w", encoding="utf-8") as f:
				if is_ERROR or flag_Many_Logs: print(f"[File_JSON P{i+1}]: 开始写入")
				Json_Write_Data = json.dumps(json.loads(MessageToJson(Temp_Binary)), ensure_ascii=False)
				if Json_Write_Data == "{}": continue
				else: f.write(Json_Write_Data)
		if not flag_NO_XML:
			with open(File_Name+".xml", "w", encoding="utf-8") as x:
				XML_Write_Data += "</i>\n"
				if is_ERROR or flag_Many_Logs: print(f"[File_XML  P{i+1}]: 开始写入")
				if XML_Write_Data == XML_Data_Empty: continue
				else: x.write(XML_Write_Data)

		分P结束时间 = time.time()
		if is_ERROR or flag_Timer or flag_Many_Logs:
			print(f"分P {i+1}用时: {分P结束时间-分P开始时间}, BAS用时: {BAS结束时间-BAS开始时间}，写入用时: {分P结束时间-写入开始时间}，XML: {XML_Time}，RT:{分P结束时间-分P开始时间-segment_count*SLEEP_TIME}，Wait:{SLEEP_TIME*segment_count}")  

	if is_ERROR or flag_Timer or flag_Many_Logs:
		print(f"{bvid}|{avid} 总计用时: {time.time()-开始时间}")
	sys.exit(0)
