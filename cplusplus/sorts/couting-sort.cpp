#include <bits/stdc++.h>
using namespace std;

void swapElementArray(int arr[], int i, int j)
{
    // function to swap element index i and index j
    if (i == j)
    {
        return;
    }
    int tmp = arr[i];
    arr[i] = arr[j];
    arr[j] = tmp;
}

void printArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

void countingSort(int arr[], int length, int min, int max)
{
    int *countArr = new int[(max - min) + 1];
    for (int i = 0; i < (max - min) + 1; i++)
    {
        countArr[i] = 0;
    }
    for (int i = 0; i < length; i++)
    {
        countArr[arr[i] - min]++;
    }
    int j = 0;
    for (int i = min; i < max; i++)
    {
        while (countArr[i - min] > 0)
        {
            arr[j++] = i;
            countArr[i - min]--;
        }
    }
}

void scanArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
}

int getMinElement(int arr[], int length)
{
    int min = arr[0];
    for (int i = 1; i < length; i++)
    {
        if (arr[i] < min)
            min = arr[i];
    }
    return min;
}

int getMaxElement(int arr[], int length)
{
    int max = arr[0];
    for (int i = 1; i < length; i++)
    {
        if (arr[i] > max)
            max = arr[i];
    }
    return max;
}

int main(int argc, char **argv)
{
    int n;
    cin >> n;
    int *arr = new int[n];
    scanArray(arr, n);
    int min = getMinElement(arr, n);
    int max = getMaxElement(arr, n);
    countingSort(arr, n, min, max);
    printArray(arr, n);
    delete arr;
}