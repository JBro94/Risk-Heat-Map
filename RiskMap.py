import pandas as pd
import numpy as np
import seaborn as sb

#definition of the risk map
dataFrame = pd.DataFrame(columns=['risk', 'likelihood', 'impact', 'maturity', 'score'])

#shorthand for risks facing the project
dataFrame['risk'] = ['users', 'team', 'budget', 'security', 'time']

#percent chance of risk occurence 0 - 1
dataFrame['likelihood'] = [.25, .15, .85, .6, .5]

#impact this risk will have on project (scale 1-10)
dataFrame['impact'] = [1, 5, 5, 1, 8]

#how well the org. can handle this type of risk (scale 1-5)
dataFrame['maturity'] = [5, 2, 3, 4, 5]

#how the risk scores likelihood * impact
dataFrame['score'] = dataFrame['likelihood'] * dataFrame['impact']
print(dataFrame)

riskScoresPivot = dataFrame.pivot('impact', 'likelihood', 'score')

print(riskScoresPivot)

labelsPivot = dataFrame.pivot('impact', 'likelihood', 'risk')

print(labelsPivot)

riskHeatMap = sb.heatmap(riskScoresPivot, cmap='YlOrRd', annot=labelsPivot, fmt='')



