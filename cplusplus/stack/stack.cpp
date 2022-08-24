#include <bits/stdc++.h>
using namespace std;

void push(int *arr, int newElement, int top)
{
    arr[top] = newElement;
}

void printList(int *arr, int top)
{
    for (int i = 0; i < top; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

bool isEmpty(int *arr)
{
    return sizeof(arr) == 0;
}

int pop(int *arr, int top)
{
    int lastElement = arr[top - 1];
    return lastElement;
}

int main(int argc, char **argv)
{
    int top = 0;
    int *stack = new int[top];
    bool loop = true;
    while (loop)
    {
        cout << "Choose options:" << endl;
        cout << "Options 1: add new element to stack" << endl;
        cout << "Options 2: remove last element from stack" << endl;
        cout << "Options 3: get size of stack" << endl;
        cout << "Options 4: check stack is empty" << endl;
        cout << "Options 5: print stack" << endl;
        cout << "Options 6: exit program!" << endl;
        cout << "Please enter your option: ";
        int choose;
        cin >> choose;
        cout << endl;
        switch (choose)
        {
            case 1:
                int newElement;
                cout << "Enter new element: ";
                cin >> newElement;
                push(stack, newElement, top);
                top+=1;
                break;
            case 2:
                pop(stack, top);
                top-=1;
                break;
            case 3:
                cout << "Size of stack: " << top << endl;
                break;
            case 4:
                cout << (isEmpty(stack) ? "Empty" : "Not Empty") << endl;
                break;
            case 5:
                printList(stack, top);
                break;
            case 6:
                loop = false;
                break;
            default:
                break;
        }

    }
}