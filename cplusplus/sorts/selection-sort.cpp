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

void selectionSort(int arr[], int n){
    for(int startIndex = 0;startIndex <= n-1;startIndex++){
        int minimum = startIndex;
        for(int i=startIndex+1; i < n; i++){
            if(arr[i] < arr[minimum]){
                minimum = i;
            } 
        }
        swapElementArray(arr, minimum, startIndex);
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
    selectionSort(arr, n);
    printArray(arr, n);
    delete arr;
}