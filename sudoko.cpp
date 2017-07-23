#include<bits/stdc++.h>
using namespace std;
int main()
{
    int i,j,el,k,l,ilow,ihigh,jlow,jhigh,coun=0;
    int data[9][9];
    for (i=0;i<9;i++)
    {
        for (j=0;j<9;j++)
        {
            cin >> el;
            if (el == 0)
            {
                coun = coun + 1;
            }
            data[i][j] = el;
        }
    }
    cout << "Given Sudoko Grid is " << endl;
    for (i=0;i<9;i++)
    {
        for (j=0;j<9;j++)
        {
            cout << data[i][j] << " ";
        }
        cout << endl;
    }
    cout << "coun is " << coun << endl;
    while (coun != 0)
    {
        cout << "coun is " << coun << endl;
        cout << "i is " << i << " j is " << j << endl;
        for (i=0;i<9;i++)
        {
            for (j=0;j<9;j++)
            {
                if (data[i][j] != 0)
                    continue;
                set<int>pos; //Creating Set
                for (k=1;k<=9;k++)
                {
                    pos.insert(k);
                }
                for (k=0;k<9;k++) //Check Vertical rows
                {
                    if (data[k][j] != 0)
                    {
                        if (pos.find(data[k][j]) != pos.end())
                        {
                            pos.erase(data[k][j]);
                        }
                    }
                }
                for (k=0;k<9;k++) //Check Horizontal Elements
                {
                    if (data[i][k] != 0)
                    {
                        if (pos.find(data[i][k]) != pos.end())
                        {
                            pos.erase(data[i][k]);
                        }
                    }
                }
                ilow = i - i%3;     //Setting bounds
                ihigh = i + (3-i%3);
                jlow = j - j%3;
                jhigh = j + (3-j%3);
                for (k=ilow;k<ihigh;k++)    //Checking in same box
                {
                    for (l=jlow;l<jhigh;l++)
                    {
                        if (pos.find(data[k][l]) != pos.end())
                        {
                            pos.erase(data[k][l]);
                        }
                    }
                }
                set<int>::iterator it;
                if (pos.size() == 1)
                {
                    it = pos.begin();
                    for (it=pos.begin();it != pos.end();++it)
                    {
                        data[i][j] = *it;
                    }
                    coun = coun - 1;
                }
            }
        }
    }
    cout << "Solved Sudoko grid is " << endl;
    for (i=0;i<9;i++)
    {
        for (j=0;j<9;j++)
        {
            cout << data[i][j] << " ";
        }
        cout << endl;
    }
    return 0;
}

