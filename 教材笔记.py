
## zwQT source文件夹下主要有以下模块：
 zwBacktest.py， zw 量化分析： 回溯测试工具函数，
 zwQTBox.py， zw 常用“量化”工具函数集
 zwQTDraw.py， zw 量化分析： 绘图工具函数
 zwStrategy.py， zw 量化分析： 策略工具函数
 zwSys.py， zw 量化初始化和系统模块，主要定义基础数据类、全局路径、全局变量等
 zwTools.py， zw 常用（非量化）工具函数集
 zw_talib.py， zw 版的 talib 函数封装，主要基于 pandas 进行移植 zwBacktest.py
为简化架构，除 zwSys.py 系统模块，因为全局数据变量需要，定义了三个基本类 class，以及少量类函数。其他模块，都是采用统一的函数定义， 整体设计，逻辑清晰， 便于用户修改，扩展。
zwQT 日后的升级版本，为统一起见，可能会将有关的类函数，改为工具函数。

## zwQuant 最常用的三个模块是：
zwSys.py， zw 量化初始化和系统模块，主要定义基础数据类、全局路径、全局变量等
zwTools.py， zw 常用（非量化）工具函数集
zwQTBox.py， zw 常用“量化”工具函数集

## zwQuant 常用缩写
import zwSys as zw
import zwTools as zwt
import zwQTBox as zwx
import zwQTDraw as zwdr
import zwBacktest as zwbt
import zwStrategy as zwsta
import zw_talib as zwta


# zwsys.py：zwSys 是 zw 量化初始化和系统模块，主要定义基础数据类、全局路径、全局变量等。
------变量
stkLib={} #全局变量，相关股票的交易数据，内存股票数据库
stkLibCode=[] #全局变量，相关股票的交易代码，内存股票数据库

------zwSys 定义了三个类 class： zwXBar、 zwDatX， zwQuantX。
class zwXBar 为数据包类， 'Bar' 是量化交易的传统数据单位，记录每笔交易；
	def prXBar，类函数，输出当前 Bar变量的数据。
class zwDatX，设置各个数据目录；类函数 
	def prDat,输出其他相关的目录信息。
