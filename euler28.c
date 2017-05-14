#include <stdio.h>
int main(){
	long s=1,c=1;
	for(int i = 3;i <= 1001;i+=2){
		s+=4*c+10*(i-1);
		c+=4*(i-1);
	}
	printf("%ld\n",s);
}
