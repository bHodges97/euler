#include <stdio.h>

int main(){
	int a,b,c = 0;
	int lista[4],listb[4];
	int a0[2],b0[2];
	for(b = 11;b < 100;++b){
		b0[1] = b/10;
		b0[0] = b%10;
		if(b%10==0)continue;
		for(a = 10;a < b;++a){
			if(a%b==0)continue;
			if(a%10==0)continue;
			a0[1] = a/10;
			a0[0] = a%10;
			if(b0[1] == a0[1]){
				if((float)b/(float)b0[0] == (float)a/(float)a0[0]){
					lista[c] = a;
					listb[c] = b;
					++c;
					break;					
				}		
			}
			if(b0[1] == a0[0]){
				if((float)b/(float)b0[0] ==(float)a/(float)a0[1]){
					lista[c] = a;
					listb[c] = b;
					++c;
					break;
				}
			}
			if(b0[0] == a0[0]){
				if((float)b/(float)b0[1] ==(float)a/(float)a0[1]){
					lista[c] = a;
					listb[c] = b;
					++c;
					break;
				}
			}
			if(b0[1] == a0[1]){
				if((float)b/(float)b0[1] ==(float)a/(float)a0[0]){
					lista[c] = a;
					listb[c] = b;
					++c;
					break;
				}
			}
		}
	}
	for(int i = 0;i < 4;++i){
		printf("%d/%d\n",lista[i],listb[i]);
	}//use a calculator

}
