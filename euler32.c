#include <stdio.h>
#include <time.h>

int ten(int in){
	int b=1;
	for(int i = 0;i < in;++i)b*=10;
	return b;
}

int len(int in){
	for(int i = 9; i > 0; --i)
		if(in/ten(i))return i+1;
	return 1;
}

int main(){
	clock_t t1, t2;
	t1 = clock();
	int digits[10];
	int dig[9];
	int t,l0,l1,l2,i0,i1,i2,i,j,k,sum=0;
	for(int i = 10;i < 1000000;++i){
		for(j=0;j<10;++j)digits[j]=0;
		i0=i;
		l0=len(i0);
		if(l0==8)continue;
		for(k = 0;k < l0;++k){
			t=i0%10;
			i0/=10;
			dig[k]=t;
			if(!t||digits[t]){l0=10;break;}
			digits[t]=1;
		}
		if(l0==10)continue;
		for(j=1;j*j <= i;++j){
			if((i%j))continue;
			for(t=0;t<10;++t)digits[t]=0;
			for(t=0;t<l0;++t)digits[dig[t]]=1;
			i1=j;
			i2=i/j;
			l1=len(i1);
			l2=len(i2);
			if((l0+l1+l2)!=9)continue;
			for(k = 0;k < l1;++k){
				t=i1%10;
				i1/=10;
				dig[k+l0]=t;
				if(!t||digits[t]){l1=10;break;}
				digits[t]=1;
			}
			if(l1==10)continue;
			for(k = 0;k < l2;++k){
				t=i2%10;
				i2/=10;
				dig[k+l0+l1]=t;
				if(!t||digits[t]){l1=10;break;}
				digits[t]=1;
			}
			if(l1==10)continue;
			sum+=i;
			break;
		}
	}
	t2 = clock();
	printf("Time taken:%g\n",(float)(t2-t1));
	printf("%d\n",sum);
}

