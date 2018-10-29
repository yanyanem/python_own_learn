

1. 采用 自然语言收集.xls 进行 X, Y 的训练集合模拟。

2. 用 jieba 进行单词分割

3. 用 CountVectorizer 形成向量集

4. 用 classifier 进行训练

5. 在进行模拟验证

遇到的问题：

1. 从xls生成csv文件的时候，需要将文件生成 TAB 分割的文件，因为xls 中的语句中有逗号。 

2. 采用 python csv 模块进行读取分割。 

3. 在从二维数组的转换上，发现必须采用 X0=[x[1] for x in dataCsv[1:] ] 的方式将数组的列获取出来。

4. CountVectorizer 中开始的时候不能支持中文很好fit_transformer 

   参考了 http://blog.csdn.net/tiffany_li2015/article/details/50236833 后将 
   
   即把analyzer参数中原来的word改为(lambda s: s.split())

