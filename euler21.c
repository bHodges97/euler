#include <stdio.h>

int s(int in){
	int s = 0;
	for(int i = 1; i <= in/2;i++){
		if(in%i==0)s+=i;
	}
	return s;
}


int main(){
	int sum = 0;
	int m[10000];
	int t;
	for(int i = 0;i < 220;++i)m[i]=0;
	for(int i = 220;i < 10000;++i)m[i] = s(i);
	for(int i = 220; i < 10000;++i){
		t = m[i];
		if(t<=10000 && t!=i && m[t] == i){
			sum+=i;
		}
	}
	printf("%d\n",sum);
}
