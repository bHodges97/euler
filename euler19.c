#include <stdio.h>

int main(){
	int count = 0,day = 1,maxday;
	for(int year = 1;year < 100;++year){
		if(year%4==0 && (year%100!=0 || year == 1000)){
			maxday = 366;
		}else{
			maxday = 365;
		}
		int i;
		for(i = 0;i < maxday;++i){
			if(day == 7 || day == 0){
				day = 0;
				int t = maxday == 365?i:i-1;
				if(i == 0||i == 31 || t == 59 || t == 90|| t == 120 || t == 151
						|| t == 181 || t == 212 || t == 243 || t == 273 || t == 304 || t == 334){
					++count;
					printf("%d %d\n",i,year+1900);
				}
			}
			++day;
		}
	}
	printf("%d\n",count);
}

