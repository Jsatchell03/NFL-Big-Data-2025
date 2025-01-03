import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.patches as patches
from matplotlib.widgets import Button

colors = {
    'ARI':["#97233F","#000000","#FFB612"],
    'ATL':["#A71930","#000000","#A5ACAF"],
    'BAL':["#241773","#000000"],
    'BUF':["#00338D","#C60C30"],
    'CAR':["#0085CA","#101820","#BFC0BF"],
    'CHI':["#0B162A","#C83803"],
    'CIN':["#FB4F14","#000000"],
    'CLE':["#311D00","#FF3C00"],
    'DAL':["#003594","#041E42","#869397"],
    'DEN':["#FB4F14","#002244"],
    'DET':["#0076B6","#B0B7BC","#000000"],
    'GB' :["#203731","#FFB612"],
    'HOU':["#03202F","#A71930"],
    'IND':["#002C5F","#A2AAAD"],
    'JAX':["#101820","#D7A22A","#9F792C"],
    'KC' :["#E31837","#FFB81C"],
    'LA' :["#003594","#FFA300","#FF8200"],
    'LAC':["#0080C6","#FFC20E","#FFFFFF"],
    'LV' :["#000000","#A5ACAF"],
    'MIA':["#008E97","#FC4C02","#005778"],
    'MIN':["#4F2683","#FFC62F"],
    'NE' :["#002244","#C60C30","#B0B7BC"],
    'NO' :["#101820","#D3BC8D"],
    'NYG':["#0B2265","#A71930","#A5ACAF"],
    'NYJ':["#125740","#000000","#FFFFFF"],
    'PHI':["#004C54","#A5ACAF","#ACC0C6"],
    'PIT':["#FFB612","#101820"],
    'SEA':["#002244","#69BE28","#A5ACAF"],
    'SF' :["#AA0000","#B3995D"],
    'TB' :["#D50A0A","#FF7900","#0A0A08"],
    'TEN':["#0C2340","#4B92DB","#C8102E"],
    'WAS':["#5A1414","#FFB612"],
    'football':["#CBB67C","#663831"]
}

cols_needed = ['frameId', 'gameId', 'playId', 'nflId', 'displayName', 'x', 'y', 'club']
data = pd.read_csv("/Users/jsatchell/Documents/Projects/NFL-Big-Data-2025/data/tracking_week_1.csv", usecols=cols_needed)

def animatePlay(gameId, playId):
    fig, ax = plt.subplots(figsize=(15, 8))
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 53.3)
    
    ax.add_patch(patches.Rectangle((0, 0), 120, 53.3, 
                                 facecolor='green', alpha=0.3))
    
    # Add yard lines
    for yard in range(0, 120, 10):
        ax.axvline(yard, color='white', alpha=0.5)
    playData = data.query(f"gameId == {gameId} and playId == {playId}")
    groups = playData.groupby('nflId')
    playerLocations = {}
    playerPlots = {}
    
    for name, group in groups:
        start_x = group['x'].iloc[0]
        start_y = group['y'].iloc[0]
        club = group["club"].iloc[0]
        playerPlots[str(name)] = ax.scatter([start_x], [start_y], c=colors[club][0], s=100)
        coords = group.sort_values('frameId')[['x', 'y']].values
        playerLocations[str(name)] = coords

    totalFrames = len(list(playerLocations.values())[0])
    def animate(frame):
        for nflId, scatter in playerPlots.items():
            x = playerLocations[nflId][frame][0]
            y = playerLocations[nflId][frame][1]
            scatter.set_offsets([[x, y]])
        return playerPlots.values()
    
    animation = FuncAnimation(fig, animate, frames=totalFrames,
                        interval=100, blit=True)
    
    # Create buttons
    ax_playpause = plt.axes([0.8, 0.0, 0.1, 0.075])
    
    button_playpause = Button(ax_playpause, 'Pause')
    
    # Animation controls
    def play_pause(event):
        if animation.running:
            animation.event_source.stop()
            button_playpause.label.set_text('Play')
        else:
            animation.event_source.start()
            button_playpause.label.set_text('Pause')
        animation.running = not animation.running
    

    
    button_playpause.on_clicked(play_pause)
    
    
    # Initialize the animation state
    animation.running = True
    plt.show()
    return animation

    

#
animatePlay(2022091200,643)
