#include <stdio.h>

int main(){
	int i,j,len = 1000;//2^1000 is less than 1000 digits as 2 < 10
	char a[len];
	for(i = 0;i < len;++i)a[i]=0;
	a[0]=1;
	for(i = 0;i < 1000;++i){
		for(j = len-1;j >= 0;--j){
			a[j]*=2;
			if(a[j]>=10){
				a[j]-=10;
				a[j+1]+=1;
			}
		}	
	}
	j = 0;
	for(i = 0;i < len;++i){
		j+=a[i];
	}
	printf("%d\n",j);
}
