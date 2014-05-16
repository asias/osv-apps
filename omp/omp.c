#include<stdio.h>
#include<omp.h>
int main()
{
	int i=0;
	#pragma omp parallel for
	for(i=0;i<4;i++)
	{
		printf("here %d\n",omp_get_thread_num());                           
	}   
	return 0;
}