class zwQuantX，定义了 zwQuant 量化交易所需的各种变量参数，以及相关的类函数
	def qxTimSet，设置时间参数
	def qxTim0SetVar(self, xtim)，回溯测试时间点开始，初始化相关参数
		'略'
	def qxTim9SetVar(self,xtim)，回溯测试时间点结束，整理相关数据
		self.qxUsr['date']=xtim
		zwx.xusrUpdate(self)
		self.qxLib = self.qxLib.append(self.qxUsr.T,ignore_index=True)
	def qxIDSet，生成订单流水号编码 ID
	def prQxUsr，输出用户变量保存的数据
		print('\n::qxUsr');
        dss=zwt.xobj2str(self.qxUsr,qxLibName);
        print(dss,'\n')
	def prQLibr，输出各种回溯交易测试数据，一般用于结束时
		print('')
        self.prQxUsr();
        print('::qxUsr.stk',self.prjName)
        print(self.qxUsrStk)
        print('::xtrdLib',self.fn_xtrdLib)
        #print(self.xtrdLib.tail())
        print(self.xtrdLib)
        print('')
        print('::qxLib.head',self.fn_qxLib)
        #print(self.qxUsr);
        print(self.qxLib.head())
        print('')
        print('::qxLib.tail')
        print(self.qxLib.tail())
        print('')
	
	# zwQuantX 类，还定义了一组类似的变量：(相对于zwSys的变量)
	self.qxLib=pd.DataFrame(columns=qxLibName,index=['date']); #所有交易记录清单列表
	self.xtrdLib=pd.DataFrame(columns=xtrdName,index=['date']); #所有 xBars 股票交易记录清单列表 
	self.qxUsr=pd.Series(index=qxLibName) #用户资产数据
	self.qxUsrStk={}; #用户持有的股票资产数据
	------以上， 用于保存相关的交易记录、回溯分析数据，都是按时间逐一保存的。
	
	------"zwQuant 量化分析系统，是精简版的量化分析、回溯测试系统，面向的是单用户、单任务模式， 因此可以采用这种简单的设计模式。如果是多个用户， 或者单用户， 需要进行多种测试， 例如： 沪深 300、 上证 50 等等。可以提供设置不同的 zwQuantX 类变量， 设置不同的参数， 运行完一个任务，再运行第二个任务即可。"
	
	
	qxLibName=['date','stkVal','cash','dret','val','downLow','downHigh','downDay','downKMax'];
		date， 交易时间， 采用 date，是为了和股票数据源保持统一，使用 tick、 1 分钟、 5 分钟等分时数据时， 请注意，此处的 date 表示时间列，不仅仅支持日期，也支持分钟、毫秒等分时数据
		stkVal，当前时间点，用户手中持有的所有股票的市场价值
	 	cach，当前时间点，用户手中持有的现金数额
	 	downLow，到当前时间点为止， 用户资产的最低价值水位
	 	downHigh，到当前时间点为止， 用户资产的最高价值水位
	 	downDay, 到当前时间点为止， 用户回缩的最长时间，
	 	downKMax，到当前时间点为止， 用户的最大回缩率
	 	dret， 单位回报率， 如果 time 是日，就是“日 回报率”
	 	val， 当前时间点，用户的全部资产价值
	'需要注意， zwQuant 类变量 qxUsr，采用的数据格式，也是 qxLibName。实际上， qxUsr 是单个时间点，用户的资产数据， qxLib 是多个时间点用户数据的汇总表格。qxUsr还有一个衍生数据 qxUsrStk，表示，当前用户持有的所有股票数目，采用的是字典格式，每个股票对应一个数值。'
	
	------xtrdLib 是所有交易的记录列表，单个记录，表示单一个股票交易订单的情况。
	xtrdName=['date','ID','mode','code','dprice','num','kprice','sum','cash'];
		date， 交易时间， 支持分钟、毫秒等分时数据
		ID，用户交易订单 ID 编号
		mode，订单模式。 buy：买入； sell，卖出
		code，股票代码
		num，交易的股票数量
		dprice，当前股票，策略分析采用的价格
		kprice，当前股票，实际交易采用的价格
		sum，当前股票，实际交易采用的总价格
		cash，当前交易完毕，用户实际持有的现金数目
		
	# 价格体系
	------在 zwQuant 类当中，定义了多种价格变量，用来设置各种环境的价格模式：
	priceWrk，策略分析时，使用的股票价格，一般是： dprice，复权开盘价
	priceBuy，买入/卖出的股票价格，一般是： kprice，一般采用次日的复权开盘价
	priceCalc，最后结算使用的股票价格，一般是： adj close，复权收盘价
	qxKPriceName=['open','high','low','close','adj close','dprice','kprice']
		self.priceWrk='dprice';
		self.priceBuy='kdprice';
		self.priceCalc='adj close';
	
	# 其他变量
	self.periodNDay=rrule.rrule(rrule.DAILY,dtstart=self.DTxtim0,until=self.DTxtim9).count()	
	self.dvix_k0=80     # dvix波动率下限
    self.dvix_k9=120  	# dvix 波动率上限
	self.trdNilFlag=False;  #空头交易标志


	
# zwTools 常用（非量化）工具函数
def iff2(kflag,x1,x0):二选一函数，如果 kflag 为 True，返回值是 x1；否则，返回值是 x0；
	'略'
def iff3(v,k,xn1,x0,x1): 三选一函数，如果 v<k，返回值是 xn1； v=k，返回值是 x0； v>k，返回值是 x1；
	'略'
def listPr(lst):输出列表信息
def listRd(fnam):读取列表数据
def listWr(fnam,lst):保存列表数据
def lst4dir(rss):目录文件生成列表数据
def wait(n,mstr=''):等待 n 秒
def xdebug(xmod,mnam,fnam):输出调试信息
def xin(xk,k0sgn,k9sgn):如果 xk 位于(x0sgn, x9sgn)间，不含等于，返回 True；否则，返回值是 x0；
def xinEQ(d,k0,k9): 如果 d 位于(k0, k9)之间，包含等于，返回 True；否则，返回值是 False；
	'略'
