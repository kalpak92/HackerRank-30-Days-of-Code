# Enter your code here. Read input from STDIN. Print output to STDOUT
mealCost = float(raw_input())
tipPercent = int(raw_input())
taxPercent = int(raw_input())
output = "The total meal cost is "+str(int(round(mealCost + tipPercent*mealCost*0.01 + taxPercent*mealCost*0.01)))+" dollars."
print output