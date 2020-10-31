# Closest Pair of Points

Closest pair of points problem solved with the "Divide and Conquer" (D&C) algorithm in Python.
In Bruteforce,the Algorithm work in O(n^2).The Algorithm works more efficiently in O(n*(log(n)) time by using the recursive divide and conquer approach.The program is works in O(n*(log(n)).
### Algorithm-Divide & conquer(Strategy)-Time Complexity Calculation
DIVIDE-Divide the problem into two equal-sized sub problems
CONQUER-Solve those sub problems recursively
MERGE-Merge the sub problem solutions into an overall solution

1. Partition two dimensional pair S into subsets S1(Left) and S2(right) by a vertical line L at the median x-coordinate of S.
2. Solve the problem recursively on S1 and S2.
3. let {p1,p2} be the closest pair in S1 and {q1,q2} in S2.
4. let R1=distance(p1,p2) and R2=distance(q1,q2)
5. let R=min(R1,R2)
6. in order to merge we have to determine if exists a pair of points {p,q}where p=>S1,q=>S2 and distance(p,q) < R
7. if so,p and q must be both be within R of L
8. let P1 and P2 be vertical regions of the plane of width R on either side(left or right) of L.
9. if {p,q} exists,p must be within P1 and q within P2.
10. however every point in S1 and S2 may be candidate,as long as each is within R of L which the complexity is calculated as O(n/2)*O(n/2)=O(n^2)
11. We can able optimize it by,For a point p in P1,which portion of P2 should be checked?
12. Thus,we can limit the portion of p2
for example,
We are limiting the points to consider for point p must lie within Rectange.For eg.The points within R of p in the y projection need to be considered.(6points)
13. After sorting the points on y coordinate we can find the points by scanning the sorted lists.points are sorted by y coordiantes.(it can also be done with x-coordinates)
14. To prevent resorting in O(nlogn) in each merge,two previously sorted lists are merged in O(n).Thus, the time complexity is optimized to O(nlogn)


### Steps used in the program:
  1.  We sort all points according to x-coordinates and y-coordinates.

  2. Divide all points in two halves.

3. Recursively find the smallest distances in both subarrays-we take the Euclidean Distance Formula for calculating the distance.
4. Take the minimum of two smallest distances. Let the minimum be d.
5. Create an array that stores all points which are at most d distance away from the middle line dividing the two sets.
6. Find the nearest 6 points based on y-coordinate, and consider if there exist any distance smaller than the current closest distance.
7. Return the minimum of d and the smallest distance calculated in above step-6.
