#include <stdio.h>
int main (void){
	int n;
	int x;
	int sum;

	printf("������������͂��܂��� :");
	scanf("%d", &n);
	sum = 0;
	while (n-- > 0){
		printf("����=");
		scanf("%d", &x);
		sum += x;
	}
	printf("���v=%d\n", sum);
	return(0);
}
	