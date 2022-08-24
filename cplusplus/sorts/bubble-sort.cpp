#include <bits/stdc++.h>
using namespace std;

void swapElementArray(int arr[], int i, int j){
    // function to swap element index i and index j
    if (i == j)
    {
        return;
    }
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void bubbleSort(int arr[], int n){
    for(int lastIndex = n-1;lastIndex >= 0;lastIndex--){
        for(int i=0; i<lastIndex; i++){
            if(arr[i] > arr[i+1]){
                swapElementArray(arr, i, i+1);
            }
        }
    }
}

void scanArray(int arr[],int n){
    for(int i = 0; i < n; i++){
        cin >> arr[i];
    }
}

void printArray(int arr[], int n){
    for(int i=0;i<n;i++){
        cout << arr[i] << " ";
    }
}

int main(int argc, char **argv){
    int n;
    cin >> n;
    int *arr = new int[n];
    scanArray(arr, n);
    bubbleSort(arr, n);
    printArray(arr, n);
    delete arr;
}