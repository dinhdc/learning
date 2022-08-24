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

void insertionSort(int arr[], int n){
    for(int startIndex = 0;startIndex < n;startIndex++){
        int newElement = arr[startIndex];
        int i;
        for(i=startIndex; i>0 && arr[i-1]>newElement; i--){
            arr[i] = arr[i-1];
        }
        arr[i] = newElement;
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
    insertionSort(arr, n);
    printArray(arr, n);
    delete arr;
}