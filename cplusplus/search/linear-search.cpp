#include <bits/stdc++.h>
using namespace std;

int linearSearch(int arr[], int n, int value){
    for(int i = 0;i < n;i++){
        if(arr[i] == value){
            return i;
        }
    }
    return -1;
}

void scanArray(int arr[],int n){
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
}


int main(int argc, char **argv){
    int n,k;
    cin >> n >> k;
    int *arr = new int[n];
    scanArray(arr, n);
    int index = linearSearch(arr, n, k);
    cout << index << endl;
    delete arr;
}