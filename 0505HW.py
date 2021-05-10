class todo:

	def __init__(self, name, level, time, worker):
		self.name = name
		self.level = level
		self.time = time
		self.worker = worker 

	def info(self):
		print(f'할일 :  {self.name}')
		print(f'난이도 : {self.level}')
		print(f'걸리는 시간 : {self.time}')
		print(f'일할사람 : {self.worker}')
		print()

	def assigned(self, worker_num):
		print(f"{self.name} 배정 : {self.worker[worker_num]}")

task1 = todo("물품정리", "easy", 2, ['jack', 'tom'])
task2 = todo("재고분류", "hard", 4, ['jack', 'rosie', 'tom'])
task3 = todo("상품출고", "normal", 2, ['jack', 'rosie'])
task4 = todo("문의종합", "easy", 1, ['rosie', 'tom'])
task5 = todo("포장점검", "normal", 2, ['jack', 'rosie', 'tom'])

task1.info()
task2.info()
task3.info()
task4.info()
task5.info()

task1.assigned(1)
task2.assigned(2)
task3.assigned(1)
task4.assigned(0)
task5.assigned(0)
