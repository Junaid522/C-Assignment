#include<stdio.h>
#include<unistd.h>
#include <sys/wait.h>
int main()
{
	int pid=0;
	int sum=0,sum1=0,sum2=0,sum3=0,sum4=0,child1=0,child2=0,child3=0;
	int a;
	for(a=1;a<=25;a++)
		{
			sum1+=a;
		}
	printf("Sum calculated by Parent : %d\n",sum1);
	sum=sum+sum1;
	child1=fork();
 	if(child1>0)
	{
		
		child2=fork();
		if(child2>0)
		{
			//pid=waitpid(child2,NULL,1);
			child3=fork();
			if(child3>0)
			{
				//pid=wait(&status);
				
				//printf("Total Sum : %d\n",sum);
			}
			else if(child3==0)
			{
				int b;
				for(b=26;b<=50;b++)
				{
					sum4+=b;
				}
				sum=sum+sum4;
				printf("Sum calculated by Child 3 : %d\n",sum4);
	
			}
		}
		else if(child2==0)
		{
			int c;
			for(c=51;c<=75;c++)
			{
				sum3+=c;
			}
			sum=sum+sum3;
			printf("Sum calculated by Child 2 : %d\n",sum3);
			//printf("Total Sum : %d\n",sum);	
		}			
	}
	else if(child1==0)
	{
		int d;
		for(d=76;d<=100;d++)
		{
			sum2+=d;
		}
		sum=sum+sum2;
		printf("Sum calculated by Child 1 : %d\n",sum2);
		
	}
	printf("Sum calculated by all processes : %d\n", sum);
		
}
