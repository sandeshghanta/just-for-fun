#include<stdio.h>
#include<conio.h>
int main()
{
    int n,i,j,el,dup,pass=0;
    printf("Enter size of n*n matrix ");
    scanf("%d",&n);
    int data[n][n],ans[n*n],status[n][n];
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            printf("Enter an element ");
            scanf("%d",&el);
            data[i][j] = el;
        }
    }
    for (i=0;i<n;i++)
    {
        for (j=0;j<n;j++)
        {
            status[i][j] = 0;
        }
    }
    i = 0;
    j = 0;
    for (dup=0;dup<n*n;dup++)
    {
        el = data[i][j];
        printf("%d ",el);
        if (j+1 < n && status[i][j+1] == 0 && pass == 0)
        {
            j = j + 1;
            status[i][j] = 1;
        }
        else if (i+1 < n && status[i+1][j] == 0)
        {
            i = i + 1;
            status[i][j] = 1;
        }
        else if (j-1 >= 0 && status[i][j-1] == 0)
        {
            j = j - 1;
            status[i][j] = 1;
        }
        else
        {
            i = i - 1;
            pass = 1;
            status[i][j] = 1;
        }
        if (pass == 1)
        {
            if (i == j + 1)
            {
                pass = 0;
            }
        }
    }
    return 0;
}
