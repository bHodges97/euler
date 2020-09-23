using System;

namespace ProjectEulerSolutions
{
    class Euler31
    {
        static int[] denominations = { 1, 2, 5, 10, 20, 50, 100, 200 };

        static void Main(string[] args)
        {
            int[] splits = new int[201];
            int ans = Split(200,200);

            Console.WriteLine(ans);
        }

        static int Split(int num,int lim)
        {            
            if (num == 0)
            {
                return 1;
            }
            int sum = 0;
            for(int i = 0; i < denominations.Length && denominations[i] <= lim && denominations[i] <= num; i++)
            {
                sum += Split(num - denominations[i], denominations[i]);
            }
            return sum;
        }
    }
}
