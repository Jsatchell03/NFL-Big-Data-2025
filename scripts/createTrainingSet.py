# gameId, playId, down, yrdsToGo, distFromTD, isShotgun, isSingleback, isEmpty, isIForm, isPistol,
# wr0StartX, wr0StartY, wr1StartX, wr1StartY, wr2StartX, wr2StartY, wr3StartX, wr3StartY, wr4StartX, wr4StartY, te0StartX, te0StartY, te1StartX, te1StartY, te2StartX, te2StartY, te3StartX, te3StartY,
# te4StartX, te4StartY,rb0StartX, rb0StartY, rb1StartX, rb1StartY, rb2StartX, rb2StartY, rb3StartX, rb3StartY, qbStartX, qbStartY, lineman0StartX, lineman0StartY, lineman1StartX, lineman1StartY, lineman2StartX, lineman2StartY,
# lineman3StartX, lineman3StartY, lineman4StartX, lineman4StartY, wrWeightChange, rbWeightChange, teWeightChange, linemanWeightChange, teamWeightChange
 
# Random Forest Classification

import numpy as np
import pandas as pd

week1TrackingData = pd.read_csv("/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/tracking_week_1.csv", usecols=cols_needed)
playData = pd.read_csv("/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/plays.csv", usecols=cols_needed)

def getData(gameId, playId):
    result = str(gameId) + ", " + str(playId)

