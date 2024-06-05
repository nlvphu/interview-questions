def getTrueWater(height):
    leftWater = getWater(height[::-1])[::-1]
    rightWater = getWater(height)
    total = 0
    for left, right, h in zip(leftWater, rightWater, height):
        total += max(min(left, right) - h, 0)
    return total

def getWater(height):
    n = len(height)

    level =[]

    cur_left =0

    for i in range(n):
        cur_left = max(cur_left, height[i])
        level.append(cur_left)
    
    return level


    

if __name__ =='__main__':

    #height = [0,1,0,2,1,0,1,3,2,1,2,1]  
    height = [4,2,0,3,2,5]


    print(getTrueWater(height))