def xobj2str(xobj,xnamLst):对象属性字符串，根据属性列表，生成字符串
	return ... + str( xnamLst[i] + xobj[(xnamLst[i])] ) + ...

# zwQTBox.py
def cross_Mod(qx,ksma):均线交叉策略，判断均线向上、向下趋势
	 kmod=-9;
	if  (dp>dma)and(dp2n<ma2n)and(dp>dp2n):
		'dp>dma:现在现价 dprice 大于均线 ma_n;'	
		'dp2n<ma2n:2日前现价 dprice_shift(2) 小于均价 ma_n'
		'dp>dp2n:现在价格 dprice 大于2日前价格 dprice_shift(2)'
        kmod=1;
	elif (dp<dma)and(dp2n>ma2n)and(dp<dp2n):
        kmod=-1;
    return kmod  
def df2cnstk(df0):股票数据格式转换，转换为中国 A 股格式
def df2yhaoo(df0):股票数据格式转换，转换为 Yahoo 格式
def df2zw(df0):股票数据格式转换，转换为 zw 格式
def df2zwAdj(df0):股票数据格式转换，转换为 zw 增强版格式，带 adj close
	'大写--->小写,并设置 adj close '
def downKMax(dlow,dhigh):计算最大回缩率
def down_stk_cn010(qx,xtyp="D"):中国 A 股数据下载子程序(对单只股票操作)
	'下载全部或最近三年数据，然后append + drop_duplicates'
def down_stk_yahoo010(qx,ftg):yahoo 美股数据下载子程序
def qxObjSet(xtim,stkVal,dcash,dret):设置 xtrdLib 单次交易节点数据
	
def sharpe_rate(rets,rfRate,ntim=252):计算夏普指数
	'''
	rets (list): 收益率数组（根据ntim，按日、小时、保存）
    rfRate (int): 无风险收益利润
    ntim (int): 交易时间（按天、小时、等计数）
         采用小时(60分钟)线数据，ntim= 252* 6.5 = 1638.
	
	'''
	return rsharp
def stkGetPrice(qx,ksgn):获取当前价格
	'优先获取 ksgn 的价格，如果ksgn 的价格为空，那么就获取 dprice 的价格'
def stkGetPrice9x(qx,ksgn):获取首个、末个交易日数据
	'略'
def stkGetVars(qx,ksgn): return dval   获取股票代码，指定字段的数据
	d01 = zw.stklib[qx.stkCode][qx.xtim:qx.xtim] # qx.stkCode 之前已经初始化为单一股票
	if len(d01)>0:
		dval = d01[ksgn][0]
def stkInxLibRd(qx):读取指定的大盘数据到zw.stkInxLib
def stkInxLibSet8XTim(qx,dtim0,dtim9):根据时间段，切割大盘指数数据 zw.stkInxLib
def stkLibGetTimX(xcod):返回指定股票代码首个、末个交易日时间数据
def stkLibName8Code(xcod):根据股票代码，返回股票中文、英文/拼音缩写名称
def stkLibPr():输出股票数据
def stkLibRd(xlst,rdir):读取指定的股票数据，可多只股票
	'如果xlst=['aeti','egan','glng','simo']，则读取 rdir 内对应的股票数据'
	'如果 xlst=['@dat\\inx_code.csv']，则读取 rdir 内 inx_code.csv里面的[code]列股票数据'
def stkLibSet8XTim(dtim0,dtim9):根据时间段，切割股票数据
def stkValCalc(qx,xdicts):计算 xdicts 内所有的股票总价值
	'略'
def stk_col_renLow(dat): 股票数据格式转换，转换小写列名称
def stk_copy_OHLC(dat0):复制股票 OHLC 数据
def xbarGet8Tim(xcod,xtim):根据指定股票代码。时间，获取数据包
def xbarGet8TimExt(xcod,xtim): 根据指定股票代码。时间，获取数据包及股票数据
	d10=zw.stkLib[xcod]
    d02=d10[xtim:xtim]
	return d02，d10 
def xbarPr(bars):输出数据包数据
def xusrStkNum(qx,xcod):返回用户持有的 xcod 股票数目
	'略'
