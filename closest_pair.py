import math

def closest_pair_of_points(t):# giving the pairs as input

    def sort_i_x(t):#sort the points according to the x-coordinate takes O(nlogn)
        return [i for (i,u) in sorted(enumerate(t), key = lambda p: p[1][0])]

    def sort_i_y(t):#sort the points according to the y-coordinate takes O(nlogn)
        return [i for (i,u) in sorted(enumerate(t), key = lambda p: p[1][1])]

    i_x = sort_i_x(t)
    i_y = sort_i_y(t)

    def distance(u,v):#caculate the distance, without get sqrt to save more time
        dx = u[0] - v[0]
        dy = u[1] - v[1]
        return dx*dx + dy*dy

    def search(i,j): ##divide and conquer takes O(nlogn)       
        if i >= j:
            return None
        elif i + 1 == j:
            return (i_x[i], i_x[j])
        else:  ##find the closest pair of points for both left and right side
            mid = (i + j) // 2
            left = search(i, mid)
            right = search(mid+1, j)

            if left is None:
                (i_min, j_min) = right
            elif right is None:
                (i_min, j_min) = left
            else:
                (i_left, j_left) = left
                (i_right, j_right) = right
                d_left = distance(t[i_left], t[j_left])
                d_right = distance(t[i_right], t[j_right])
                if d_left < d_right:
                    (i_min, j_min) = (i_left, j_left)
                else:
                    (i_min, j_min) = (i_right, j_right)

            d = distance(t[i_min], t[j_min])

            x = (t[i_x[mid]][0] + t[i_x[mid + 1]][0]) / 2

            area = [j for j in i_y if abs(t[j][0] - x) <= d]

            for p in range(len(area)):##find the nearest 6 points based on y-coordinate, and consider if there exist any distance smaller than the current closest distance
                r = p + 1
                while r < len(area) and (t[i_y[r]][1] - t[i_y[p]][1]) < d and r - p <= 6:
                    e = distance(t[i_y[p]], t[i_y[r]])
                    if e < d:
                        d = e
                        i_min = p
                        j_min = r
                    r = r + 1                  
            return (i_min, j_min)

    return search(0, len(t) - 1)


print(closest_pair_of_points([(1,2),(2,5),(4,2),(5,7),(6,4),(7,4),(9,7),(9,3),(9,1)]))
print(closest_pair_of_points([(-1000, -10), (-729, -9), (-512, -8), (-343, -7), (-216, -6), (-125, -5), (-64, -4), (-27, -3), (-8, -2), (-1, -1), (0, 0), (8, 2), (27, 3), (64, 4), (125, 5), (216, 6), (343, 7), (512, 8), (729, 9)]))
