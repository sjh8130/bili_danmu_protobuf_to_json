#!/dev/null
from functools import lru_cache


@lru_cache
def DanmakuAttrType(attr: int):
    if attr == 0:
        return "DM "
    o = ""
    attr_map = {
        1: "[保护]",
        2: "[直播]",
        4: "[高赞]",
        8: "[03]",
        16: "[TODO_04]",
        32: "[05]",
        64: "[06]",
        128: "[07]",
        256: "[图片]",
        512: "[09]",
        1024: "[10]",
        2048: "[NFT]",
        4096: "[12]",
        8192: "[13]",
        16384: "[14]",
        32768: "[TODO_15]",
        65536: "[16]",
        131072: "[17]",
        262144: "[18]",
        524288: "[19]",
        1048576: "[20]",
        2097152: "[21]",
        4194304: "[22]",
        8388608: "[23]",
        16777216: "[24]",
        33554432: "[25]",
        67108864: "[26]",
        134217728: "[27]",
        268435456: "[28]",
        536870912: "[29]",
        1073741824: "[30]",
        2147483648: "[31]",
        4294967296: "[32]",
        8589934592: "[33]",
    }

    # 使用位运算和循环来检查每个属性
    for bit, label in attr_map.items():
        if attr & bit:  # 如果该位为1
            o += label

    return o
