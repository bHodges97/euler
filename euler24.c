#include <stdio.h>

#define s 10//10 digits

int fact(int i){
	if(i>1)return i*fact(i-1);
	else return 1;
}

int main(){//left to right
	int digits[s] = {0,1,2,3,4,5,6,7,8,9};
	int perm = 1000000;
	for(int i = s-1;i >= 0;--i){
		int fac = fact(i);
		int n = perm/fac;
		int r = perm%fac;
		if(!r)--n;
		perm-=n*fac;//not r for special case when there is 0 perms left
		int index = 0;
		while(n>0){
			do{
				++index;
			}while(digits[index]<0);
			--n;
		}
		printf("%d",digits[index]);
		digits[index] = -1;
	}
	printf("\n");
}
