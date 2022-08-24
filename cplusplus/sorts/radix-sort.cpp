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

void scanArray(int arr[], int n)
{
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
}

int getDigit(int position, int value, int radix)
{
    return value / (int)pow(radix, position) % radix;
}

void radixSingleSort(int input[], int length, int position, int radix)
{

    int numItems = length;
    int *countArray = new int[radix];
    for (int i = 0; i < length; i++)
    {
        countArray[getDigit(position, input[i], radix)]++;
    }
    // Adjust the count array
    for (int j = 1; j < radix; j++)
    {
        countArray[j] += countArray[j - 1];
    }

    int *temp = new int[numItems];
    for (int tempIndex = numItems - 1; tempIndex >= 0; tempIndex--)
    {
        temp[--countArray[getDigit(position, input[tempIndex], radix)]] =
            input[tempIndex];
    }
    delete countArray;
    for (int tempIndex = 0; tempIndex < numItems; tempIndex++)
    {
        input[tempIndex] = temp[tempIndex];
    }
    delete temp;
}

void radixSort(int input[], int length, int radix, int width)
{
    for (int i = 0; i < width; i++)
    {
        radixSingleSort(input, length, i, radix);
    }
}

int main(int argc, char **argv)
{
    int n;
    cin >> n;
    int *arr = new int[n];
    scanArray(arr, n);
    radixSort(arr, n, 10, 4);
    printArray(arr, n);
    delete arr;
}