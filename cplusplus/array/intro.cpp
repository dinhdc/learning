#include<iostream>
using namespace std;

int main(){

   // initialize the array with length = 10 
   int a[10];

   for(int i=0;i<10;i++){
    // initialize value int array with value of array at index = index * index
    a[i] = i*i;
    cout<<a[i]<<" ";
   }
   cout<<endl;

   //int b;
   //cout<<sizeof(b)<<endl;

   int d[10] = {1,2,3};
   // get size of array
   cout<<sizeof(d);





   return 0;
}