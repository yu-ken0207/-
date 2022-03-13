from splinter.browser import Browser
from time import sleep
import traceback
class Buy_Tickets(object):
	# 定義例項屬性，初始化
	def __init__(self, username, passwd, order, passengers, dtime, starts, ends):
		self.username = username
		self.passwd = passwd
		# 車次，0代表所有車次，依次從上到下，1代表所有車次，依次類推
		self.order = order
		# 乘客名
		self.passengers = passengers
		# 起始地和終點
		self.starts = starts
		self.ends = ends
		# 日期
		self.dtime = dtime
		# self.xb = xb
		# self.pz = pz
		self.login_url = 'https://kyfw.12306.cn/otn/login/init'
		self.initMy_url = 'https://kyfw.12306.cn/otn/index/initMy12306'
		self.ticket_url = 'https://kyfw.12306.cn/otn/leftTicket/init'
		self.driver_name = 'chrome'
		self.executable_path = 'C:Python36Scriptschromedriver.exe'
	# 登入功能實現
	def login(self):
		self.driver.visit(self.login_url)
		self.driver.fill('loginUserDTO.user_name', self.username)
		# sleep(1)
		self.driver.fill('userDTO.password', self.passwd)
		# sleep(1)
		print('請輸入驗證碼...')
		while True:
			if self.driver.url != self.initMy_url:
				sleep(1)
			else:
				break
	# 買票功能實現
	def start_buy(self):
		self.driver = Browser(driver_name=self.driver_name, executable_path=self.executable_path)
		#視窗大小的操作
		self.driver.driver.set_window_size(700, 500)
		self.login()
		self.driver.visit(self.ticket_url)
		try:
			print('開始購票...')
			# 載入查詢資訊
			self.driver.cookies.add({"_jc_save_fromStation": self.starts})
			self.driver.cookies.add({"_jc_save_toStation": self.ends})
			self.driver.cookies.add({"_jc_save_fromDate": self.dtime})
			self.driver.reload()
			count = 0
			if self.order != 0:
				while self.driver.url == self.ticket_url:
					self.driver.find_by_text('查詢').click()
					count += 1
					print('第%d次點選查詢...' % count)
					try:
						self.driver.find_by_text('預訂')[self.order-1].click()
						sleep(1.5)
					except Exception as e:
						print(e)
						print('預訂失敗...')
						continue
			else:
				while self.driver.url == self.ticket_url:
					self.driver.find_by_text('查詢').click()
					count += 1
					print('第%d次點選查詢...' % count)
					try:
						for i in self.driver.find_by_text('預訂'):
							i.click()
							sleep(1)
					except Exception as e:
						print(e)
						print('預訂失敗...')
						continue
			print('開始預訂...')
			sleep(1)
			print('開始選擇使用者...')
			for p in self.passengers:
				self.driver.find_by_text(p).last.click()
				sleep(0.5)
				if p[-1] == ')':
					self.driver.find_by_id('dialog_xsertcj_ok').click()
			print('提交訂單...')
			# sleep(1)
			# self.driver.find_by_text(self.pz).click()
			# sleep(1)
			# self.driver.find_by_text(self.xb).click()
			# sleep(1)
			self.driver.find_by_id('submitOrder_id').click()
			sleep(2)
			print('確認選座...')
			self.driver.find_by_id('qr_submit_id').click()
			print('預訂成功...')
		except Exception as e:
			print(e)
if __name__ == '__main__':
	# 使用者名稱
	username = 'xxxx'
	# 密碼
	password = 'xxx'
	# 車次選擇，0代表所有車次
	order = 2
	# 乘客名，比如passengers = ['丁小紅', '丁小明']
	# 學生票需註明，註明方式為：passengers = ['丁小紅(學生)', '丁小明']
	passengers = ['丁彥軍']
	# 日期，格式為：'2018-01-20'
	dtime = '2018-01-19'
	# 出發地(需填寫cookie值)
	starts = '%u5434%u5821%2CWUY' #吳堡
	# 目的地(需填寫cookie值)
	ends = '%u897F%u5B89%2CXAY' #西安
	# xb =['硬座座'] 
	# pz=['成人票']

	Buy_Tickets(username, password, order, passengers, dtime, starts, ends).start_buy()
