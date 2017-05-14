//oeis.org/A001913 has the answer ;)

//a solution of note found on the euler forums
//find remainder of 1/n
//multiply it by 10 and keep finding remainders  which is each digit after the decimal
//if one of the remainders is the same as the first remainder its repeating


#include <stdio.h>

int main(){
	int r,r0,c,max,index;	
	for(int i = 999; i > 10; i-=2){
		if(i%5==0)continue;
		//perhaps this is wrong since i'm not keeping track of all the remainders
		//but thos gives the right ans
		r0 = 1%i;
		r = r0*10;
		for(c = 0; c < 100000; ++c){
			r = r%i;
			if(r==r0)break;
			r*=10;
		}
		if(c > max){
			max = c;
			index = i;
		}
	}
	printf("%d\n",index);
}
