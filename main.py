from apscheduler.schedulers.blocking import BlockingScheduler

#各大賣場爬蟲函式
from get_price import price_rtmart, price_savesafe, price_carrefour, price_feamart, price_wellcome
#資料寫入及整理函式
from file_data import file_save, file_clean

sched = BlockingScheduler({'apscheduler.timezone': 'Asia/Taipei'})
@sched.scheduled_job('interval', minutes=2)
def timed_job():
    print('每 2 分鐘執行一次程式工作區塊')

    row_list = []    
    #大潤發
    row_list += price_rtmart('可口可樂')
    #大買家
    row_list += price_savesafe('可口可樂')
    #家樂福
    row_list += price_carrefour('可口可樂')    
    #愛買
    row_list += price_feamart('可口可樂')    
    #頂好
    row_list += price_wellcome('可口可樂')
    #寫入價格資料
    file_save(row_list)
    #整理資料, 留下最新的
    file_clean()

sched.start()