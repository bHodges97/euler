#include <stdio.h>

int ipow(int base,int pow){
	int r = 1;
	for(int i = 0;i < pow;++i)r*=base;
	return r;
}

int main(){
	int r=0;
	for(int i = 2;i < 355000; ++i){
		int sum = 0,t = i,p;
		for(int d = 6;d >= 0;--d){
			p = t/ipow(10,d);
			t -= p*ipow(10,d);
			sum+=ipow(p,5);
		}
		if(sum==i)r+=i;
	}
	printf("%d\n",r);
}
