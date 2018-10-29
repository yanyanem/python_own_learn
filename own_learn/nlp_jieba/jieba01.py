# encoding=utf-8 
import jieba

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = jieba.cut("我来到北京清华大学", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

seg_list = jieba.cut("告诉我这个月的销售冠军是谁？", cut_all=False)
print("00-Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("这个月卖得最好的5样东西。", cut_all=False)
print("00-Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("上个Q的A0001和A0002的销量对比", cut_all=False)
print("00-Default Mode: " + "/ ".join(seg_list))  # 精确模式
