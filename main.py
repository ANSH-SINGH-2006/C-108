import random
import plotly.express as px
import plotly.figure_factory as ff
total=0
count=[]
diceResult=[]

for sum in range(100):
    x=random.randint(1,6)
    y=random.randint(1,6)
    total=x+y
    diceResult.append(total)
    count.append(sum)

print(count, diceResult)

#fig=px.bar(x=diceResult, y=count)
fig=ff.create_distplot([diceResult], ["Result"])
fig.show()