def xusrUpdate(qx):更新用户数据
	设置：qx.qxUsr['date']，qx.qxUsr['stkVal']，qx.qxUsr['val'],qx.qxUsr['cash'],qx.qxUsr['dret'],qx.qxUsr['downHigh'],qx.qxUsr['downLow'],qx.qxUsr['KMax'],qx.qxUsr['downDay']
def xusr4xtrd(qx,b2):根据交易数据，更新用户数据 qxUsr
def xedit_zwXDat(df):编辑用户数据格式
def xtrdChkFlag(qx):检查是不是有效交易
	流程：qx.stkNum，>0，买入股票；<0，卖出股票；-1；卖出全部股票
	设置：xfg,True,有效交易；False，无效交易
	设置：qx.trdNilFlag，False，空头交易标志
	if kfg or qx.trdNilFlag:
        b2=xtrdObjSet(qx);	#设置交易节点
	return kfg,b2
def xtrdLibAdd(qx):添加交易到 xtrdLib
def xtrdObjSet(qx):设置交易节点数据
	b2=pd.Series(zw.xtrdNil,index=zw.xtrdName)
	设置b2['date'],b2['mode'],b2['dprice'],b2['kprice'],b2['sum'],b2['cash']
	return b2
def zwRetPr(qx):输出、计算回报率
	retAvg=np.mean(qx.qxLib['dret']);
    retStd=np.std(qx.qxLib['dret']);
    dsharp=sharpe_rate(qx.qxLib['dret'],qx.rfRate)
    dsharp0=sharpe_rate(qx.qxLib['dret'],0)
    dcash=qx.qxUsr['cash'];
    dstk=stkValCalc(qx,qx.qxUsrStk); 
    dval=dstk+dcash;
    dret9=(dval-qx.mbase)/qx.mbase	
	
	print('')
    print("最终资产价值 Final portfolio value: $%.2f" % dval)
    print("最终现金资产价值 Final cash portfolio value: $%.2f" % dcash)
    print("最终证券资产价值 Final stock portfolio value: $%.2f" % dstk)
    print("累计回报率 Cumulative returns: %.2f %%" % (dret9*100))
    print("平均日收益率 Average daily return: %.3f %%" %(retAvg*100))
    print("日收益率方差 Std. dev. daily return:%.4f " %(retStd))
    print('')
    print("夏普比率 Sharpe ratio: %.3f,（%.2f利率）" % (dsharp,qx.rfRate))    
    print("无风险利率 Risk Free Rate: %.2f" % (qx.rfRate))
    print("夏普比率 Sharpe ratio: %.3f,（0利率）" % (dsharp0))    
    print('')
    print("最大回撤率 Max. drawdown: %.4f %%" %(abs(qx.downKMax)))
    print("最长回撤时间 Longest drawdown duration:% d" %qx.downMaxDay);
    print("回撤时间(最高点位) Time High. drawdown: " ,qx.downHighTime)
    print("回撤最高点位 High. drawdown: %.3f" %qx.downHigh)
    print("回撤最低点位 Low. drawdown: %.3f" %qx.downLow)
    print('')
    print("时间周期 Date lenght: %d (Day)" %qx.periodNDay)
    print("时间周期（交易日） Date lenght(weekday): %d (Day)" %qx.wrkNDay)
    
    print("开始时间 Date begin: %s" %qx.xtim0)
    print("结束时间 Date lenght: %s" %qx.xtim9)
    print('')
    print("项目名称 Project name: %s" % qx.prjName)    
    print("策略名称 Strategy name: %s" % qx.staName)    
    print("股票代码列表 Stock list: ",zw.stkLibCode)    
    print("策略参数变量 staVars[]: ",qx.staVars)    
    print('')
def zwRetTradeCalc(qx):输出、计算交易数据
	计算总交易的，trdNum,sum9,numAdd,sumAdd,sumDec并输出：
	print('交易总次数：%d' %trdNum)
    print('交易总盈利：%.2f' %sum9)
    print('')
    print('盈利交易数：%d' %numAdd)
    print('盈利交易金额：%.2f' %sumAdd)
    print('亏损交易数：%d' %numDec)
    print('亏损交易金额：%.2f' %sumDec)
	qx.xtim=xtim9
	
	

