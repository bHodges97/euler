#include <stdio.h>
#include <stdlib.h>

int primes[1000];

int isPrime(int a){
	int n;
	for(int i = 0;i < 1000;++i){
		if(primes[i]==a){
			return 1;
		}
		if(a<primes[i])return 0;
		if(a%primes[i]==0){
			return 0;
		}
	}
	for(int i = primes[999];i*i<a;i+=2){
		if(a%i==0)return 0;
	}
	return 1;
}


int main(){
	FILE *file = fopen("primes.txt","r");
	for(int i = 0;i < 1000;++i){
		fscanf(file,"%d,",&primes[i]);
	}
	fclose(file);
	int a,b,n,product,y,index=0;
	for(a = -1000;a < 1000;++a){
		for(b = -1000;b < 1000;++b){
			for(n = 0;;++n){
				y = n*n+a*n+b;
				if(isPrime(y)){
					if(n>=index){
						index = n;
						product = a*b;
					}
				}else{
					break;
				}
			}
		}
	}
	printf("%d\n",product);
}
