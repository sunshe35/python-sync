
# ���û�ͼ��ʽ��
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rc('figure', figsize=(10, 6))
mpl.style.use('seaborn-whitegrid')


# �������С����ʽ��
np.set_printoptions(precision=4)
pd.set_option('display.width', 450)

# ����notebook�������ʽ���Ա����ʽ�����
pandas.core.format.set_printoptions(notebook_repr_html=True)

# pandas
flst=pd.read_csv(fss, dtype=str,encoding='gbk')  
	"dtype = str ����Ϊ��Щ��Ʊ����Ϊһλ���֣�����000001�����Ĺ�Ʊ����ᱻ��Ϊ 1 ���ں�������л�������⡣"

df10=pd.read_csv(fss,index_col=0,parse_dates=[0]);
	'���õ�һ��Ϊ��������������һ��Ϊ�����͸�ʽ��'

xd2.drop_duplicates(subset='index', keep='last', inplace=True);
	'�� index ��Ϊ��׼ȥ�أ��������һ������Դ�ļ�'
	
close_px = pd.read_csv('ch09/stock_px.csv', parse_dates=True, index_col=0)
close_px.info() # �õ���������Ӧ��Ҫ�������顣

ds5 = ds2.rolling(center=False,window=n).mean() 
	'����ds5Ϊ n �վ���'
	rolling()����Series��Ч��Ҳ�� DataFrame��Ч�������Ƕ����ݵ�Ԥ��ʽ��������groupby()һ��
		In [12]: s.rolling(window=10)
		Out[12]: Rolling [window=10,center=False,axis=0]
	���� 'min_periods= n2��n2<n��'������ n ��֮ǰ�����Զ� n2  rolling
		s.rolling(window=10, min_periods=5).mean()
		'������ǰ5-9�շֱ��� 6,7,8,9�վ���'

if not qx.xbarWrk[qx.priceWrk].empty:
	# ע������� empty û�����š�
		
	## reset_index()����ԭ�����أ�indexΪcolumns��
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
	'ͳ��dtstart��until֮�����������������һ��������rrule.WEEKLY����ͳ������֮���������'
	'parse(xtim)��ʾ����xtimΪdatetime.datetime(2011, 1, 3, 0, 0)���͸�ʽ��'

	
# tushare
import tushare as ts
xd=ts.get_h_data(xcod,start=tim0,end=None,retry_count=5,pause=1)    
	'������������ظ�ִ�� 5 �Σ��ظ��������ݹ�������ͣ 1 ��������ֹ������ʱ��̫�̳�������'
	


# numpy

	## np.take �� np.random.permutation
def draw(deck, n=5):
    return deck.take(np.random.permutation(len(deck))[:n])
    # permutation(x):
    #   x Ϊint,���� np.arange(x)���������
    #   x Ϊarray,���� array���������

	

# groupby �������� agg,transform, apply �ܽ�
1. aggregate����agg����
    - ���뵥������: grouped[col1,col2].agg(func)
    - ���뺯����ɵ��б�grouped[col1,col2].agg([func1,func2])
    - ����(name,func)��ɵ��б�grouped[col1,col2].agg([(name1,func1),(name2,func2)]):������str(name1)����str(func1)
    - �����ֵ䣺grouped.agg({col1:[func1,func2],col2:fnc3}):�Բ�ͬ����Ӧ�ò�ͬ�ĺ���**ע������� col��λ��**
    - �Ա�9-1���ڽ���������func�����봫�뺯����str(func)��������Ϊ���Զ���ĺ���
    - ��transform�ĵڶ�����ʽ�ĺ�����֧��(��Ϊ��û��groupЧ��)��
2. transform:
    - ����ĺ������Ծ��з���Ч������np.mean,��ô�����agg(np.mean)��չ����
    - ����ĺ���Ҳ�������з��鹦�ܵ���û�з���Ч���ģ��� lambda x: x - x.mean �����ص�û�з���Ч�����з��������DataFrame
3. apply:
    - apply(func),��func�ȷ������㣬Ȼ���ٵ�����������˶�transform �����ֺ�����֧�֡�    
    - apply(func, *args, **kwargs),��apply(top, n=1, column='total_bill') ���������� top �Ĳ���
    - ���� lambda x:{'min': x.min(), 'max': x.max(), 'count': x.count(), 'mean': x.mean()} ��ÿһ�鷵��4��group����

