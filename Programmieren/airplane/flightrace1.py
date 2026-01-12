import numpy as np
import matplotlib.pyplot as plt

# Die Fliegojglos
fj =        [[8,6,5,8,7,7,10,5], [9,8,8,5,6,5,10,3], [8,3,7,4,7,7,10,6], [7,6,5,4,3,8,10,5], [9,8,5,6,7,6,10,6]]
r_wing =    [[6,8,7,8,7,5,10,7,], [5,8,7,9,8,5,10,5], [6,7,5,6,7,7,10,6], [7,6,5,6,7,5,10,5], [7,6,6,6,7,7,10,7]]
jet_67 =    [[5,6,6,7,7,5,10,5], [5,6,2,8,8,9,10,6], [3,4,1,7,8,5,10,8], [4,4,1,8,6,8,10,10], [3,6,2,5,9,8,10,6]]
fliegerle = [[7,8,7,9,5,5,10,2], [7,8,8,9,8,9,10,4], [7,7,7,9,8,5,10,6], [9,9,9,10,9,5,10,5], [8,9,8,9,9,9,10,6]]

fj_result=7.43
fliegerle_result=9.12

# Calculate Fliegojglos total score
for i in range(len(fj)):
    fj[i] = np.array(fj[i])
    fj_result += sum(fj[i])

# Calculate Fliegerle total score
for i in range(len(fliegerle)):
    fliegerle[i] = np.array(fliegerle[i])
    fliegerle_result += sum(fliegerle[i])

# Print results
print("Fliegerle total score:", fliegerle_result)
print("Fliegojglos total score:", fj_result)



