# -*- coding: utf-8 -*-
# version 2021.12.22
from flask import Flask, json, request
from flask_cors import CORS
import read as rd       #grab passthrough functions from main read file
import write as wr      #grab passthrough functions from main write file

#set-up Flask details
giv_api = Flask(__name__)
jsonResponseType = { 'Content-Type': 'application/json; charset=utf-8' }
CORS(giv_api)

#Proxy Read Functions

#Read from Inverter put in cache and publish
@giv_api.route('/runAll', methods=['GET'])
def getAll():
    return rd.runAll(True), 200, jsonResponseType

#Publish last cached Inverter Data
@giv_api.route('/readData', methods=['GET'])
def rdData():
    return rd.pubFromPickle(), 200, jsonResponseType

#Read from Inverter put in cache
@giv_api.route('/getData', methods=['GET'])
def gtData():
    return rd.getData(), 200, jsonResponseType

#Proxy Write Functions
@giv_api.route('/enableChargeTarget', methods=['POST'])
def enChargeTrgt():
    payload = request.get_json(silent=True, force=True)
    return wr.enableChargeTarget(payload), 200, jsonResponseType
    
@giv_api.route('/enableChargeSchedule', methods=['POST'])
def enableChrgSchedule():
    payload = request.get_json(silent=True, force=True)
    return wr.enableChargeSchedule(payload), 200, jsonResponseType

@giv_api.route('/enableDischargeSchedule', methods=['POST'])
def enableDischrgSchedule():
    payload = request.get_json(silent=True, force=True)
    return wr.enableDischargeSchedule(payload), 200, jsonResponseType

@giv_api.route('/enableDischarge', methods=['POST'])
def enableBatDisharge():
    payload = request.get_json(silent=True, force=True)
    return wr.enableDischarge(payload), 200, jsonResponseType

@giv_api.route('/setChargeTarget', methods=['POST'])
def setChrgTarget():
    payload = request.get_json(silent=True, force=True)
    return wr.setChargeTarget(payload), 200, jsonResponseType

@giv_api.route('/setBatteryReserve', methods=['POST'])
def setBattReserve():
    payload = request.get_json(silent=True, force=True)
    return wr.setBatteryReserve(payload), 200, jsonResponseType

@giv_api.route('/setChargeRate', methods=['POST'])
def setChrgeRate():
    payload = request.get_json(silent=True, force=True)
    return wr.setChargeRate(payload), 200, jsonResponseType

@giv_api.route('/setDischargeRate', methods=['POST'])
def setDischrgeRate():
    payload = request.get_json(silent=True, force=True)
    return wr.setDischargeRate(payload), 200, jsonResponseType

@giv_api.route('/setChargeSlot1', methods=['POST'])
def setChrgSlot1():
    payload = request.get_json(silent=True, force=True)
    return wr.setChargeSlot1(payload), 200, jsonResponseType

@giv_api.route('/setChargeSlot2', methods=['POST'])
def setChrgSlot2():
    payload = request.get_json(silent=True, force=True)
    return wr.setChargeSlot2(payload), 200, jsonResponseType

@giv_api.route('/setDischargeSlot1', methods=['POST'])
def setDischrgSlot1():
    payload = request.get_json(silent=True, force=True)
    return wr.setDischargeSlot1(payload), 200, jsonResponseType

@giv_api.route('/setDischargeSlot2', methods=['POST'])
def setDischrgSlot2():
    payload = request.get_json(silent=True, force=True)
    return wr.setDischargeSlot2(payload), 200, jsonResponseType

@giv_api.route('/tempPauseDischarge', methods=['POST'])
def tmpPauseDischrg():
    payload = request.get_json(silent=True, force=True)
    return wr.tempPauseDischarge(payload), 200, jsonResponseType

@giv_api.route('/tempPauseCharge', methods=['POST'])
def tmpPauseChrg():
    payload = request.get_json(silent=True, force=True)
    return wr.tempPauseCharge(payload), 200, jsonResponseType

@giv_api.route('/forceCharge', methods=['POST'])
def frceChrg():
    payload = request.get_json(silent=True, force=True)
    return wr.forceCharge(payload), 200, jsonResponseType

@giv_api.route('/forceExport', methods=['POST'])
def frceExprt():
    payload = request.get_json(silent=True, force=True)
    return wr.forceExport(payload), 200, jsonResponseType

@giv_api.route('/setBatteryMode', methods=['POST'])
def setBattMode():
    payload = request.get_json(silent=True, force=True)
    return wr.setBatteryMode(payload), 200, jsonResponseType

@giv_api.route('/setDateTime', methods=['POST'])
def setDate():
    payload = request.get_json(silent=True, force=True)
    return wr.setDateTime(payload), 200, jsonResponseType

if __name__ == "__main__":
    giv_api.run()