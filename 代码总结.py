
# 设置绘图格式：
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(10, 6))
mpl.style.use('seaborn-whitegrid')


# 设置输出小数格式：
np.set_printoptions(precision=4)
pd.set_option('display.width', 450)

# 设置notebook的输出形式：以表格形式输出：
pandas.core.format.set_printoptions(notebook_repr_html=True)

# pandas
flst=pd.read_csv(fss, dtype=str,encoding='gbk')  
	"dtype = str 是因为有些股票代码为一位数字，这样000001这样的股票代码会被视为 1 ，在后面计算中会出现问题。"

df10=pd.read_csv(fss,index_col=0,parse_dates=[0]);
	'设置第一列为索引，并解析第一列为日期型格式。'

xd2.drop_duplicates(subset='index', keep='last', inplace=True);
	'以 index 列为基准去重，保留最后一项，并替代源文件'
	
close_px = pd.read_csv('ch09/stock_px.csv', parse_dates=True, index_col=0)
close_px.info() # 拿到数据首先应该要做的事情。

ds5 = ds2.rolling(center=False,window=n).mean() 
	'设置ds5为 n 日均线'
	rolling()即对Series有效，也对 DataFrame有效，仅仅是对数据的预格式化。就像groupby()一样
		In [12]: s.rolling(window=10)
		Out[12]: Rolling [window=10,center=False,axis=0]
	传入 'min_periods= n2（n2<n）'可以在 n 日之前，可以对 n2  rolling
		s.rolling(window=10, min_periods=5).mean()
		'这样，前5-9日分别是 6,7,8,9日均线'

if not qx.xbarWrk[qx.priceWrk].empty:
	# 注意这里的 empty 没有括号。
		
	## reset_index()：还原（多重）index为columns列
people = DataFrame(np.random.randn(5, 5),
                   columns=['a', 'b', 'c', 'd', 'e'],
                   index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
people['one'] = pd.Series(list('aabbb'),index=people.index)
people['a'] = pd.Series(list('cccdd'),index=people.index)

test2 = people.set_index(['a','one'])
print(test2)
test2_reset_index = test2.reset_index()
print(test2_reset_index)
	
	
# dateutil
from dateutil import rrule
from dateutil.parser import parse
rrule.rrule(rrule.DAILY,dtstart=qx.DTxtim0,until=parse(xtim)).count()
	'统计dtstart到until之间的相差天数，如果第一个参数是rrule.WEEKLY，则统计两者之间的周数。'
	'parse(xtim)表示解析xtim为datetime.datetime(2011, 1, 3, 0, 0)类型格式。'

	
# tushare
import tushare as ts
xd=ts.get_h_data(xcod,start=tim0,end=None,retry_count=5,pause=1)    
	'遇网络等问题重复执行 5 次，重复请求数据过程中暂停 1 秒数，防止请求间隔时间太短出现问题'
	


# numpy

	## np.take 与 np.random.permutation
def draw(deck, n=5):
    return deck.take(np.random.permutation(len(deck))[:n])
    # permutation(x):
    #   x 为int,返回 np.arange(x)的随机排列
    #   x 为array,返回 array的随机排列

	

# groupby 三个函数 agg,transform, apply 总结
1. aggregate（或agg）：
    - 传入单个函数: grouped[col1,col2].agg(func)
    - 传入函数组成的列表：grouped[col1,col2].agg([func1,func2])
    - 传入(name,func)组成的列表：grouped[col1,col2].agg([(name1,func1),(name2,func2)]):输出结果str(name1)代替str(func1)
    - 传入字典：grouped.agg({col1:[func1,func2],col2:fnc3}):对不同的列应用不同的函数**注意这里的 col的位置**
    - 对表9-1的内建函数函数func，必须传入函数名str(func)，否则被认为是自定义的函数
    - 对transform的第二种形式的函数不支持(因为它没有group效果)。
2. transform:
    - 传入的函数可以具有分组效果，如np.mean,那么结果是agg(np.mean)的展开。
    - 传入的函数也可以是有分组功能但是没有分组效果的，如 lambda x: x - x.mean 。返回的没有分组效果但有分组运算的DataFrame
3. apply:
    - apply(func),对func先分组运算，然后再叠加起来，因此对transform 的两种函数都支持。    
    - apply(func, *args, **kwargs),如apply(top, n=1, column='total_bill') 后面两个是 top 的参数
    - 传入 lambda x:{'min': x.min(), 'max': x.max(), 'count': x.count(), 'mean': x.mean()} 对每一组返回4行group数据

