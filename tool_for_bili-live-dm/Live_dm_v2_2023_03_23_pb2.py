# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Live_dm_v2_2023_03_23.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1bLive_dm_v2_2023_03_23.proto\x12$bilibiliDm.community.service.dm.live\"\x98\x08\n\x02\x44m\x12\x0e\n\x06id_str\x18\x01 \x01(\t\x12\x0c\n\x04mode\x18\x02 \x01(\x05\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\r\n\x05\x63olor\x18\x04 \x01(\r\x12\r\n\x05uhash\x18\x05 \x01(\t\x12\x0c\n\x04text\x18\x06 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x07 \x01(\x03\x12\x0e\n\x06weight\x18\x08 \x01(\x05\x12\x0b\n\x03rnd\x18\t \x01(\x03\x12\x0c\n\x04\x61ttr\x18\n \x01(\x03\x12\x41\n\tbiz_scene\x18\x0b \x01(\x0e\x32..bilibiliDm.community.service.dm.live.BizScene\x12<\n\x06\x62ubble\x18\x0c \x01(\x0b\x32,.bilibiliDm.community.service.dm.live.Bubble\x12=\n\x07\x64m_type\x18\r \x01(\x0e\x32,.bilibiliDm.community.service.dm.live.DmType\x12\x43\n\temoticons\x18\x0e \x03(\x0b\x32\x30.bilibiliDm.community.service.dm.live.emots_temp\x12:\n\x05voice\x18\x0f \x01(\x0b\x32+.bilibiliDm.community.service.dm.live.Voice\x12\x11\n\tanimation\x18\x10 \x01(\t\x12\x46\n\x0b\x61ggregation\x18\x11 \x01(\x0b\x32\x31.bilibiliDm.community.service.dm.live.Aggregation\x12\x14\n\x0csend_from_me\x18\x12 \x01(\x08\x12:\n\x05\x63heck\x18\x13 \x01(\x0b\x32+.bilibiliDm.community.service.dm.live.Check\x12\x38\n\x04user\x18\x14 \x01(\x0b\x32*.bilibiliDm.community.service.dm.live.User\x12\x38\n\x04room\x18\x15 \x01(\x0b\x32*.bilibiliDm.community.service.dm.live.Room\x12\x38\n\x04icon\x18\x16 \x01(\x0b\x32*.bilibiliDm.community.service.dm.live.Icon\x12:\n\x05reply\x18\x17 \x01(\x0b\x32+.bilibiliDm.community.service.dm.live.Reply\x12\x11\n\tunknown24\x18\x18 \x01(\x0c\x12\x11\n\tunknown25\x18\x19 \x01(\x0c\x12\x11\n\tunknown26\x18\x1a \x01(\x0c\x12\x11\n\tunknown27\x18\x1b \x01(\x0c\x12\x11\n\tunknown28\x18\x1c \x01(\x0c\x12\x11\n\tunknown29\x18\x1d \x01(\x0c\x12\x11\n\tunknown30\x18\x1e \x01(\x0c\x12\x11\n\tunknown31\x18\x1f \x01(\x0c\x12\x11\n\tunknown32\x18  \x01(\x0c\"\"\n\x05\x43heck\x12\r\n\x05token\x18\x01 \x01(\t\x12\n\n\x02ts\x18\x02 \x01(\x03\"1\n\x04Room\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0e\n\x06roomid\x18\x03 \x01(\r\"2\n\x06\x42ubble\x12\n\n\x02id\x18\x01 \x01(\x03\x12\r\n\x05\x63olor\x18\x02 \x01(\t\x12\r\n\x05id_v2\x18\x03 \x01(\x03\"X\n\nemots_temp\x12\x0b\n\x03key\x18\x01 \x01(\t\x12=\n\x05value\x18\x02 \x01(\x0b\x32..bilibiliDm.community.service.dm.live.Emoticon\"\x89\x01\n\x08\x45moticon\x12\x0e\n\x06unique\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x12\n\nis_dynamic\x18\x03 \x01(\x08\x12\x16\n\x0ein_player_area\x18\x04 \x01(\x03\x12\x15\n\rbulge_display\x18\x05 \x01(\x03\x12\x0e\n\x06height\x18\x06 \x01(\x03\x12\r\n\x05width\x18\x07 \x01(\x03\"_\n\x05Voice\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x13\n\x0b\x66ile_format\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x15\n\rfile_duration\x18\x04 \x01(\x03\x12\x0f\n\x07\x66ile_id\x18\x05 \x01(\t\"k\n\x0b\x41ggregation\x12\x16\n\x0eis_aggregation\x18\x01 \x01(\x08\x12\x17\n\x0f\x61\x63tivity_source\x18\x02 \x01(\x03\x12\x19\n\x11\x61\x63tivity_identity\x18\x03 \x01(\t\x12\x10\n\x08not_show\x18\x04 \x01(\x05\"\xa4\x04\n\x04User\x12\x0b\n\x03uid\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nname_color\x18\x03 \x01(\t\x12\x0c\n\x04\x66\x61\x63\x65\x18\x04 \x01(\t\x12\x0b\n\x03vip\x18\x05 \x01(\x03\x12\x0c\n\x04svip\x18\x06 \x01(\x03\x12\x0c\n\x04rank\x18\x07 \x01(\x05\x12\x15\n\rmobile_verify\x18\x08 \x01(\x05\x12\x12\n\nlpl_status\x18\t \x01(\x03\x12\x0c\n\x04\x61ttr\x18\n \x01(\x03\x12:\n\x05medal\x18\x0b \x01(\x0b\x32+.bilibiliDm.community.service.dm.live.Medal\x12>\n\x05level\x18\x0c \x01(\x0b\x32/.bilibiliDm.community.service.dm.live.UserLevel\x12:\n\x05title\x18\r \x01(\x0b\x32+.bilibiliDm.community.service.dm.live.Title\x12@\n\x08identify\x18\x0e \x01(\x0b\x32..bilibiliDm.community.service.dm.live.Identify\x12<\n\x06wealth\x18\x0f \x01(\x0b\x32,.bilibiliDm.community.service.dm.live.Wealth\x12\x45\n\x0bgroup_medal\x18\x10 \x01(\x0b\x32\x30.bilibiliDm.community.service.dm.live.GroupMedal\"J\n\x08Identify\x12\x15\n\rbeginning_url\x18\x01 \x01(\t\x12\x12\n\nending_url\x18\x02 \x01(\t\x12\x13\n\x0bjump_to_url\x18\x03 \x01(\t\"\xc7\x01\n\x05Medal\x12\r\n\x05level\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0f\n\x07special\x18\x03 \x01(\t\x12\r\n\x05\x63olor\x18\x04 \x01(\x03\x12\x0f\n\x07icon_id\x18\x05 \x01(\x03\x12\x14\n\x0c\x62order_color\x18\x06 \x01(\x03\x12\x1c\n\x14gradient_start_color\x18\x07 \x01(\x03\x12\x1a\n\x12gradient_end_color\x18\x08 \x01(\x03\x12\x11\n\tprivilege\x18\t \x01(\x03\x12\r\n\x05light\x18\n \x01(\x03\"L\n\tUserLevel\x12\r\n\x05level\x18\x01 \x01(\x03\x12\r\n\x05\x63olor\x18\x02 \x01(\x03\x12\x0c\n\x04rank\x18\x03 \x01(\t\x12\x13\n\x0bonline_rank\x18\x04 \x01(\x03\")\n\x05Title\x12\r\n\x05title\x18\x01 \x01(\t\x12\x11\n\told_title\x18\x02 \x01(\t\"+\n\x06Record\x12\x0c\n\x04\x64mid\x18\x01 \x01(\t\x12\x13\n\x0btime_offset\x18\x02 \x01(\x03\"\x17\n\x06Wealth\x12\r\n\x05level\x18\x01 \x01(\x03\"D\n\x04Icon\x12<\n\x06prefix\x18\x01 \x01(\x0b\x32,.bilibiliDm.community.service.dm.live.Prefix\"(\n\x06Prefix\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x10\n\x08resource\x18\x02 \x01(\t\"@\n\nGroupMedal\x12\x10\n\x08medal_id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nis_lighted\x18\x03 \x01(\x03\"^\n\x05Reply\x12\x12\n\nshow_reply\x18\x01 \x01(\x08\x12\x11\n\treply_mid\x18\x02 \x01(\x03\x12\x13\n\x0breply_uname\x18\x03 \x01(\t\x12\x19\n\x11reply_uname_color\x18\x04 \x01(\t*\x85\x01\n\x08\x42izScene\x12\x10\n\x0c\x42izSceneNone\x10\x00\x12\x13\n\x0f\x42izSceneLottery\x10\x01\x12\x13\n\x0f\x42izSceneSurvive\x10\x02\x12\x15\n\x11\x42izSceneVoiceConn\x10\x03\x12\x14\n\x10\x42izScenePlayBack\x10\x04\x12\x10\n\x0c\x42izSceneVote\x10\x05*?\n\x06\x44mType\x12\x10\n\x0c\x44mTypeNormal\x10\x00\x12\x12\n\x0e\x44mTypeEmoticon\x10\x01\x12\x0f\n\x0b\x44mTypeVoice\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Live_dm_v2_2023_03_23_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BIZSCENE']._serialized_start=2990
  _globals['_BIZSCENE']._serialized_end=3123
  _globals['_DMTYPE']._serialized_start=3125
  _globals['_DMTYPE']._serialized_end=3188
  _globals['_DM']._serialized_start=70
  _globals['_DM']._serialized_end=1118
  _globals['_CHECK']._serialized_start=1120
  _globals['_CHECK']._serialized_end=1154
  _globals['_ROOM']._serialized_start=1156
  _globals['_ROOM']._serialized_end=1205
  _globals['_BUBBLE']._serialized_start=1207
  _globals['_BUBBLE']._serialized_end=1257
  _globals['_EMOTS_TEMP']._serialized_start=1259
  _globals['_EMOTS_TEMP']._serialized_end=1347
  _globals['_EMOTICON']._serialized_start=1350
  _globals['_EMOTICON']._serialized_end=1487
  _globals['_VOICE']._serialized_start=1489
  _globals['_VOICE']._serialized_end=1584
  _globals['_AGGREGATION']._serialized_start=1586
  _globals['_AGGREGATION']._serialized_end=1693
  _globals['_USER']._serialized_start=1696
  _globals['_USER']._serialized_end=2244
  _globals['_IDENTIFY']._serialized_start=2246
  _globals['_IDENTIFY']._serialized_end=2320
  _globals['_MEDAL']._serialized_start=2323
  _globals['_MEDAL']._serialized_end=2522
  _globals['_USERLEVEL']._serialized_start=2524
  _globals['_USERLEVEL']._serialized_end=2600
  _globals['_TITLE']._serialized_start=2602
  _globals['_TITLE']._serialized_end=2643
  _globals['_RECORD']._serialized_start=2645
  _globals['_RECORD']._serialized_end=2688
  _globals['_WEALTH']._serialized_start=2690
  _globals['_WEALTH']._serialized_end=2713
  _globals['_ICON']._serialized_start=2715
  _globals['_ICON']._serialized_end=2783
  _globals['_PREFIX']._serialized_start=2785
  _globals['_PREFIX']._serialized_end=2825
  _globals['_GROUPMEDAL']._serialized_start=2827
  _globals['_GROUPMEDAL']._serialized_end=2891
  _globals['_REPLY']._serialized_start=2893
  _globals['_REPLY']._serialized_end=2987
# @@protoc_insertion_point(module_scope)
