from app.trainInfo import train
from flask import request
from flask_cors import CORS
from flask import jsonify
from trainData import getListData
import re
import json
import requests

CORS(train)

@train.route('/getTrainList', methods=['POST'])
def getlist():
    print(request.get_json())
    # print(request.form)
    departureStation = request.get_json()["departureStation"]  # 获取POST请求参数
    destinationStation = request.get_json()["destinationStation"]
    startDate = request.get_json()["startDate"]
    endDate = request.get_json()["endDate"]
    trainList = getListData.trainData(departureStation, destinationStation, startDate).gettrainInfo()
    resp = {
        "status": "ok",
        "trainList": trainList
    }
    return jsonify(resp)

@train.route('/getStationList', methods=['GET'])
def getStationList():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9095'
    response = requests.get(url, verify=False)
    cStations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
    stationListArr = []
    for t in cStations:
        stationList = dict()
        stationList["value"] = t[0]
        stationList["text"] = t[1]
        stationListArr.append(stationList)
    resp = {
        "status": "ok",
        "stationList": stationListArr
    }
    return jsonify(resp)

@train.route('/getTrainInfo', methods=['POST'])
def getTrainInfo():
    print(request.get_json())
    trainId = request.get_json()["trainId"]  # 获取POST请求参数
    startStation = request.get_json()["startStation"]
    endStation = request.get_json()["endStation"]
    date = request.get_json()["date"]

    url = 'https://kyfw.12306.cn/otn/czxx/queryByTrainNo'
    response = requests.get(url, params={'train_no': trainId,
                                          'from_station_telecode': startStation,
                                          'to_station_telecode': endStation,
                                          'depart_date': date
                                          }, verify=False)
    # print(response.text)
    respdata = json.loads(response.text)
    if (respdata["httpstatus"] == 200):
        resp = {
            "status": "ok",
            "trainInfoList": respdata["data"]
        }
        return jsonify(resp)

