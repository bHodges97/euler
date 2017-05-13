#include <stdio.h>

char a[1000],b[1000],c[1000];

int main(){
	int count = 1,i = 0;
	for(i = 0;i < 1000;++i){
		a[i]=0;
		b[i]=0;
		c[i]=0;
	}
	b[0] = 1;
	while(!c[999]){
		for(i = 0;i < 999;++i){
			c[i]+=a[i]+b[i];
			if(c[i] > 9){
				c[i+1] = 1;
				c[i] = c[i]%10;
			}
			a[i] = b[i];
			b[i] = c[i];
			c[i] = 0;
		}
		++count;
	}
	printf("%d\n",count);
}

