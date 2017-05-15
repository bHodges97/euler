#include <stdio.h>
#include <math.h>


int main(){
	int a,b,c,i;
	int p[1000];
	for(a = 0;a < 1000;++a)p[a]=0;
	for(a = 1; a < 1000; ++a){
		for(b = 1;b < 1000; ++b){
			c = a*a+b*b;
			for(i = 2;i*i<c;++i);
			if(i*i!=c)continue;
			c = a+b+i;
			if(c<1000)++p[c];
		}
	}
	a = p[0];
	for(i = 1;i < 1000;++i){
		if(p[i]>a){
			a=p[i];
			b=i;
		}
	}
	printf("%d\n",b);
}
