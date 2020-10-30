# Closest Pair of Points

Closest pair of points problem solved with the "Divide and Conquer" (D&C) algorithm in Python.
In Bruteforce,the Algorithm work in O(n^2).The Algorithm works more efficiently in O(n*(log(n)) time by using the recursive divide and conquer approach.The program is works in O(n*(log(n)).

### Algorithm:
  1.  We sort all points according to x-coordinates and y-coordinates.

  2. Divide all points in two halves.

3. Recursively find the smallest distances in both subarrays-we take the Euclidean Distance Formula for calculating the distance.
4. Take the minimum of two smallest distances. Let the minimum be d.
5. Create an array that stores all points which are at most d distance away from the middle line dividing the two sets.
6. Find the nearest 6 points based on y-coordinate, and consider if there exist any distance smaller than the current closest distance.
7. Return the minimum of d and the smallest distance calculated in above step-6.
