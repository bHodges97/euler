#include <stdio.h>
#include <math.h>

int main(){
	double ans[10000] = {0};
	int count = 0,f=0,i;
	double r,a,b;
	for(a = 2;a <= 100;++a){
		for(b = 2;b <= 100;++b){
			r=pow(a,b);
			for(i = 0;i < count;++i){
				if(ans[i]==r)break;
			}
			if(i==count){
				ans[i]=r;
				count++;
			}
		}
	}
	printf("%d\n",count);
}
