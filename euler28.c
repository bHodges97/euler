#include <stdio.h>


int main(){
	int w,c=1;
	long s=1;
	for(int i = 3;i <= 1001;i+=2){
		w=(i-1);
		c+=w;
		s+=c;
		c+=w;
		s+=c;
		c+=w;
		s+=c;
		c+=w;
		s+=c;
	}
	printf("%ld\n",s);
}
