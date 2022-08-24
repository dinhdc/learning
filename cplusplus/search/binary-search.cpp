#include <bits/stdc++.h>
using namespace std;

int binarySearch(int arr[], int n, int value){
    int start = 0;
    int end = n;
    while (start < end)
    {
        int mid = (start + end - 1)/2;
        if (arr[mid] == value) return mid;
        else if (arr[mid] > value)
        {
            end = mid;
        }else{
            start = mid;
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
    int index = binarySearch(arr, n, k);
    cout << index << endl;
    delete arr;
}