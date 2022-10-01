import subprocess as sp
import pandas as pd
import sys,os
import matplotlib.pyplot as plt
import japanize_matplotlib
if os.path.exists('demography.csv'):
	data = pd.read_csv('demography.csv')
else:
	sp.call("wget https://toyokeizai.net/sp/visual/tko/covid19/csv/demography.csv",shell=True)
	data = pd.read_csv('demography.csv')
age = data["age_group"].head(9)
deaths = data['death'].head(9)
def main():
	plt.xticks(rotation=90)
	plt.plot(age,deaths)
	plt.tight_layout()
	plt.savefig('result.png')
	plt.show()
main()