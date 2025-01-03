# gameId, playId, down, yrdsToGo, distFromTD, isShotgun, isSingleback, isEmpty, isIForm, isPistol, isJumbo
# wr0StartX, wr0StartY, wr1StartX, wr1StartY, wr2StartX, wr2StartY, wr3StartX, wr3StartY, wr4StartX, wr4StartY, te0StartX, te0StartY, te1StartX, te1StartY, te2StartX, te2StartY, te3StartX, te3StartY,
# te4StartX, te4StartY,rb0StartX, rb0StartY, rb1StartX, rb1StartY, rb2StartX, rb2StartY, rb3StartX, rb3StartY, qbStartX, qbStartY, lineman0StartX, lineman0StartY, lineman1StartX, lineman1StartY, lineman2StartX, lineman2StartY,
# lineman3StartX, lineman3StartY, lineman4StartX, lineman4StartY, wrWeightChange, rbWeightChange, teWeightChange, linemanWeightChange, teamWeightChange, runScheme
 
# Random Forest Classification

import numpy as np
import pandas as pd

week1TrackingData = pd.read_csv("/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/tracking_week_1.csv")
playData = pd.read_csv("/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/plays.csv")
# nflVerseData = pd.read_csv("/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/play_by_play_2022.csv")

def get_previous_play(current_gameId, current_playId, df = playData):
    # Get all plays from the same game
    game_plays = df[df['gameId'] == current_gameId].copy()
    
    # Get current play info
    current_play = game_plays[game_plays['playId'] == current_playId].iloc[0]
    current_team = current_play['possessionTeam']
    
    # Convert gameClock to seconds for proper ordering
    def clock_to_seconds(clock_str):
        minutes, seconds = map(int, clock_str.split(':'))
        return minutes * 60 + seconds
    
    game_plays['clockSeconds'] = game_plays['gameClock'].apply(clock_to_seconds)
    current_clock_seconds = clock_to_seconds(current_play['gameClock'])
    
    # Find previous play
    prev_play_df = game_plays[
        ((game_plays['quarter'] == current_play['quarter']) & 
         (game_plays['clockSeconds'] > current_clock_seconds)) |
        (game_plays['quarter'] < current_play['quarter'])
    ].sort_values(['quarter', 'clockSeconds'], ascending=[False, True])
    
    # Return 0 if no previous play exists
    if prev_play_df.empty:
        return 0
        
    # Get previous play
    prev_play = prev_play_df.iloc[0]
    
    # Return 0 if possession team is different
    if prev_play['possessionTeam'] != current_team:
        return 0
        
    return prev_play['playId']

# def getPosGroupWeights(gameId, playId):


def getData(gameId, playId):
    result = str(gameId) + ", " + str(playId)
    currPlayData = playData.loc[(playData["playId"] == playId) & (playData["gameId"] == gameId)].reset_index(drop=True)
    down , yardsToGo, yardlineNumber, defensiveTeam, yardlineSide, formation = currPlayData.loc[0, ["down", "yardsToGo", "yardlineNumber", "defensiveTeam","yardlineSide", "offenseFormation"]].values
    distFromTD = -1
    if(defensiveTeam == yardlineSide):
        distFromTD = yardlineNumber    
    else:
        distFromTD = 100 - yardlineNumber
    prevPlay = get_previous_play(gameId, playId)
    print(down, yardsToGo, distFromTD)
    print(prevPlay)

getData(2022091200,643)

