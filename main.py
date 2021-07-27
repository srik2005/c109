import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd


df = pd.read_csv("hw.csv")

height = df['Height(Inches)'].tolist()

weight = df['Weight(Pounds)'].tolist()

heightmean = statistics.mean(height)

weightmean = statistics.mean(weight)

heightmedian = statistics.median(height)

weightmedian = statistics.median(weight)

heightmode = statistics.mode(height)

weightmode = statistics.mode(weight)


print('Mean,Median,Mode of the height is {}, {} and {} respectively'.format(heightmean,heightmedian,heightmode))

print('Mean,Median,Mode of the weight is {}, {} and {} respectively'.format(weightmean,weightmedian,weightmode))


#standard deviation

heightstd = statistics.stdev(height)
weightstd = statistics.stdev(weight)

height1SDstart,height1SDend = heightmean-heightstd,heightmean+heightstd
height2SDstart,height2SDend = heightmean-(2*heightstd),heightmean+(2*heightstd)
height3SDstart,height3SDend = heightmean-(3*heightstd),heightmean+(3*heightstd)

weight1SDstart,weight1SDend = weightmean-weightstd,weightmean+weightstd
weight2SDstart,weight2SDend = weightmean-(2*weightstd),weightmean+(2*weightstd)
weight3SDstart,weight3SDend = weightmean-(3*weightstd),weightmean+(3*weightstd)

# Calculating percentage

heightdata_1SD = [result for result in height if result>height1SDstart and result<height1SDend]
heightdata_2SD = [result for result in height if result>height2SDstart and result<height2SDend]  
heightdata_3SD = [result for result in height if result>height3SDstart and result<height3SDend] 

weightdata_1SD = [result for result in weight if result>weight1SDstart and result<weight1SDend]
weightdata_2SD = [result for result in weight if result>weight2SDstart and result<weight2SDend]  
weightdata_3SD = [result for result in weight if result>weight3SDstart and result<weight3SDend] 

print('{} % of heightdata lies in 1STD'.format(len(heightdata_1SD)*100/len(height)))
print("{} % of heightdata lies in 2STD".format(len(heightdata_2SD)*100/len(height)))
print('{} % of heightdata lies in 3STD'.format(len(heightdata_3SD)*100/len(height)))

print('{} % of weightdata lies in 1STD'.format(len(weightdata_1SD)*100/len(weight)))
print('{} % of weightdata lies in 2STD'.format(len(weightdata_2SD)*100/len(weight)))
print('{} % of weightdata lies in 3STD'.format(len(weightdata_3SD)*100/len(weight)))