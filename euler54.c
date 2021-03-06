#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct{
	char rank;
	char suit;
}card;

void fix(char *in){
	const char arr[] = {'T','J','Q','K','A'};
	for(int i = 0;i < 5;++i)if(*in==arr[i]){*in=10+i;return;}
	*in-='0';
}

//bubble sort
void sort(card *in,int size){
	int i,m = size-1;
	bool done = false;
	card c;

	while(!done){
		done = true;
		for(i = 0;i < m;++i){
			if(in[i].rank>in[i+1].rank){
				c=in[i+1];
				in[i+1]=in[i];
				in[i]=c;
				done = false;
			}
		}
		--m;
	}
}

int eval(card *in){
	sort(in,5);
	bool flush = true,straight = true;
	bool equ[4];
	int i;
	for(i = 0;i < 4;++i){
		if(in[i].suit != in[i+1].suit)flush = false;
		if(in[i].rank+1 != in[i+1].rank)straight = false;
		equ[i] = in[i].rank == in[i+1].rank;
	}

	//straight flush + royal flush
	if(straight && flush)return 900+in[0].rank;

	//four of a kind
	if(equ[0] && equ[1] && equ[2] && equ[3])return 800+in[0].rank;
	
	//full house
	if(equ[0] && equ[2] && equ[3])return 700+in[3].rank;
	if(equ[0] && equ[1] && equ[3])return 700+in[1].rank;
	
	//flush and straight
	if(flush)return 600+in[0].rank;
	if(straight)return 500+in[0].rank;

	//three of a kind
	if(equ[0] && equ[1])return 400+in[0].rank;
	if(equ[1] && equ[2])return 400+in[1].rank;
	if(equ[2] && equ[3])return 400+in[2].rank;
	
	//2 pairs
	if(equ[0] && equ[2])return 300+in[2].rank;
	if(equ[0] && equ[3])return 300+in[3].rank;
	if(equ[1] && equ[3])return 300+in[3].rank;

	//1 pair
	if(equ[0])return in[0].rank;
	if(equ[1])return in[1].rank;
	if(equ[2])return in[2].rank;
	if(equ[3])return in[3].rank;
	return 0;
}

int main(){
	FILE *file = fopen("p054_poker.txt","r");
	const int lines = 1000;
	card p1[lines][5],p2[lines][5];
	int i,j,k,t,wins=0;
	for(i = 0; i < lines; ++i){
		for(j = 0;j < 5; ++j){
			fscanf(file,"%c%c ",&p1[i][j].rank,&p1[i][j].suit);
			fix(&p1[i][j].rank);
		}
		for(j = 0;j < 5; ++j){
			fscanf(file,"%c%c ",&p2[i][j].rank,&p2[i][j].suit);
			fix(&p2[i][j].rank);
		}
	}
	for(i = 0; i < lines; ++i){
		j = eval(&p1[i][0]);
		k = eval(&p2[i][0]);
		if(j > k){
			++wins;
		}else if(j == k){
			for(t = 4;t >= 0;--t){
				if(p1[i][t].rank > p2[i][t].rank){
					++wins;
					break;
				}else if(p1[i][t].rank < p2[i][t].rank){
					break;
				}
			}
		}
	}
	printf("%d\n",wins);
}
