#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE *file = fopen("primes.txt","r");
	int primes[78498];
	long long unsigned sums[78498];
	int i,j,k,m=0,m1=0,m0;
	for(i = 0;i < 78498;++i){
		fscanf(file,"%d,",&primes[i]);
	}
	int flag;
	//iterate through the primes
	for(i = 0;i < 78498;++i){
		sums[i] = 0;
		if(sums[0]>1000000)return 0;//stop(it just works?????)
		//add to list of prime sums
		for(j = 0;j < i;++j){
			m0 = i-j+1;
			sums[j]+=primes[i];
			//if the length is too short don't bother
			if(m0<=m1)continue;
			//check if its a prime
			for(k = 0;k < 78498;++k){
				if(sums[j] < primes[k]){
					break;
				}
				if(primes[k] == sums[j]){
					m = primes[k];
					m1 = m0;
					printf("found %d %d\n",m,m0);
				}
			}
		}
	}
}

