#include <stdio.h>
int main (void){
	int n;
	int x;
	int sum;

	printf("整数を何回入力しますか :");
	scanf("%d", &n);
	sum = 0;
	while (n-- > 0){
		printf("整数=");
		scanf("%d", &x);
		sum += x;
	}
	printf("合計=%d\n", sum);
	return(0);
}
	