# zwQTDraw.py 绘图模块
def dr_quant3x_init(qx,w,h):初始化绘图环境， w、 h 是图形大小尺寸
def dr_quant3x(qx,ktop2,kbot,kmidlst,midSgn0=''):绘制图形

zw 版 3x 三合一，回溯测试绘图函数
【输入】
qx，全局量化参数变量
ktop2， Top 顶部成交量股票代码
kbot， Bot 底部绘图列名称，一般是'val'，资产总价值；数据源为： qx.qxLib
kmidlst， Mid 中部绘图列名称列表，为符合表格
子列表元素 1，为股票代码 xcod，其他列名称，为格式为：
[[xcod1,nam1,nam2,...],[xcod2,nam1,nam2,...],[xcod3,nam1,nam2,...]]
注意， kmidlst 数据源为： stkLib[xcod]，包含预处理扩充的数据列
midSgn0，中部绘图区图标前缀
其中，“<xcod>”为特殊符号，表示对应的股票代码
【输出】
无


# zwBackTest 回溯测试工具函数
def bt_init(xlst,rdat,prjNam,money0=1000000): return qx 设置回溯测试参数 
	'xlst 股票代码列表''rdat 股票数据目录''prjNam 项目名称''money0 启动资金'
	'初始化启动资金：qx=zw.zwQuantX(prjNam,money0);'
	'设置各种价格模式：qx.priceCalc, qx.priceWrk, qx.priceBuy'
	'设置绘图 和 数据输出格式'
	'设置数据源目录等场所，读取股票数据'
		qx.rdat=rdat
		zwx.stkLibRd(xlst,rdat)
	'设置大盘指数'
	'读取股票数据 qx.qxTimSet(xtim0,xtim9)'
	
def zwBackTest100(qx):回溯测试只函数，单一股票，单一时间点的测试
	#----运行策略函数，进行策略分析
    qx.stkNum=qx.staFun(qx);
    if qx.stkNum!=0:
        #----检查，是不是有效交易
        xfg,qx.xtrdChk=zwx.xtrdChkFlag(qx)
        if xfg:
            #----如果是有效交易，加入交易列表
            zwx.xtrdLibAdd(qx)
        elif qx.trdNilFlag:
            zwx.xtrdLibNilAdd(qx)
def zwBackTest(qx):回溯测试主程序
	'增加数据源波动率参数：dvix '	'计算回溯时间周期，也可以在此，根据nday调整回溯周期长度。或者在qt_init数据初始化时，通过qx.qxTimSet(xtim0,xtim9)，设置回溯周期长度'
	'按时间循环，进行回溯测试'
	for tc in range(nday)
		'每个测试时间点，开始时，清除qx相关参数'
		'按设定的股票代码列表，循环进行回溯测试'
		for xcod in zw.stkLibCode:
			qx.stkCode=xcod
			qx.xbarWrk = qx.stkLib[xcod][xtim]
			qx.xdatWrk = qx.stkLib[xcod]
			if not qx.xbarWrk[qx.priceWrk].empty:
				dvixFlag=zwt.xinEQ(dvix,qx.dvix_k0,qx.dvix_k9)or(dvix==0)or(np.isnan(dvix)) 
					# np.isnan(dvix)是在考虑缺失值的情况，dvix==0 这个老大估计是搞错了。
				if dvixFlag:
                    xpriceFlag=True
                    # 调用回溯子程序，如果是有效交易，设置成功交易标志xtrdFlag
                    zwBackTest100(qx)
                else:
                    print('@dvix',xcod,xtim,dvix);
		'如果所有股票代码列表循环完毕，成功交易标志为真'
        '在当前测试时间点终止，设置有关交易参数'
		if xpriceFlag:
			qx.wrkNDay+=1
            qx.qxTim9SetVar(qx.xtim);
 
					
