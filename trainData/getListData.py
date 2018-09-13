import requests
import urllib3
from trainData.lib import cStationName
from trainData.lib import eStationName
import pprint
urllib3.disable_warnings()

class trainData() :
    def __init__(self, departureStation, destinationStation, date):
        self.departureStation = departureStation
        self.destinationStation = destinationStation
        self.date = date
    def gettrainInfo(self):
        from_station = cStationName.cityCode.get(self.departureStation)
        to_station = cStationName.cityCode.get(self.destinationStation)
        # print(from_station, to_station)
        dataUrl = 'https://kyfw.12306.cn/otn/leftTicket/queryA'
        r = requests.get(dataUrl, params={'leftTicketDTO.train_date': self.date,
                                          'leftTicketDTO.from_station': from_station,
                                          'leftTicketDTO.to_station': to_station,
                                          'purpose_codes': 'ADULT'
                                          }, verify=False)
        # print(r.json())
        resData = r.json()['data']

        trainData = resData['result']  # 火车所有信息
        # print(trainData)
        trainMap = resData['map']      # 火车车站信息
        trainListData = []
        for i in trainData:
            temp = i.split("|")
            tickect = dict()
            tickect['trainState'] = temp[1]                                       # 火车状态
            tickect['trainId'] = temp[2]                                          # 火车编号
            tickect['trainNum'] = temp[3]                                         # 火车车次
            tickect['startStation'] = temp[4]                                     # 火车始发车站
            tickect['endStation'] = temp[5]                                       # 火车终点车站
            tickect['departureStation'] = trainMap[temp[6]]                       # 出发车站
            tickect['destinationStation'] = trainMap[temp[7]]                     # 目的车站
            tickect['sTime'] = temp[8]                                            # 出发时间
            tickect['eTime'] = temp[9]                                            # 到达时间
            tickect['tTime'] = temp[10]                                           # 耗时时间
            tickect['date'] = temp[13]                                            # 出发日期
            tickect['endSequence'] = temp[16]                                     # 出发车序
            tickect['startSequence'] = temp[17]                                   # 到达车序
            tickect['seniorSoftBerth'] = temp[22]                                 # 高级软卧
            tickect['softBerth'] = temp[23]                                       # 软卧
            tickect['softSeats'] = temp[24]                                       # 软座
            tickect['noSeat'] = temp[26]                                          # 无座
            tickect['hardBerth'] = temp[28]                                       # 硬卧
            tickect['hardSeats'] = temp[29]                                       # 硬座
            tickect['secondSeat'] = temp[30]                                      # 二等座
            tickect['firstSeat'] = temp[31]                                       # 一等座
            tickect['specialSeat'] = temp[32]                                     # 商务座 / 特等座
            tickect['moveBerth'] = temp[33]                                       # 动卧
            tickect['seatType '] = temp[35]                                       #类型
            trainListData.append(tickect)
        # print(trainListData)
        # pprint.pprint(trainListData, indent=4)
        return trainListData

