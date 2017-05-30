#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


/**
 * Using dijkstra
 * each iteration extracts node with current min length
 * and recalculate neighbour costs
 **/
int main(){
	//test case
	//const int size = 5;
	//long m[][5] = {{131,673,234,103,18},{201,96,342,965,150},{630,803,746,422,111},{537,699,497,121,956},{805,732,524,37,331}};
	const int size = 80;
	long m[size][size];
	long r[size][size];//length
	short ignore[size][size];
	int i,j;
	long k;

	//open file
	FILE *file = fopen("p081_matrix.txt","r");
	if(size==80)//dont read on test
	for(i = 0;i < 80;++i){
		for(j = 0;j < 80;++j){
			fscanf(file,"%ld,",&m[i][j]);
		}
	}
	printf("Solve for %d by %d\n",size,size);
	for(i = 0;i < size;++i){
		for(j = 0;j < size;++j){
			r[i][j] = INT_MAX;
			ignore[i][j] = 0;	
		}
	}
	r[0][0] = m[0][0];
	int x,y,x1,y1;
	int points[][2] = {{-1,0},{1,0},{0,-1},{0,1}};
	while(1){
		k = INT_MAX;
		x = -1;y = -1;
		for(i = 0;i < size;++i){
			for(j = 0;j < size;++j){
				if(!ignore[i][j] && r[i][j]<k){
					k = r[i][j];
					x = i;
					y = j;
				}
			}
		}	
		if(x == -1 || y == -1)break;//queue empty
		if(x == size-1 && y == size-1)break;//at end
		ignore[x][y] = 1;
		for(i = 0;i < 4;++i){
			x1 = points[i][0]+x;
			y1 = points[i][1]+y;
			if(x1 < 0 || x1 >=size)continue;
			if(y1 < 0 || y1 >=size)continue;
			k = r[x][y]+m[x1][y1];
			if(k < r[x1][y1]){
				r[x1][y1]=k;
			}
		}
	}
	printf("%ld\n",r[size-1][size-1]);

}
