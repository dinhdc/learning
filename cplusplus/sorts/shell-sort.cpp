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

void shellSort(int arr[], int n){
    for(int gap = n/2;gap>0;gap/=2){
        for(int i=gap; i<n;i++){
            int newElement = arr[i];
            int j=i;
            while (j>=gap && arr[j-gap]>newElement)
            {
                arr[j] = arr[j-gap];
                j -= gap;
            }
            arr[j] = newElement;            
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
    shellSort(arr, n);
    printArray(arr, n);
    delete arr;
}