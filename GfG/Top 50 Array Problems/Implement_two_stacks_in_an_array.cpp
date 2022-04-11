//Function to push an integer into the stack1.
void twoStacks :: push1(int x)
{
    arr[this->top1++] = x;
}
   
//Function to push an integer into the stack2.
void twoStacks ::push2(int x)
{
    arr[this->top2--] = x;
}
   
//Function to remove an element from top of the stack1.
int twoStacks ::pop1()
{
    if (this->top1 == -1)
    {
        return -1;
    }
    else
    {
        this->top1--;
    }

    return arr[this->top1];
}

//Function to remove an element from top of the stack2.
int twoStacks :: pop2()
{
    if (this->top2 == this->size)
    {
        return -1;
    }
    else
    {
        this->top2++;
        return arr[this->top2];
    }
}