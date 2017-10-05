#include <stdio.h>

int main(){
	//last 10 digits 0f 28433 * 2^7830457 - 1
	int i,j,k;
	int pow = 7830457;
	unsigned long long m = 1; 
	unsigned long long lim = 10000000000;
	for(i = 0;i < pow;++i){
		m*=2;
		if(m>lim)m%=lim;
	}
	m = m * 28433 + 1;
	printf("%llu\n",m%lim);


}