# zwStrategy 策略工具函数
'''
zw 量化策略分析函数，采用 1+1 模式，每个策略一组两个函数。
其中一个为策略数据初始化函数、一个为策略分析函数。
这种 1+1 策略函数组模式，是 zwQT 独创的，具有策略编写简单、逻辑清晰、运行效率极高。
用户可参考相关源码，自行编写、扩充策略函数库。
'''
def sta_dataPre0xtim(qx,xnam0):策略参数设置子函数，根据预设时间，裁剪数据源stkLib
	'设置策略名称为xname0'
	'设置默认无风险年收益rfRate'  	'切割数据源(股票+大盘)：切割范围来源于staVars的后两位，(staVars为策略参数变量列表，有三(四)个元素，后两位为起始时间、结束时间)'  
	'设置 qxUsr 用户变量，初始数据：qx.qxUsr=qxObjSet(qx.xtim0, 0, qx.money, 0)。'
	
def BBANDS_dataPre(qx,xnam0,ksgn0):布林带数据预处理函数
def BBANDS_sta(qx):布林带策略分析函数
def CMA_dataPre(qx,xnam0,ksgn0):均线交叉策略数据预处理函数
    'zwx.sta_dataPre0xtim(qx,xnam0);'
	'对每只股票依据 qx.staVars 添加均线,并添加 ma2n(ma_n滞后2日) ，dp2n(dprice滞后2日)'
	'若开启调试模式，则：print(d20.tail())；d20.to_csv(fss)'
def CMA_sta(qx):均线交叉策略分析函数
	kmod=zwx.cross_Mod(qx)
	if kmod = ...: stknum = ...
	return stknum
def SMA_dataPre(qx,xnam0,ksgn0):简单均线策略数据预处理函数
	'zwx.sta_dataPre0xtim(qx,xnam0)'
	'对每只股票依据 qx.staVars 添加均线'
	'若开启调试模式，则：print(d20.tail())；d20.to_csv(fss)'
def SMA_sta(qx):return stknum  简单均线策略分析函数
	'如果 dprice > ma_n(n 日均线) 并且 xmun（用户持有的股票数目）== 0， stknum = 100'
	'如果 dprice < ma_n 并且 xmun > 0 stknum = -1'
def VWAP_dataPre(qx,xnam0,ksgn0):vwap 数据预处理函数
def VWAP_sta(qx):vwap 成交量加权平均价策略分析函数

# zw_talib.py 金融函数模块
'''
zw_talib 是个独立开源项目，是基于 pandas 的 talib 函数封装 ，属于 zwQaunt（简称 zwQT， zw 量化）项目的衍生项目。
zw_talib 无需安装 zwQaunt，模块和 demo，均可独立运行
'''
------zwtalib 首批函数名称
 ACCDIST(df, n):集散指标(A/D)——Accumulation/Distribution,是由价格和成交量的变化而决定的
 ADX(df, n, n_ADX): #adx，中文全称：平均趋向指数， ADX 指数是反映趋向变动的程度，而不是方向
的本身;英文全称： Average Directional Index 或者 Average Directional Movement Index
 ATR(df, n): ATR,均幅指标（ Average True Ranger） ,取一定时间周期内的股价波动幅度的移动平均值，主要
用于研判买卖时机
 BBANDS(df, n):布林带.Bollinger Bands
 BBANDS_UpLow(df, n): zw 改进版的布林带 talib 函数
 CCI(df, n): CCI 顺势指标(Commodity Channel Index),CCI 指标，是由美国股市分析家唐纳德·蓝伯特（ Donald
Lambert）所创造的，是一种重点研判股价偏离度的股市分析工具。
 COPP(df, n):估波指标（ Coppock Curve） ,又称“估波曲线”，通过计算月度价格的变化速率的加权平均值
来测量市场的动量，属于长线指标。估波指标由 Edwin· Sedgwick· Coppock 于 1962 年提出，主要用于判
断牛市的到来。该指标用于研判大盘指数较为可靠，一般较少用于个股；再有，该指标只能产生买进讯号。
依估波指标买进股票后，应另外寻求其他指标来辅助卖出讯号。估波指标的周期参数一般设置为 11、 14，
加权平均参数为 10，也可以结合指标的平均线进行分析
 Chaikin(df):佳庆指标（ Chaikin Oscillator） ,是由马可·蔡金（ Marc Chaikin）提出的，聚散指标（ A/D）的
