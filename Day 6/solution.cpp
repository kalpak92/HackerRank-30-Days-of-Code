#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include<string.h>
using namespace std;


int main() {
    int n;
    cin>>n;
int i;
    for(i=0;i<n;i++)
    {
        string str;
        cin>>str;

        for(int j=0;j<str.length();j++)
        {
            if(j%2==0)
            cout<<str[j];
        }
        cout<<" ";
        for(int j=0;j<str.length();j++)
        {
            if(j%2!=0)
            cout<<str[j];
        }
        cout<<endl;
    }
}

