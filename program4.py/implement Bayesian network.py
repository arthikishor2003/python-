# Probability of Rain
P_Rain = 0.2

# Probability of Sprinkler given Rain
P_Sprinkler_Rain = 0.01
P_Sprinkler_NoRain = 0.4

# Probability of Wet Grass given Rain and Sprinkler
P_Wet_Rain_Sprinkler = 0.99
P_Wet_Rain_NoSprinkler = 0.8
P_Wet_NoRain_Sprinkler = 0.9
P_Wet_NoRain_NoSprinkler = 0.0

# Calculate probability of sprinkler
P_Sprinkler = (
    P_Sprinkler_Rain * P_Rain
    + P_Sprinkler_NoRain * (1 - P_Rain)
)

print("Probability of Rain =", P_Rain)
print("Probability of Sprinkler =", round(P_Sprinkler, 4))

# Calculate probability of Wet Grass
P_WetGrass = (
    P_Rain * P_Sprinkler_Rain * P_Wet_Rain_Sprinkler
    + P_Rain * (1 - P_Sprinkler_Rain) * P_Wet_Rain_NoSprinkler
    + (1 - P_Rain) * P_Sprinkler_NoRain * P_Wet_NoRain_Sprinkler
    + (1 - P_Rain) * (1 - P_Sprinkler_NoRain)
    * P_Wet_NoRain_NoSprinkler
)

print("Probability of Wet Grass =", round(P_WetGrass, 4))