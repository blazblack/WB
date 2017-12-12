#include <stdio.h>
int main (void){
	int n;
	int x;
	int sum;

	printf("®”‚ğ‰½‰ñ“ü—Í‚µ‚Ü‚·‚© :");
	scanf("%d", &n);
	sum = 0;
	while (n-- > 0){
		printf("®”=");
		scanf("%d", &x);
		sum += x;
	}
	printf("‡Œv=%d\n", sum);
	return(0);
}
	