改良版本。
16
 DONCH(df, n):奇安通道指标,Donchian Channel,该指标是由 Richard Donchian 发明的，是有 3 条不同颜色的
曲线组成的，该指标用周期（一般都是 20）内的最高价和最低价来显示市场的波动性;当其通道窄时表示
市场波动较小，反之通道宽则表示市场波动比较大。
 EMA(df, n):指数平均数指标(Exponential Moving Average， EXPMA 或 EMA),指数平均数指标也叫 EXPMA
指标，它也是一种趋向类指标，其构造原理是仍然对价格收盘价进行算术平均，并根据计算结果来进行分
析，用于判断价格未来走势的变动趋势。
 EOM(df, n):简易波动指标(Ease of Movement Value)，又称 EMV 指标;它是由 RichardW． ArmJr．根据等量
图和压缩图的原理设计而成,目的是将价格与成交量的变化结合成一个波动指标来反映股价或指数的变动
状况。由于股价的变化和成交量的变化都可以引发该指标数值的变动,因此,EMV 实际上也是一个量价合成
指标。
 FORCE(df, n):劲道指数(Force Index);劲道指数是由亚历山大·埃尔德(Alexander Elder)博士设计的一种摆荡
指标，藉以衡量每个涨势中的多头劲道与每个跌势中的空头劲道。劲道指数结合三项主要的市场资讯：价
格变动的方向、它的幅度与成交量。它是由一个崭新而实用的角度，把成交量纳入交易决策中。
 KELCH(df, n):肯特纳通道（ Keltner Channel， KC） ,肯特纳通道（ KC）是一个移动平均通道，由叁条线组
合而成(上通道、中通道及下通道)。通道，一般情况下是以上通道线及下通道线的分界作为买卖的最大可
能性。若股价於边界出现不正常的波动，即表示买卖机会。
 KST(df, r1, r2, r3, r4, n1, n2, n3, n4): 确然指标（ KST）又称为完定指标，该指标参考长、中、短期的变速
率 ROC，以了解不同时间循环对市场的影响。该指标将数个周期的价格变动率函数作加权以及再平滑绘制
长短曲线，其特色在通过修正的价格变动组合来判断趋势，精准掌握转折买卖点。
 KST4(df, r1, r2, r3, r4, n1, n2, n3, n4): zw 修订版， KST 确然指标。
 	MA(df, n, ksgn='close'):移动平均线,Moving Average，即最常用的均线指标
		'对 df[ksgn] 求 n 日移动平均线，并添加到 df 中,返回 df'	
 MACD(df, n_fast, n_slow): #MACD 指标信号和 MACD 的区别, MACD Signal and MACD difference， MACD
是由一快及一慢指数移动平均（ EMA）之间的差计算出来。“快”指短时期的 EMA，而“慢”则指长时
期的 EMA，最常用的是 12 及 26 日 EMA。
 MFI(df, n): MFI,资金流量指标和比率,Money Flow Index and Ratio，资金流量指标又称为量相对强弱指标
（ Volume Relative Strength Index， VRSI）；根据成交量来计测市场供需关系和买卖力道。该指标是通过反
映股价变动的四个元素：上涨的天数、下跌的天数、成交量增加幅度、成交量减少幅度；来研判量能的趋
势，预测市场供求关系和买卖力道，属于量能反趋向指标。
 MOM(df, n):动量线，英文全名 MOmentum，简称 MOM。“动量”这一名词，市场上的解释相当广泛。以
Momentum 命名的指标，种类更是繁多。综合而言，动量可以视为一段期间内，股价涨跌变动的比率。
 MassI(df):梅斯线（ Mass Index），梅斯线是 Donald Dorsey 累积股价波幅宽度之后，所设计的震荡曲线。
本指标最主要的作用，在于寻找飙涨股或者极度弱势股的重要趋势反转点。 MASS 指标是所有区间震荡指
标中，风险系数最小的一个。
 OBV(df, n):能量潮指标（ On Balance Volume， OBV）， OBV 指标是葛兰维（ Joe Granville）于本世纪 60
