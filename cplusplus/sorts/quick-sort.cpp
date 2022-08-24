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

int partition(int arr[], int start, int end){
    int pivot = arr[start];
    int i=start,j=end;
    while (i<j)
    {
        while (i<j && arr[--j]>=pivot);
        if(i<j){
            arr[i] = arr[j];
        }
        while (i<j && arr[++i]<=pivot);
        if(i<j){
            arr[j] = arr[i];
        }
    }
    arr[j] = pivot;
    return j;    
}

void quickSort(int arr[], int start, int end){
    if(end-start<2){
        return;
    }
    int pivotIndex = partition(arr, start, end);
    quickSort(arr, start, pivotIndex);
    quickSort(arr, pivotIndex+1, end);
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
    quickSort(arr, 0, n);
    printArray(arr, n);
    delete arr;
}