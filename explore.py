import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')

actions = pd.read_csv('final_match_xt.csv')

player_xt = actions.groupby(['team', 'player'])['xt'].sum().reset_index()
player_xt = player_xt.sort_values('xt', ascending=False).head(10)

colors = ['#4d94c9' if team == 'Argentina' else '#d4a017' for team in player_xt['team']]

fig, ax = plt.subplots(figsize=(10, 6), facecolor='#0d1b2a')
ax.set_facecolor('#0d1b2a')

ax.barh(player_xt['player'][::-1], player_xt['xt'][::-1], color=colors[::-1])

ax.set_xlabel('Total xT Generated', color='white', fontsize=11)
ax.set_title('Top 10 Players by Total xT — WC 2022 Final', color='white', fontsize=14, pad=15)
ax.tick_params(colors='white', labelsize=10)
for spine in ax.spines.values():
    spine.set_visible(False)

from matplotlib.lines import Line2D
legend_elements = [Line2D([0], [0], color='#4d94c9', lw=6, label='Argentina'),
                   Line2D([0], [0], color='#d4a017', lw=6, label='France')]
ax.legend(handles=legend_elements, loc='lower right', frameon=False, labelcolor='white')

plt.tight_layout()
plt.savefig('top_xt_players.png', dpi=200, facecolor='#0d1b2a', bbox_inches='tight')
print("Saved top_xt_players.png")