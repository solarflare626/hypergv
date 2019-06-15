How to use:
1. install python
2. set data on data.txt
2.rightclick hypergv.py and click edit with idle
3. press F5 on opened application

use @ for hgv
use >>

Sample Data Format:

[{0,1},{0,1},{0,1},{0,1}]
[{0,1},{0,1},{0,1,2},{0,1}]
[{0,1,2},{0,2},{0,1,2},{0,1,2}]
[{3},{0,1,3},{0,1,3},{0,1,3}]


Sample inputs: 
1>>2
1@2>>3


[1@({0,1}@2)]@(1@{1,2})>>1
[1@({0,1}@2)]@(1@{1,2})>>[{1,0}@3]