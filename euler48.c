#include <stdio.h>


int main(){
	unsigned long long i,j,k;
	unsigned long long max = 10000000000;
	unsigned long long sum = 0;
	// 10405071317
	for(i = 1;i <= 1000;++i){
		k = i;
		for(j = 1;j < i;++j){
			k*=i;
			while(k>max){
				k-=max;
			}		
		}
		printf("%llu\n",k);
		sum+=k;
		while(sum>max){
			sum-=max;
		}
	}
	printf("%llu\n",sum);
}