年代提出的，并被广泛使用。股市技术分析的四大要素：价、量、时、空。 OBV 指标就是从“量”这个
要素作为突破口，来发现热门股票、分析股价运动趋势的一种技术指标。它是将股市的人气——成交量与
股价的关系数字化、直观化，以股市的成交量变化来衡量股市的推动力，从而研判股价的走势。关于成交
量方面的研究， OBV 能量潮指标是一种相当重要的分析指标之一。
 PPSR(df):支点，支撑线和阻力线.Pivot Points, Supports and Resistances； PIVOT 指标的观念很简单，不需要
计算任何东西，它纯粹只是一个分析反转点的方法而已。 PIVOT 意思是指“轴心”，轴心是用来确认反转
的基准，所以 PIVOT 指标其实就是找轴心的方法； PIVOT 指标，经常与布林带数据一起分析。
 ROC(df, n):变动率(Rate of change,ROC)， ROC 是由当天的股价与一定的天数之前的某一天股价比较，其变
动速度的大小,来反映股票市场变动的快慢程度。 ROC，也叫做变动速度指标、变动率指标或变化速率指标。
 RSI(df, n): RSI，相对强弱指标,Relative Strength Index，也称相对强弱指数、相对力度指数； RSI，是通过
比较一段时期内的平均收盘涨数和平均收盘跌数来分析市场买沽盘的意向和实力，从而作出未来市场的走
17
势。 RSI 通过特定时期内股价的变动情况计算市场买卖力量对比，来判断股票价格内部本质强弱、推测价
格未来的变动方向的技术指标。
 RSI100(df, n):zw 版 RSI 相对强弱指数，取 0..100 之间的数值
 STDDEV(df, n):标准偏差,Standard Deviation
 STOD(df, n):随机指标 D 值,Stochastic oscillator %D；随机指标，又称 KD 指标， KDJ 指标；随机指标综合
了动量观念、强弱指标及移动平均线的优点，用来度量股价脱离价格正常范围的变异程度。随机指标考虑
的不仅是收盘价，而且有近期的最高价和最低价，这避免了仅考虑收盘价而忽视真正波动幅度的弱点。随
机指标一般是根据统计学的原理，通过一个特定的周期（常为 9 日、 9 周等）内出现过的最高价、最低价，
及最后一个计算周期的收盘价及这三者之间的比例关系，来计算最后一个计算周期的未成熟随机值 RSV，
然后根据平滑移动平均线的方法来计算 K 值、 D 值与 J 值，并绘成曲线图来研判股票走势。
 STOK(df):随机指标 K 值,Stochastic oscillator %K
 TRIX(df, n):TRIX 指标又叫三重指数平滑移动平均指标， Triple Exponentially Smoothed Average
 TSI(df, r, s): TSI，真实强度指数,True Strength Index， TSI 是相对强弱指数 (RSI) 的变体。 TSI 使用价格动
量的双重平滑指数移动平均线，剔除价格的震荡变化并发现趋势的变化。 r 一般取 25，是一般取 13。
 ULTOSC(df): UOS，终极指标（ Ultimate Oscillator），终极指标，由拉瑞·威廉（ Larry Williams）所创。
他认为现行使用的各种振荡指标，对于周期参数的选择相当敏感。不同的市况，不同参数设定的振荡指标，
产生的结果截然不同。因此，选择最佳的参数组含，成为使用振荡指标之前，最重要的一道手续。为了将
参数周期调和至最佳状况，拉瑞·威廉经过不断测试的结果， 先找出三个周期不同的振荡指标，再将这些
周期参数，按照反比例的方式，制作成常数因子。然后，依照加权的方式，将三个周期不同的振荡指标，
分别乘以不同比例的常数，加以综合制作成 UOS 指标。经过一连串参数顺化的过程后， UOS 指标比一般
单一参数的振荡指标，更能够顺应各种不同的市况。
 Vortex(df, n):螺旋指标,Vortex Indicator，参见 http://www.vortexindicator.com/VFX_VORTEX.PDF

















