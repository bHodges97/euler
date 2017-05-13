#include <stdio.h>

int a(int in){
	int s = 0;
	for(int i = 1;i <= in/2; ++i){
		if(in%i==0)s+=i;
	}
	return s>in;
}

int main(){
	int max = 28126;
	int acount = 0;
	int abundants[max];
	int nums[max];
	for(int i = 0;i < max;++i){
		nums[i] = 0;
		if(a(i)){
			abundants[acount]=i;
			++acount;
		}
	}
	int t;
	for(int i = 0;i < acount;++i){
		for(int j = i;j < acount;++j){
			t = abundants[i]+abundants[j];
			if(t<=max)nums[t]=t;	
		}
	}
	t=0;
	for(int i=0;i<max;++i)if(!nums[i])t+=i;
	printf("%d\n",t);
}
