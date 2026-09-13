# Question: Classify the temperature.

t = int(input())

if t <= 0:
    print("Freezing weather")
elif t > 0 and t <= 10:
    print("Very Cold weather")
elif t > 10 and t <= 20:
    print("Cold weather")
elif t > 20 and t <= 30:
    print("Normal in Temp")
elif t > 30 and t < 40:
    print("Its Hot")
else :
    print("Its Very Hot")
