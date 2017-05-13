#include <stdio.h>
#include <stdlib.h>

#define rows 15

int main(){
	int len = rows*(rows+1)/2;
	int arr[len];
	FILE *file = fopen("18.txt","r");
	for(int i = 0;i < len;++i){
		fscanf(file,"%d",&arr[i]);
	}
	fclose(file);
	int l,r,m,w=2,c=0;
	for(int i = 1;i < len;++i){
		l =0;r=0;
		if(c){
			l = arr[i-w];
		}
		if(c!=w-1){
			r = arr[i-w+1];
		}
		m = l>r?l:r;
		arr[i]+=m;
		++c;
		printf("%d,",arr[i]);
		if(c == w){
			++w;
			c=0;
			printf("\n");
		}
	}
	m = 0;
	for(int i = len;i > len-rows;--i){
		m = arr[i]>m?arr[i]:m;
	}
	printf("%d\n",m);
}

